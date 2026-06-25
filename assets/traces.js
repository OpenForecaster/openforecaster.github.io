(function () {
  const dataBase = (window.FSIM_TRACE_DATA_BASE || './data/').replace(/\/?$/, '/');
  const state = { manifest: null, agent: '', runId: '', day: '', metric: 'brier_skill_score', currentDay: null, currentSummary: null, workspaceFile: '' };
  const chartColors = ['#0f766e', '#2563eb', '#b45309', '#9333ea', '#be123c', '#047857', '#4f46e5', '#a16207'];
  const summaryCache = new Map();
  const workspaceCache = new Map();
  const rawBatchSize = 24;

  const els = {
    agent: document.getElementById('trace-agent'),
    run: document.getElementById('trace-run'),
    day: document.getElementById('trace-day'),
    expandEnv: document.getElementById('trace-expand-env'),
    metricButtons: document.querySelectorAll('[data-trace-metric]'),
    trajectoryTitle: document.getElementById('trace-trajectory-title'),
    trajectoryMeta: document.getElementById('trace-trajectory-meta'),
    trajectoryChart: document.getElementById('trace-trajectory-chart'),
    buildMeta: document.getElementById('trace-build-meta'),
    rawLink: document.getElementById('trace-raw-link'),
    dayList: document.getElementById('trace-day-list'),
    stats: document.getElementById('trace-day-stats'),
    tools: document.getElementById('trace-tool-list'),
    workspaceStatus: document.getElementById('trace-workspace-status'),
    workspaceFiles: document.getElementById('trace-workspace-files'),
    workspaceContent: document.getElementById('trace-workspace-content'),
    status: document.getElementById('trace-status'),
    events: document.getElementById('trace-events'),
  };

  async function init() {
    try {
      const response = await fetch(dataBase + 'manifest.json', { cache: 'no-store' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      state.manifest = await response.json();
      if (els.rawLink && window.FSIM_RAW_TRACE_URL) els.rawLink.href = window.FSIM_RAW_TRACE_URL;
      populateAgents();
      wireControls();
      await loadSelection();
    } catch (error) {
      els.buildMeta.textContent = 'Trace index unavailable';
      els.status.textContent = `Could not load ${dataBase}manifest.json (${error.message}).`;
    }
  }

  function wireControls() {
    els.agent.addEventListener('change', () => {
      state.agent = els.agent.value;
      state.workspaceFile = '';
      populateRuns();
      loadSelection();
    });
    els.run.addEventListener('change', () => {
      state.runId = els.run.value;
      state.workspaceFile = '';
      populateDays();
      renderTrajectory();
      loadSelection();
    });
    els.day.addEventListener('change', () => {
      state.day = els.day.value;
      state.workspaceFile = '';
      loadSelection();
    });
    els.expandEnv.addEventListener('change', renderCurrentDay);
    for (const button of els.metricButtons) {
      button.addEventListener('click', () => {
        state.metric = button.dataset.traceMetric;
        for (const item of els.metricButtons) item.setAttribute('aria-pressed', String(item === button));
        renderTrajectory();
      });
    }
  }

  function populateAgents() {
    const agents = [...new Set(state.manifest.runs.map((run) => run.agent_slug))];
    fillSelect(els.agent, agents.map((slug) => {
      const run = state.manifest.runs.find((item) => item.agent_slug === slug);
      return { value: slug, label: run.agent_name || slug };
    }));
    state.agent = els.agent.value;
    populateRuns();
    const build = state.manifest.created_at_utc ? new Date(state.manifest.created_at_utc).toLocaleDateString() : '';
    els.buildMeta.textContent = `${state.manifest.runs.length} runs${build ? ` - built ${build}` : ''}`;
  }

  function populateRuns() {
    const runs = filteredRuns();
    fillSelect(els.run, runs.map((run) => ({
      value: run.run_id,
      label: runOptionLabel(run),
    })));
    state.runId = els.run.value;
    populateDays();
    renderTrajectory();
  }

  function populateDays(preferredDay) {
    const run = selectedRun();
    const days = sortedDays(run);
    fillSelect(els.day, days.map((day) => ({
      value: day.date,
      label: `${day.date} - ${day.event_count} actions`,
    })));
    if (preferredDay && days.some((day) => day.date === preferredDay)) els.day.value = preferredDay;
    state.day = els.day.value;
    renderDayRail();
  }

  function fillSelect(select, options) {
    select.replaceChildren();
    for (const option of options) {
      const node = document.createElement('option');
      node.value = option.value;
      node.textContent = option.label;
      select.appendChild(node);
    }
  }

  function filteredRuns() {
    return state.manifest.runs.filter((run) => run.agent_slug === state.agent);
  }

  function selectedRun() {
    return state.manifest.runs.find((run) => run.agent_slug === state.agent && run.run_id === state.runId);
  }

  function sortedDays(run) {
    return [...((run && run.days) || [])].sort((a, b) => a.date.localeCompare(b.date));
  }

  async function loadSelection() {
    const run = selectedRun();
    const day = run && run.days.find((item) => item.date === state.day);
    if (!run || !day) {
      state.currentDay = null;
      state.currentSummary = null;
      state.workspaceFile = '';
      renderCurrentDay();
      return;
    }
    els.status.textContent = 'Loading day shard...';
    els.events.replaceChildren();
    const response = await fetch(dataBase + day.path, { cache: 'no-store' });
    if (!response.ok) {
      els.status.textContent = `Could not load ${day.path} (HTTP ${response.status}).`;
      return;
    }
    state.currentDay = await response.json();
    state.currentSummary = await loadRunSummary(run);
    renderCurrentDay();
  }

  async function loadRunSummary(run) {
    if (!run) return null;
    const cacheKey = `${run.agent_slug}/${run.run_id}`;
    if (summaryCache.has(cacheKey)) return summaryCache.get(cacheKey);
    const path = `summaries/${encodeURIComponent(run.agent_slug)}__${encodeURIComponent(run.run_id)}.json`;
    try {
      const response = await fetch(dataBase + path, { cache: 'no-store' });
      if (!response.ok) {
        summaryCache.set(cacheKey, null);
        return null;
      }
      const payload = await response.json();
      summaryCache.set(cacheKey, payload);
      return payload;
    } catch (_) {
      summaryCache.set(cacheKey, null);
      return null;
    }
  }

  async function loadWorkspace(run) {
    if (!run || !run.workspace || !run.workspace.manifest_path) return null;
    const cacheKey = `${run.agent_slug}/${run.run_id}`;
    if (workspaceCache.has(cacheKey)) return workspaceCache.get(cacheKey);
    try {
      const response = await fetch(dataBase + run.workspace.manifest_path, { cache: 'no-store' });
      if (!response.ok) {
        workspaceCache.set(cacheKey, null);
        return null;
      }
      const payload = await response.json();
      workspaceCache.set(cacheKey, payload);
      return payload;
    } catch (_) {
      workspaceCache.set(cacheKey, null);
      return null;
    }
  }

  function renderCurrentDay() {
    const run = selectedRun();
    const day = state.currentDay;
    renderRunStats(run);
    renderDayRail();
    renderWorkspace(run);
    els.events.replaceChildren();
    if (!run || !day) {
      els.status.textContent = 'No trace day selected.';
      els.tools.replaceChildren();
      return;
    }

    const resultById = new Map();
    for (const event of day.events) {
      for (const block of event.blocks || []) {
        if (block.type === 'tool_result' && block.tool_use_id) resultById.set(block.tool_use_id, block);
      }
    }

    const visible = visibleActionEvents(day.events);
    const summary = summaryForCurrentDay(run, day, visible);
    els.status.textContent = visible.length ? 'Summarized trace.' : 'No visible actions for this day.';
    els.events.appendChild(renderDaySummary(summary, day, visible, resultById));

    renderToolList(run);
  }

  function renderTrajectory() {
    const runs = filteredRuns().filter((run) => run.metrics && run.metrics.length);
    els.trajectoryChart.replaceChildren();
    const selected = selectedRun();
    els.trajectoryTitle.textContent = `${selected ? selected.agent_name : 'Run'} trajectories`;
    els.trajectoryMeta.textContent = metricLabel(state.metric);
    if (!runs.length) {
      els.trajectoryChart.appendChild(el('div', 'No daily metrics for this model and harness.', 'trace-status'));
      return;
    }

    const points = runs.map((run, index) => ({
      run,
      color: chartColors[index % chartColors.length],
      values: run.metrics
        .filter((row) => Number.isFinite(row[state.metric]))
        .map((row) => ({ date: row.date, day: dayIndex(row.date), value: Number(row[state.metric]) })),
    })).filter((series) => series.values.length);
    if (!points.length) {
      els.trajectoryChart.appendChild(el('div', 'No values for this metric.', 'trace-status'));
      return;
    }

    const allValues = points.flatMap((series) => series.values);
    const minDay = Math.min(...allValues.map((point) => point.day));
    const maxDay = Math.max(...allValues.map((point) => point.day));
    let minValue = Math.min(...allValues.map((point) => point.value));
    let maxValue = Math.max(...allValues.map((point) => point.value));
    const pad = Math.max((maxValue - minValue) * 0.08, state.metric === 'top1_accuracy' ? 1 : 0.005);
    minValue -= pad;
    maxValue += pad;

    const width = 1100;
    const height = 330;
    const margin = { top: 16, right: 24, bottom: 42, left: 76 };
    const plotW = width - margin.left - margin.right;
    const plotH = height - margin.top - margin.bottom;
    const x = (day) => margin.left + (maxDay === minDay ? plotW / 2 : (day - minDay) / (maxDay - minDay) * plotW);
    const y = (value) => margin.top + (maxValue === minValue ? plotH / 2 : (maxValue - value) / (maxValue - minValue) * plotH);
    const tooltip = document.createElement('div');
    tooltip.className = 'trace-chart-tooltip';
    els.trajectoryChart.appendChild(tooltip);

    const svg = svgEl('svg', { viewBox: `0 0 ${width} ${height}`, role: 'img', 'aria-label': `${metricLabel(state.metric)} trajectories` });
    for (const tick of valueTicks(minValue, maxValue, 5)) {
      svg.appendChild(svgEl('line', { x1: margin.left, x2: width - margin.right, y1: y(tick), y2: y(tick), class: 'trace-chart-grid' }));
      const label = svgEl('text', { x: margin.left - 10, y: y(tick) + 4, 'text-anchor': 'end', class: 'trace-chart-label' });
      label.textContent = formatMetric(tick, state.metric);
      svg.appendChild(label);
    }
    for (const tick of dayTicks(minDay, maxDay, 5)) {
      svg.appendChild(svgEl('line', { x1: x(tick), x2: x(tick), y1: margin.top, y2: height - margin.bottom, class: 'trace-chart-grid' }));
      const label = svgEl('text', { x: x(tick), y: height - 12, 'text-anchor': 'middle', class: 'trace-chart-label' });
      label.textContent = formatShortDate(dateFromDay(tick));
      svg.appendChild(label);
    }
    svg.appendChild(svgEl('line', { x1: margin.left, x2: width - margin.right, y1: height - margin.bottom, y2: height - margin.bottom, class: 'trace-chart-axis' }));
    svg.appendChild(svgEl('line', { x1: margin.left, x2: margin.left, y1: margin.top, y2: height - margin.bottom, class: 'trace-chart-axis' }));
    const yLabel = svgEl('text', {
      x: 18,
      y: margin.top + plotH / 2,
      transform: `rotate(-90 18 ${margin.top + plotH / 2})`,
      'text-anchor': 'middle',
      class: 'trace-chart-axis-title',
    });
    yLabel.textContent = axisMetricLabel(state.metric);
    svg.appendChild(yLabel);

    for (const series of points) {
      const path = series.values.map((point, index) => `${index ? 'L' : 'M'}${x(point.day).toFixed(1)},${y(point.value).toFixed(1)}`).join(' ');
      const isSelected = series.run.run_id === state.runId;
      svg.appendChild(svgEl('path', {
        d: path,
        stroke: series.color,
        class: `trace-chart-line${isSelected ? ' is-selected' : ''}`,
      }));
      const last = series.values[series.values.length - 1];
      svg.appendChild(svgEl('circle', {
        cx: x(last.day),
        cy: y(last.value),
        r: isSelected ? 4 : 3,
        fill: series.color,
        class: 'trace-chart-point',
      }));
      for (const point of series.values) {
        const dayMeta = series.run.days.find((day) => day.date === point.date);
        const hit = svgEl('circle', {
          cx: x(point.day),
          cy: y(point.value),
          r: isSelected ? 8 : 7,
          class: 'trace-chart-hit',
          tabindex: '0',
          role: 'button',
          'aria-label': `${runOptionLabel(series.run)}, ${point.date}, ${metricLabel(state.metric)} ${formatMetric(point.value, state.metric)}, ${dayMeta ? dayMeta.event_count : 0} actions`,
        });
        hit.addEventListener('mouseenter', () => showTooltip(tooltip, point, dayMeta, x(point.day), y(point.value), width, state.metric, series.run));
        hit.addEventListener('mousemove', () => showTooltip(tooltip, point, dayMeta, x(point.day), y(point.value), width, state.metric, series.run));
        hit.addEventListener('mouseleave', () => hideTooltip(tooltip));
        hit.addEventListener('focus', () => showTooltip(tooltip, point, dayMeta, x(point.day), y(point.value), width, state.metric, series.run));
        hit.addEventListener('blur', () => hideTooltip(tooltip));
        hit.addEventListener('click', () => selectRunDay(series.run.run_id, point.date));
        hit.addEventListener('keydown', (event) => {
          if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            selectRunDay(series.run.run_id, point.date);
          }
        });
        svg.appendChild(hit);
      }
    }
    els.trajectoryChart.appendChild(svg);

    const legend = document.createElement('div');
    legend.className = 'trace-chart-legend';
    for (const series of points) {
      const item = document.createElement('span');
      item.style.color = series.color;
      item.appendChild(el('i', '', 'trace-chart-swatch'));
      item.appendChild(document.createTextNode(runOptionLabel(series.run)));
      if (series.run.run_id === state.runId) item.style.fontWeight = '650';
      legend.appendChild(item);
    }
    els.trajectoryChart.appendChild(legend);
  }

  function shouldShowEvent(event) {
    if (event.kind === 'tool_result') return false;
    if (event.kind === 'user' && isOnlyToolResults(event)) return false;
    if (!event.preview && !(event.blocks || []).some((block) => block.type === 'tool_use' || block.type === 'compaction' || (block.type === 'text' && String(block.text || '').trim()))) return false;
    return true;
  }

  function isOnlyToolResults(event) {
    const blocks = event.blocks || [];
    return blocks.length > 0 && blocks.every((block) => block.type === 'tool_result');
  }

  function visibleActionEvents(events) {
    return (events || []).filter((event) => shouldShowEvent(event) && !isOnlyToolResults(event));
  }

  function summaryForCurrentDay(run, day, visible) {
    const date = day && day.sim_date;
    const curated = state.currentSummary && Array.isArray(state.currentSummary.days)
      ? state.currentSummary.days.find((item) => item.date === date)
      : null;
    if (curated) return { ...curated, source: 'curated' };
    return buildAutoSummary(run, day, visible);
  }

  function buildAutoSummary(run, day, visible) {
    const date = day && day.sim_date ? day.sim_date : state.day;
    const toolCounts = countToolsForEvents(visible);
    const forecastCount = toolCounts.get('submit_forecasts') || 0;
    const searchCount = toolCounts.get('search_news') || 0;
    const titleBits = [];
    if (forecastCount) titleBits.push(`${forecastCount} forecast update${forecastCount === 1 ? '' : 's'}`);
    if (searchCount) titleBits.push(`${searchCount} search${searchCount === 1 ? '' : 'es'}`);
    const title = titleBits.length
      ? `Auto summary: ${titleBits.join(', ')}.`
      : 'Auto summary: reviewed the day and advanced through available actions.';
    return {
      date,
      source: 'auto',
      title,
      display_summary: `${run ? run.agent_name || run.agent_slug : 'This run'} had no curated summary sidecar for this day, so consecutive actions are grouped by tool type.`,
      stats: {
        action_count: visible.length,
        tool_call_count: [...toolCounts.values()].reduce((acc, count) => acc + count, 0),
        forecast_count: forecastCount,
      },
      segments: buildAutoSegments(date, visible),
    };
  }

  function buildAutoSegments(date, visible) {
    const segments = [];
    let active = null;
    const flush = () => {
      if (!active || !active.events.length) return;
      const tools = [...new Set(active.events.flatMap(eventTools))];
      segments.push({
        id: `auto-${date}-${String(segments.length + 1).padStart(2, '0')}`,
        auto: true,
        event_idx_start: active.events[0].idx,
        event_idx_end: active.events[active.events.length - 1].idx,
        label: autoSegmentLabel(active.kind, active.events),
        summary: autoSegmentSummary(active.kind, active.events, tools),
        tools,
        representative_event_idxs: active.events.slice(0, 4).map((event) => event.idx),
      });
      active = null;
    };

    for (const event of visible) {
      const kind = eventCategory(event);
      if (!active || active.kind !== kind || active.events.length >= rawBatchSize) {
        flush();
        active = { kind, events: [] };
      }
      active.events.push(event);
    }
    flush();
    return segments;
  }

  function eventCategory(event) {
    const tools = eventTools(event);
    if (tools.some(isSubmitForecastTool)) return 'forecast';
    if (tools.some(isSearchNewsTool)) return 'search';
    if (tools.some((tool) => String(tool || '').includes('next_day'))) return 'advance';
    if (tools.some(isBashTool)) return 'workspace';
    if ((event.blocks || []).some((block) => block.type === 'compaction')) return 'compaction';
    if (tools.length) return 'tool';
    return 'reasoning';
  }

  function autoSegmentLabel(kind, events) {
    const count = events.length;
    const labels = {
      forecast: 'Forecast updates',
      search: 'News search sweep',
      advance: 'Advance day',
      workspace: 'Workspace and market checks',
      compaction: 'Context compaction',
      reasoning: 'Reasoning note',
      tool: 'Tool actions',
    };
    return count > 1 ? `${labels[kind] || 'Actions'} (${count})` : labels[kind] || 'Action';
  }

  function autoSegmentSummary(kind, events, tools) {
    const count = events.length;
    if (kind === 'forecast') return `Submitted ${count} forecast action${count === 1 ? '' : 's'} for this consecutive update block.`;
    if (kind === 'search') return `Ran ${count} news search${count === 1 ? '' : 'es'} to collect evidence for active markets.`;
    if (kind === 'workspace') return `Used local commands to inspect market files, article bundles, memory, or run state.`;
    if (kind === 'advance') return `Called next_day and moved the simulation forward.`;
    if (kind === 'reasoning') return `Recorded a short reasoning or handoff note before the next tool actions.`;
    return `Ran ${count} action${count === 1 ? '' : 's'} with ${tools.map(prettyToolName).join(', ') || 'tools'}.`;
  }

  function renderDaySummary(summary, day, visible, resultById) {
    const wrap = document.createElement('div');
    wrap.className = 'trace-day-story';

    const header = document.createElement('header');
    header.className = 'trace-story-header';
    const title = document.createElement('div');
    title.appendChild(el('span', formatShortDate(summary.date || day.sim_date), 'trace-story-date'));
    title.appendChild(el('h2', summary.title || 'Day summary'));
    header.appendChild(title);
    const pills = document.createElement('div');
    pills.className = 'trace-story-pills';
    pills.appendChild(el('span', summary.source === 'curated' ? 'curated' : 'auto grouped'));
    pills.appendChild(el('span', `${visible.length} actions`));
    const forecastCount = summary.stats && Number.isFinite(Number(summary.stats.forecast_count)) ? Number(summary.stats.forecast_count) : countToolsForEvents(visible).get('submit_forecasts') || 0;
    pills.appendChild(el('span', `${forecastCount} forecasts`));
    header.appendChild(pills);
    wrap.appendChild(header);

    if (summary.display_summary) wrap.appendChild(el('p', summary.display_summary, 'trace-story-copy'));

    const segmentList = document.createElement('div');
    segmentList.className = 'trace-summary-segments';
    const segments = Array.isArray(summary.segments) ? summary.segments : [];
    if (!segments.length) {
      segmentList.appendChild(el('div', 'No summary segments available for this day.', 'trace-empty'));
    } else {
      segments.forEach((segment, index) => {
        segmentList.appendChild(renderSummarySegment(segment, day, resultById, index));
      });
    }
    wrap.appendChild(segmentList);
    return wrap;
  }

  function renderSummarySegment(segment, day, resultById, index) {
    const details = document.createElement('details');
    details.className = 'trace-summary-segment';
    details.id = segment.id || `segment-${index + 1}`;

    const summary = document.createElement('summary');
    summary.className = 'trace-summary-row';
    summary.appendChild(el('span', String(index + 1).padStart(2, '0'), 'trace-summary-index'));
    const text = document.createElement('div');
    text.className = 'trace-summary-text';
    text.appendChild(el('h3', segment.label || `Segment ${index + 1}`));
    text.appendChild(el('p', segment.summary || 'Expand to inspect this action sequence.'));
    summary.appendChild(text);
    summary.appendChild(renderSegmentPills(segment, day));
    details.appendChild(summary);

    const body = document.createElement('div');
    body.className = 'trace-summary-body';
    details.appendChild(body);
    details.addEventListener('toggle', () => {
      if (!details.open || body.dataset.loaded) return;
      renderSegmentBody(body, segment, day, resultById);
      body.dataset.loaded = 'true';
    });
    return details;
  }

  function renderSegmentPills(segment, day) {
    const pills = document.createElement('div');
    pills.className = 'trace-segment-pills';
    pills.appendChild(el('span', segmentRangeLabel(segment)));
    const events = segmentEvents(day, segment);
    pills.appendChild(el('span', `${visibleActionEvents(events).length} raw actions`));
    const tools = segment.tools && segment.tools.length ? segment.tools : [...new Set(events.flatMap(eventTools))];
    for (const tool of tools.slice(0, 3)) pills.appendChild(el('span', prettyToolName(tool)));
    if (tools.length > 3) pills.appendChild(el('span', `+${tools.length - 3}`));
    return pills;
  }

  function renderSegmentBody(body, segment, day, resultById) {
    body.replaceChildren();
    appendSegmentInsights(body, segment);
    const events = visibleActionEvents(segmentEvents(day, segment));
    if (!events.length) {
      body.appendChild(el('div', 'No raw actions found for this segment range.', 'trace-empty'));
      return;
    }
    const intro = document.createElement('div');
    intro.className = 'trace-raw-intro';
    intro.appendChild(el('strong', 'Raw trace'));
    intro.appendChild(el('span', events.length > rawBatchSize
      ? `${events.length} actions split into ${Math.ceil(events.length / rawBatchSize)} batches.`
      : `${events.length} action${events.length === 1 ? '' : 's'}.`));
    body.appendChild(intro);
    if (events.length > rawBatchSize) body.appendChild(renderRawBatches(events, resultById));
    else body.appendChild(renderRawEventList(events, resultById));
  }

  function appendSegmentInsights(body, segment) {
    if (Array.isArray(segment.notable_facts) && segment.notable_facts.length) {
      const facts = document.createElement('ul');
      facts.className = 'trace-segment-facts';
      for (const fact of segment.notable_facts) facts.appendChild(el('li', fact));
      body.appendChild(facts);
    }
    const forecasts = segment.forecast_updates || segment.representative_forecasts || [];
    if (forecasts.length) {
      const list = document.createElement('div');
      list.className = 'trace-forecast-summary-list';
      for (const item of forecasts) {
        const row = document.createElement('div');
        row.className = 'trace-forecast-summary';
        row.appendChild(el('strong', item.question_id ? `qid ${item.question_id}` : `event ${item.event_idx || ''}`));
        row.appendChild(el('span', item.summary || 'Forecast update'));
        if (item.event_idx) row.appendChild(el('code', `#${item.event_idx}`));
        list.appendChild(row);
      }
      body.appendChild(list);
    }
  }

  function renderRawBatches(events, resultById) {
    const list = document.createElement('div');
    list.className = 'trace-raw-batches';
    for (let start = 0; start < events.length; start += rawBatchSize) {
      const batch = events.slice(start, start + rawBatchSize);
      const details = document.createElement('details');
      details.className = 'trace-raw-batch';
      const label = `${segmentRangeLabel({ event_idx_start: batch[0].idx, event_idx_end: batch[batch.length - 1].idx })} · ${batch.length} actions · ${batchToolLabel(batch)}`;
      details.appendChild(el('summary', label));
      const body = document.createElement('div');
      body.className = 'trace-raw-batch-body';
      details.appendChild(body);
      details.addEventListener('toggle', () => {
        if (!details.open || body.dataset.loaded) return;
        body.appendChild(renderRawEventList(batch, resultById));
        body.dataset.loaded = 'true';
      });
      list.appendChild(details);
    }
    return list;
  }

  function renderRawEventList(events, resultById) {
    const list = document.createElement('div');
    list.className = 'trace-raw-event-list';
    appendRenderedEvents(list, events, resultById);
    return list;
  }

  function appendRenderedEvents(container, events, resultById) {
    for (let i = 0; i < events.length; i += 1) {
      const event = events[i];
      if (isMarketCsvBashEvent(event) && isMarketCsvBashEvent(events[i + 1])) {
        const group = [];
        while (i < events.length && isMarketCsvBashEvent(events[i])) {
          group.push(events[i]);
          i += 1;
        }
        i -= 1;
        container.appendChild(renderBashGroup(group, resultById));
        continue;
      }
      container.appendChild(renderEvent(event, resultById));
    }
  }

  function segmentEvents(day, segment) {
    const events = (day && day.events) || [];
    const start = Number(segment.event_idx_start);
    const end = Number(segment.event_idx_end);
    if (!Number.isFinite(start) || !Number.isFinite(end)) return [];
    return events.filter((event) => event.idx >= start && event.idx <= end);
  }

  function segmentRangeLabel(segment) {
    const start = segment.event_idx_start;
    const end = segment.event_idx_end;
    return start === end ? `event ${start}` : `events ${start}-${end}`;
  }

  function eventTools(event) {
    return [...new Set((event.blocks || [])
      .filter((block) => block.type === 'tool_use')
      .map((block) => block.name || 'tool'))];
  }

  function countToolsForEvents(events) {
    const counts = new Map();
    for (const event of events || []) {
      for (const tool of eventTools(event)) counts.set(tool, (counts.get(tool) || 0) + 1);
    }
    return counts;
  }

  function batchToolLabel(events) {
    const counts = [...countToolsForEvents(events).entries()].sort((a, b) => b[1] - a[1]);
    if (!counts.length) return 'notes';
    return counts.slice(0, 2).map(([tool, count]) => `${prettyToolName(tool)} x${count}`).join(', ');
  }

  function renderRunStats(run) {
    els.stats.replaceChildren();
    if (!run) return;
    const days = sortedDays(run);
    const totals = days.reduce((acc, day) => {
      acc.actions += Number(day.event_count) || 0;
      acc.toolCalls += Number(day.tool_call_count) || 0;
      acc.forecasts += Number(day.forecast_count) || 0;
      return acc;
    }, { actions: 0, toolCalls: 0, forecasts: 0 });
    const pairs = [
      ['model', run.agent_name || run.agent_slug],
      ['run', runOptionLabel(run)],
      ['days', days.length],
      ['actions', totals.actions],
      ['tool calls', totals.toolCalls],
      ['forecast submits', totals.forecasts],
    ];
    for (const [label, value] of pairs) {
      els.stats.appendChild(el('dt', label));
      els.stats.appendChild(el('dd', String(value)));
    }
  }

  function renderDayRail() {
    if (!els.dayList) return;
    const run = selectedRun();
    const days = sortedDays(run);
    els.dayList.replaceChildren();
    for (const day of days) {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = `trace-day-button${day.date === state.day ? ' is-active' : ''}`;
      button.title = `${formatShortDate(day.date)}\n${day.event_count} actions\n${day.tool_call_count} tool calls\n${day.forecast_count} forecasts`;
      button.setAttribute('aria-pressed', String(day.date === state.day));
      button.appendChild(el('span', formatShortDate(day.date), 'trace-day-date'));
      button.appendChild(el('span', `${day.event_count} actions`, 'trace-day-meta'));
      button.addEventListener('click', () => selectDay(day.date));
      els.dayList.appendChild(button);
      if (day.date === state.day) requestAnimationFrame(() => button.scrollIntoView({ block: 'nearest' }));
    }
  }

  function renderToolList(run) {
    const counts = new Map(Object.entries((run && run.tool_counts) || {}));
    els.tools.replaceChildren();
    for (const [name, count] of [...counts.entries()].sort((a, b) => b[1] - a[1])) {
      const row = document.createElement('div');
      row.className = 'trace-tool-row';
      row.appendChild(el('span', prettyToolName(name)));
      row.appendChild(el('strong', String(count)));
      els.tools.appendChild(row);
    }
    if (!counts.size) els.tools.appendChild(el('div', 'No tool calls in this run.'));
  }

  function renderWorkspace(run) {
    if (!els.workspaceFiles || !els.workspaceContent || !els.workspaceStatus) return;
    const token = `${state.agent}/${state.runId}/${state.day}`;
    els.workspaceFiles.replaceChildren();
    els.workspaceContent.textContent = '';
    if (!run || !run.workspace) {
      els.workspaceStatus.textContent = 'No workspace export';
      return;
    }
    els.workspaceStatus.textContent = 'Loading workspace...';
    loadWorkspace(run).then((workspace) => {
      if (token !== `${state.agent}/${state.runId}/${state.day}`) return;
      const files = workspaceFilesForDay((workspace && workspace.files) || [], state.day);
      if (!files.length) {
        els.workspaceStatus.textContent = 'No memory files';
        return;
      }
      const selected = files.find((file) => file.path === state.workspaceFile) || defaultWorkspaceFile(files, state.day);
      state.workspaceFile = selected ? selected.path : '';
      els.workspaceStatus.textContent = `${workspace.files.length} files`;
      for (const file of files) {
        const button = document.createElement('button');
        button.type = 'button';
        button.className = `trace-workspace-file${file.path === state.workspaceFile ? ' is-active' : ''}`;
        button.title = `${file.label}${file.date ? `\n${file.date}` : ''}\n${formatBytes(file.size)}`;
        button.appendChild(el('strong', workspaceFileName(file.label)));
        button.appendChild(el('span', [file.kind, file.date || 'cumulative', formatBytes(file.size)].join(' - ')));
        button.addEventListener('click', () => {
          state.workspaceFile = file.path;
          renderWorkspace(run);
        });
        els.workspaceFiles.appendChild(button);
      }
      if (selected) renderWorkspaceFile(selected, token);
    });
  }

  function workspaceFilesForDay(files, day) {
    return [...files].sort((a, b) => workspaceFileRank(a, day) - workspaceFileRank(b, day) || a.label.localeCompare(b.label));
  }

  function workspaceFileRank(file, day) {
    const kindRank = file.kind === 'memory' ? 0 : file.kind === 'predictions' ? 1 : 2;
    if (file.date === day) return kindRank * 100000;
    if (file.date && file.date < day) return kindRank * 100000 + 1000 + dayIndex(day) - dayIndex(file.date);
    if (!file.date) return kindRank * 100000 + 5000;
    return kindRank * 100000 + 9000 + dayIndex(file.date) - dayIndex(day);
  }

  function defaultWorkspaceFile(files, day) {
    return files.find((file) => file.kind === 'memory' && file.date === day)
      || files.find((file) => file.kind === 'predictions' && file.date === day)
      || files.find((file) => file.kind === 'memory' && file.date && file.date < day)
      || files.find((file) => file.kind === 'memory' && !file.date)
      || files[0];
  }

  async function renderWorkspaceFile(file, token) {
    els.workspaceContent.textContent = 'Loading file...';
    const response = await fetch(dataBase + file.path.split('/').map(encodeURIComponent).join('/'), { cache: 'no-store' });
    if (token !== `${state.agent}/${state.runId}/${state.day}` || file.path !== state.workspaceFile) return;
    if (!response.ok) {
      els.workspaceContent.textContent = `Could not load ${file.label} (HTTP ${response.status}).`;
      return;
    }
    const text = await response.text();
    els.workspaceContent.textContent = text;
  }

  function workspaceFileName(label) {
    return label.split('/').pop() || label;
  }

  function formatBytes(value) {
    const bytes = Number(value) || 0;
    if (bytes >= 1000000) return `${(bytes / 1000000).toFixed(1)} MB`;
    if (bytes >= 1000) return `${Math.round(bytes / 1000)} KB`;
    return `${bytes} B`;
  }

  function renderEvent(event, resultById) {
    const item = document.createElement('article');
    item.className = `trace-event trace-event-${event.kind || 'event'}`;
    item.id = `event-${event.idx}`;

    const marker = document.createElement('aside');
    marker.className = 'trace-marker';
    marker.appendChild(el('strong', event.kind === 'assistant' ? `#${event.turn || event.idx}` : event.kind === 'compaction' ? 'compact' : event.kind));
    marker.appendChild(el('span', event.time || ''));
    item.appendChild(marker);

    const content = document.createElement('div');
    content.className = 'trace-body-content';
    for (const block of event.blocks || []) {
      if (block.type === 'text') content.appendChild(renderText(block.text));
      if (block.type === 'tool_use') content.appendChild(renderToolUse(block, resultById.get(block.id)));
      if (block.type === 'system') content.appendChild(renderText(block.text));
      if (block.type === 'compaction') content.appendChild(renderCompaction(block.text));
    }
    if (!content.childNodes.length && event.preview) content.appendChild(renderText(event.preview));
    item.appendChild(content);
    return item;
  }

  function renderText(text) {
    const p = document.createElement('p');
    p.className = 'trace-text';
    p.textContent = text || '';
    return p;
  }

  function renderCompaction(text) {
    const row = document.createElement('div');
    row.className = 'trace-compaction';
    row.appendChild(el('strong', 'Context compacted'));
    const detail = String(text || '').replace(/^Context compacted:?\s*/, '');
    if (detail && detail !== String(text || '')) row.appendChild(el('span', detail));
    return row;
  }

  function renderToolUse(block, result) {
    if (isSubmitForecastTool(block.name)) return renderForecastTool(block, result);
    if (isBashTool(block.name)) return renderBashTool(block, result);
    if (isSearchNewsTool(block.name)) return renderSearchTool(block, result);

    const wrap = document.createElement('section');
    wrap.className = `tool-call${result && result.is_error ? ' trace-error' : ''}`;
    const header = document.createElement('div');
    header.className = 'tool-call-header';
    const title = document.createElement('div');
    title.className = 'tool-call-title';
    title.appendChild(el('strong', prettyToolName(block.name)));
    header.appendChild(title);
    header.appendChild(el('span', toolKind(block.name), 'tool-pill'));
    wrap.appendChild(header);

    const args = document.createElement('div');
    args.className = 'tool-args';
    args.appendChild(pre(block.input));
    wrap.appendChild(args);

    appendToolOutput(wrap, result);
    return wrap;
  }

  function renderForecastTool(block, result) {
    const input = block.input || {};
    const outcomes = input.outcomes && typeof input.outcomes === 'object' ? input.outcomes : {};
    const previous = input.previous_outcomes && typeof input.previous_outcomes === 'object' ? input.previous_outcomes : {};
    const hasPrevious = Object.keys(previous).length > 0;
    const rows = Object.entries(outcomes)
      .filter(([, value]) => Number.isFinite(Number(value)))
      .sort((a, b) => Number(b[1]) - Number(a[1]));

    const wrap = document.createElement('section');
    wrap.className = `tool-call tool-call-forecast${result && result.is_error ? ' trace-error' : ''}`;
    const header = document.createElement('div');
    header.className = 'forecast-header';
    header.appendChild(el('strong', 'Submit forecast'));
    if (input.question_id) header.appendChild(el('span', hasPrevious ? `qid ${input.question_id}` : `qid ${input.question_id} - first forecast`));
    wrap.appendChild(header);

    const list = document.createElement('div');
    list.className = 'forecast-bars';
    for (const [name, value] of rows) {
      const prob = Number(value);
      const prior = Number(previous[name]);
      const row = document.createElement('div');
      row.className = 'forecast-row';

      const label = document.createElement('div');
      label.className = 'forecast-label';
      label.appendChild(el('span', name));
      const meta = document.createElement('span');
      meta.className = 'forecast-value';
      meta.appendChild(document.createTextNode(formatProbability(prob)));
      if (Number.isFinite(prior)) meta.appendChild(el('span', formatDelta(prob - prior), `forecast-delta ${prob - prior >= 0 ? 'is-up' : 'is-down'}`));
      else if (hasPrevious) meta.appendChild(el('span', 'new', 'forecast-delta'));
      label.appendChild(meta);
      row.appendChild(label);

      const track = document.createElement('div');
      track.className = 'forecast-track';
      const bar = document.createElement('i');
      bar.style.width = `${Math.max(0, Math.min(100, prob * 100))}%`;
      track.appendChild(bar);
      row.appendChild(track);
      list.appendChild(row);
    }
    wrap.appendChild(list);
    appendToolOutput(wrap, result);
    return wrap;
  }

  function renderBashTool(block, result) {
    const wrap = document.createElement('section');
    wrap.className = `tool-call tool-call-bash${result && result.is_error ? ' trace-error' : ''}`;
    wrap.appendChild(el('div', 'Bash', 'tool-terminal-label'));
    const command = bashCommand(block);
    const terminal = document.createElement('pre');
    terminal.className = 'tool-terminal';
    terminal.textContent = command ? `$ ${command}` : '$';
    wrap.appendChild(terminal);
    appendToolOutput(wrap, result);
    return wrap;
  }

  function renderBashGroup(events, resultById) {
    const first = events[0];
    const item = document.createElement('article');
    item.className = 'trace-event trace-bash-group-event';
    item.id = `event-${first.idx}-group`;

    const marker = document.createElement('aside');
    marker.className = 'trace-marker';
    marker.appendChild(el('strong', `#${first.turn || first.idx}`));
    marker.appendChild(el('span', first.time || ''));
    item.appendChild(marker);

    const details = document.createElement('details');
    details.className = 'trace-bash-group';
    const commands = events.flatMap((event) => (event.blocks || []).filter((block) => block.type === 'tool_use' && isBashTool(block.name)).map(bashCommand));
    details.appendChild(el('summary', `Bash questions exploration - ${commands.length} market.csv commands`));
    const preview = document.createElement('pre');
    preview.className = 'trace-bash-group-preview';
    preview.textContent = commands.slice(0, 6).map((command) => `$ ${command}`).join('\n');
    details.appendChild(preview);
    const body = document.createElement('div');
    body.className = 'trace-bash-group-body';
    for (const event of events) body.appendChild(renderEvent(event, resultById));
    details.appendChild(body);
    item.appendChild(details);
    return item;
  }

  function renderSearchTool(block, result) {
    const wrap = document.createElement('section');
    wrap.className = `tool-call tool-call-search${result && result.is_error ? ' trace-error' : ''}`;
    const query = block.input && block.input.query ? String(block.input.query) : toolSubtitle(block);
    const box = document.createElement('div');
    box.className = 'search-query';
    box.appendChild(el('strong', 'Search News'));
    box.appendChild(el('span', query || '(empty query)'));
    wrap.appendChild(box);
    appendToolOutput(wrap, result);
    return wrap;
  }

  function appendToolOutput(wrap, result) {
    if (!result) return;
    const details = document.createElement('details');
    details.className = 'tool-output';
    details.open = els.expandEnv.checked;
    details.appendChild(el('summary', result.is_error ? 'Environment output - error' : 'Environment output'));
    const content = result.content || result.output || '';
    details.appendChild(renderEnvironmentOutput(content));
    wrap.appendChild(details);
  }

  function renderEnvironmentOutput(content) {
    const text = outputText(content);
    const chunks = parseNewsChunks(text);
    if (!chunks.length) return pre(content);
    const list = document.createElement('div');
    list.className = 'news-results';
    for (const chunk of chunks) {
      const item = document.createElement('article');
      item.className = 'news-chunk';
      const header = document.createElement('header');
      header.appendChild(el('strong', chunk.headline || `Article ${chunk.index}`));
      const meta = [chunk.source, chunk.published].filter(Boolean).join(' - ');
      if (meta) header.appendChild(el('span', meta));
      if (chunk.url) {
        const link = document.createElement('a');
        link.href = chunk.url;
        link.target = '_blank';
        link.rel = 'noreferrer';
        link.textContent = 'source';
        header.appendChild(link);
      }
      item.appendChild(header);
      const body = document.createElement('details');
      body.className = 'news-body';
      body.appendChild(el('summary', 'Article chunk'));
      body.appendChild(el('p', chunk.body));
      item.appendChild(body);
      list.appendChild(item);
    }
    return list;
  }

  function outputText(content) {
    if (typeof content !== 'string') return preText(content);
    try {
      const parsed = JSON.parse(content);
      if (parsed && typeof parsed.result === 'string') return parsed.result;
    } catch (_) {}
    return content;
  }

  function parseNewsChunks(text) {
    if (!text.includes('HEADLINE:') || !text.includes('SOURCE:')) return [];
    const parts = text.split(/\n═+\s*\[(\d+)\]\s*═+\n/g);
    const chunks = [];
    for (let i = 1; i < parts.length; i += 2) {
      const index = parts[i];
      const raw = parts[i + 1] || '';
      const headline = lineValue(raw, 'HEADLINE');
      const source = lineValue(raw, 'SOURCE');
      const published = formatNewsDate((lineValue(raw, 'PUBLISHED') || '').split('|')[0].trim());
      const url = lineValue(raw, 'URL');
      const body = raw
        .replace(/^HEADLINE:.*$/m, '')
        .replace(/^SOURCE:.*$/m, '')
        .replace(/^PUBLISHED:.*$/m, '')
        .replace(/^URL:.*$/m, '')
        .trim();
      chunks.push({ index, headline, source, published, url, body });
    }
    return chunks;
  }

  function lineValue(text, key) {
    const match = text.match(new RegExp(`^${key}:\\s*(.*)$`, 'm'));
    return match ? match[1].trim() : '';
  }

  function formatNewsDate(value) {
    const date = value.slice(0, 10);
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) return value;
    return formatShortDate(date);
  }

  function pre(value) {
    const node = document.createElement('pre');
    node.textContent = preText(value);
    return node;
  }

  function preText(value) {
    return typeof value === 'string' ? value : JSON.stringify(value == null ? {} : value, null, 2);
  }

  function isBashTool(name) {
    const value = String(name || '').toLowerCase();
    return value === 'bash' || value === 'exec_command';
  }

  function isSubmitForecastTool(name) {
    return String(name || '').includes('submit_forecasts');
  }

  function isSearchNewsTool(name) {
    const value = String(name || '');
    return value.includes('search_news') || prettyToolName(value) === 'Search News';
  }

  function bashCommand(block) {
    return block.input && (block.input.command || block.input.cmd) ? String(block.input.command || block.input.cmd) : preText(block.input);
  }

  function isMarketCsvBashEvent(event) {
    const blocks = event && event.blocks ? event.blocks : [];
    const visibleBlocks = blocks.filter((block) => block.type !== 'tool_result');
    return visibleBlocks.length > 0 && visibleBlocks.every((block) => block.type === 'tool_use' && isBashTool(block.name) && bashCommand(block).includes('market.csv'));
  }

  function prettyToolName(name) {
    return String(name || 'tool')
      .replace(/^mcp__forecast__/, '')
      .replace(/_/g, ' ')
      .replace(/\b\w/g, (letter) => letter.toUpperCase());
  }

  function runOptionLabel(run) {
    return run.seed_label || 'run';
  }

  function toolKind(name) {
    const value = String(name || '');
    if (value.includes('submit_forecasts')) return 'forecast';
    if (value.includes('search_news')) return 'search';
    if (value.includes('next_day')) return 'advance';
    return 'tool';
  }

  function toolSubtitle(block) {
    const input = block.input || {};
    if (input.query) return input.query;
    if (input.question_id) return `question ${input.question_id}`;
    if (input.command) return input.command;
    return block.id || '';
  }

  function selectDay(date) {
    selectRunDay(state.runId, date);
  }

  function selectRunDay(runId, date) {
    const targetRun = filteredRuns().find((item) => item.run_id === runId);
    if (!targetRun || !targetRun.days.some((day) => day.date === date)) return;
    state.runId = targetRun.run_id;
    els.run.value = state.runId;
    state.day = date;
    state.workspaceFile = '';
    populateDays(date);
    renderTrajectory();
    loadSelection();
  }

  function showTooltip(tooltip, point, dayMeta, x, y, width, metric, run) {
    const actions = dayMeta ? dayMeta.event_count : 0;
    const forecasts = dayMeta ? dayMeta.forecast_count : 0;
    tooltip.replaceChildren();
    if (run) tooltip.appendChild(el('span', runOptionLabel(run)));
    tooltip.appendChild(el('strong', point.date));
    tooltip.appendChild(el('span', `${metricLabel(metric)}: ${formatMetric(point.value, metric)}`));
    tooltip.appendChild(el('span', `${actions} actions`));
    tooltip.appendChild(el('span', `${forecasts} forecasts`));
    tooltip.style.left = `${x / width * 100}%`;
    tooltip.style.top = `${y / 330 * 100}%`;
    tooltip.classList.toggle('is-right', x > width - 190);
    tooltip.classList.add('is-visible');
  }

  function hideTooltip(tooltip) {
    tooltip.classList.remove('is-visible');
  }

  function metricLabel(metric) {
    return metric === 'top1_accuracy' ? 'Top 1 accuracy' : 'Brier skill score';
  }

  function axisMetricLabel(metric) {
    return metric === 'top1_accuracy' ? 'Accuracy' : 'Skill score';
  }

  function formatMetric(value, metric) {
    return metric === 'top1_accuracy' ? `${value.toFixed(1)}%` : value.toFixed(3);
  }

  function formatProbability(value) {
    return `${(value * 100).toFixed(value >= 0.1 ? 0 : 1)}%`;
  }

  function formatDelta(value) {
    const points = value * 100;
    const sign = points > 0 ? '+' : '';
    return `${sign}${points.toFixed(Math.abs(points) >= 10 ? 0 : 1)}pp`;
  }

  function dayIndex(date) {
    const start = Date.UTC(2025, 11, 24);
    const current = Date.parse(`${date}T00:00:00Z`);
    return Math.round((current - start) / 86400000);
  }

  function dateFromDay(day) {
    const date = new Date(Date.UTC(2025, 11, 24 + day));
    return date.toISOString().slice(0, 10);
  }

  function formatShortDate(date) {
    return new Date(`${date}T00:00:00Z`).toLocaleDateString('en-US', { month: 'short', day: 'numeric', timeZone: 'UTC' });
  }

  function valueTicks(min, max, count) {
    if (count <= 1 || min === max) return [min];
    const ticks = [];
    for (let i = 0; i < count; i += 1) ticks.push(min + (max - min) * i / (count - 1));
    return ticks;
  }

  function dayTicks(min, max, count) {
    if (count <= 1 || min === max) return [min];
    const ticks = [];
    for (let i = 0; i < count; i += 1) ticks.push(Math.round(min + (max - min) * i / (count - 1)));
    return [...new Set(ticks)];
  }

  function svgEl(tag, attrs) {
    const node = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (const [key, value] of Object.entries(attrs || {})) node.setAttribute(key, value);
    return node;
  }

  function el(tag, text, className) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    node.textContent = text;
    return node;
  }

  if (document.querySelector('[data-trace-app]')) init();
})();
