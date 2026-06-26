(function () {
  const dataBase = (window.FSIM_TRACE_DATA_BASE || './data/').replace(/\/?$/, '/');
  const state = { manifest: null, agent: '', runId: '', day: '', metric: 'brier_skill_score', currentDays: new Map(), currentSummary: null, summaryRuns: new Set(), workspaceFile: '', loadedRunKey: '' };
  const chartColors = ['#0f766e', '#2563eb', '#b45309', '#9333ea', '#be123c', '#047857', '#4f46e5', '#a16207'];
  const workspaceCache = new Map();
  const summaryCache = new Map();
  let dayObserver = null;

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
    topButton: document.getElementById('trace-top-button'),
    status: document.getElementById('trace-status'),
    events: document.getElementById('trace-events'),
  };

  async function init() {
    try {
      const response = await fetch(dataBase + 'manifest.json', { cache: 'no-store' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      state.manifest = await response.json();
      state.summaryRuns = await loadSummaryIndex();
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
      state.currentDays = new Map();
      state.currentSummary = null;
      state.loadedRunKey = '';
      populateRuns();
      loadSelection();
    });
    els.run.addEventListener('change', () => {
      state.runId = els.run.value;
      state.workspaceFile = '';
      state.currentDays = new Map();
      state.currentSummary = null;
      state.loadedRunKey = '';
      populateDays();
      renderTrajectory();
      loadSelection();
    });
    els.day.addEventListener('change', () => {
      state.day = els.day.value;
      state.workspaceFile = '';
      scrollToDay(state.day);
    });
    if (els.dayList) {
      els.dayList.addEventListener('click', (event) => {
        const button = event.target.closest('.trace-day-button');
        if (!button || !els.dayList.contains(button)) return;
        event.preventDefault();
        selectDay(button.dataset.day);
      });
    }
    els.expandEnv.addEventListener('change', renderCurrentRun);
    if (els.topButton) {
      els.topButton.addEventListener('click', () => {
        instantScrollTo(0);
        requestAnimationFrame(() => instantScrollTo(0));
        setTimeout(() => instantScrollTo(0), 120);
      });
    }
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
    const preferredRun = state.manifest.runs.find(hasSummary) || state.manifest.runs[0];
    state.agent = preferredRun ? preferredRun.agent_slug : els.agent.value;
    els.agent.value = state.agent;
    populateRuns();
    const build = state.manifest.created_at_utc ? new Date(state.manifest.created_at_utc).toLocaleDateString() : '';
    els.buildMeta.textContent = `${state.manifest.runs.length} runs${build ? ` - built ${build}` : ''}`;
  }

  function populateRuns() {
    const runs = filteredRuns();
    fillSelect(els.run, runs.map((run) => ({
      value: run.run_id,
      label: `${runOptionLabel(run)}${hasSummary(run) ? ' · summary' : ''}`,
    })));
    const preferredRun = runs.find((run) => run.run_id === state.runId) || runs.find(hasSummary) || runs[0];
    state.runId = preferredRun ? preferredRun.run_id : els.run.value;
    els.run.value = state.runId;
    populateDays();
    renderTrajectory();
  }

  function populateDays(preferredDay) {
    const run = selectedRun();
    const days = sortedDays(run);
    fillSelect(els.day, days.map((day) => ({
      value: day.date,
      label: `${day.date} - ${day.tool_call_count || 0} tool calls`,
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

  async function loadSelection(options = {}) {
    const run = selectedRun();
    const days = sortedDays(run);
    if (!run || !days.length) {
      state.currentDays = new Map();
      state.currentSummary = null;
      state.loadedRunKey = '';
      state.workspaceFile = '';
      renderCurrentRun();
      return;
    }
    const runKey = `${run.agent_slug}/${run.run_id}`;
    state.loadedRunKey = runKey;
    state.currentDays = new Map();
    state.currentSummary = null;
    renderRunStats(run);
    renderToolList(run);
    renderDayRail();
    renderWorkspace(run);
    els.status.textContent = `Loading ${days.length} day summaries...`;
    els.events.replaceChildren();
    const summary = await loadRunSummary(run);
    if (state.loadedRunKey !== runKey) return;
    state.currentSummary = summary;

    let loaded = [];
    if (!summary) {
      els.status.textContent = `Loading ${days.length} day shards...`;
      loaded = await Promise.all(days.map(async (day) => {
        const response = await fetch(dataBase + day.path, { cache: 'no-store' });
        if (!response.ok) return { meta: day, error: `HTTP ${response.status}` };
        return { meta: day, payload: await response.json() };
      }));
      if (state.loadedRunKey !== runKey) return;
      for (const item of loaded) {
        if (item.payload) state.currentDays.set(item.meta.date, item.payload);
      }
    }

    renderCurrentRun();
    const targetDay = options.scrollTo || state.day || (days[0] && days[0].date);
    if (targetDay) requestAnimationFrame(() => scrollToDay(targetDay, { instant: options.instant || !options.scrollTo }));
    const failures = loaded.filter((item) => item.error);
    if (failures.length) {
      els.status.textContent = `Loaded ${state.currentDays.size}/${days.length} days. ${failures.length} day shard${failures.length === 1 ? '' : 's'} failed.`;
    }
  }

  function renderCurrentRun() {
    const run = selectedRun();
    renderRunStats(run);
    renderDayRail();
    renderWorkspace(run);
    els.events.replaceChildren();
    if (!run) {
      els.status.textContent = 'No trace run selected.';
      els.tools.replaceChildren();
      return;
    }

    const days = sortedDays(run);
    if (!days.length) {
      els.status.textContent = 'No trace days for this run.';
      els.tools.replaceChildren();
      return;
    }
    if (!state.currentDays.size && !state.currentSummary) {
      els.status.textContent = 'Loading run trace...';
      return;
    }

    for (const meta of days) {
      const day = state.currentDays.get(meta.date);
      const section = document.createElement('section');
      section.className = 'trace-day-section';
      section.id = `trace-day-${meta.date}`;
      section.dataset.day = meta.date;
      if (meta.date === state.day) section.classList.add('is-active');
      section.appendChild(renderDayHeader(meta, day));

      const summaryDay = state.currentSummary && state.currentSummary.dayMap.get(meta.date);
      if (!day && !summaryDay) {
        section.appendChild(el('div', `Could not load ${meta.path}.`, 'trace-empty'));
        els.events.appendChild(section);
        continue;
      }

      const resultById = day ? resultMap(day.events) : new Map();
      const visible = day ? visibleActionEvents(day.events) : [];
      if (summaryDay) section.appendChild(renderSummaryDay(summaryDay, visible, resultById, meta));
      else if (visible.length) section.appendChild(renderRawEventList(visible, resultById));
      else section.appendChild(el('div', 'No trace entries for this day.', 'trace-empty'));
      els.events.appendChild(section);
    }

    els.status.textContent = `${days.length} days loaded · ${state.currentSummary ? 'summarized view, raw trace loads on demand' : 'raw view, no summary for this run yet'}`;
    renderToolList(run);
    setActiveDay(state.day || days[0].date);
    setupDayObserver();
  }

  async function loadRunSummary(run) {
    const key = runKey(run);
    if (summaryCache.has(key)) return summaryCache.get(key);
    try {
      const response = await fetch(dataBase + `summaries/${run.agent_slug}__${run.run_id}.json`, { cache: 'no-store' });
      if (!response.ok) {
        summaryCache.set(key, null);
        return null;
      }
      const summary = await response.json();
      summary.dayMap = new Map((summary.days || []).map((day) => [day.date, day]));
      summaryCache.set(key, summary);
      return summary;
    } catch (_) {
      summaryCache.set(key, null);
      return null;
    }
  }

  async function loadSummaryIndex() {
    try {
      const response = await fetch(dataBase + 'summaries/index.json', { cache: 'no-store' });
      if (!response.ok) return new Set();
      const payload = await response.json();
      return new Set((payload.runs || []).map((run) => `${run.agent_slug}/${run.run_id}`));
    } catch (_) {
      return new Set();
    }
  }

  function runKey(run) {
    return `${run.agent_slug}/${run.run_id}`;
  }

  function hasSummary(run) {
    return state.summaryRuns.has(runKey(run));
  }

  async function loadDayTrace(meta) {
    if (state.currentDays.has(meta.date)) return state.currentDays.get(meta.date);
    const response = await fetch(dataBase + meta.path, { cache: 'no-store' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const payload = await response.json();
    state.currentDays.set(meta.date, payload);
    return payload;
  }

  function renderSummaryDay(daySummary, visibleEvents, resultById, meta) {
    const wrap = document.createElement('div');
    wrap.className = 'trace-summary-day';

    const overview = document.createElement('article');
    overview.className = 'trace-summary-overview';
    const title = String(daySummary.title || '').replace(/^20\d{2}-\d{2}-\d{2}:\s*/, '') || 'Day summary';
    overview.appendChild(el('h3', title));
    const stats = daySummary.stats || {};
    const benchmarkUpdates = Number(stats.benchmark_update_count || 0);
    const chips = [
      benchmarkUpdates ? `${benchmarkUpdates} scored qids` : '',
      benchmarkUpdates && hasMetricValue(stats.brier_update_delta) ? `Brier update ${formatSignedMetric(stats.brier_update_delta, 3)}` : '',
      benchmarkUpdates && hasMetricValue(stats.top1_update_delta) ? `Top 1 update ${formatSignedMetric(stats.top1_update_delta, 1)} pp` : '',
      stats.truncated ? 'summary truncated' : '',
    ].filter(Boolean);
    if (chips.length) overview.appendChild(renderSummaryChips(chips));
    wrap.appendChild(overview);

    const segments = daySummary.segments || [];
    for (const segment of segments) wrap.appendChild(renderSummarySegment(segment, visibleEvents, resultById, meta));
    if (!segments.length) {
      wrap.appendChild(renderRawDetails('Raw trace', visibleEvents, resultById, {
        count: Number(daySummary.stats && daySummary.stats.tool_call_count) || visibleEvents.length,
        loadEvents: () => loadRawEventsForDay(meta),
      }));
    }
    return wrap;
  }

  function renderSummarySegment(segment, visibleEvents, resultById, meta) {
    const bounds = segmentEventBounds(segment);
    const segmentEvents = visibleEvents.filter((event) => event.idx >= bounds.start && event.idx <= bounds.end);
    const card = document.createElement('article');
    card.className = 'trace-summary-segment';

    const header = document.createElement('div');
    header.className = 'trace-summary-segment-head';
    header.appendChild(el('h4', segment.label || 'Trace segment'));
    card.appendChild(header);

    const chips = [...(segment.notable_facts || []), ...(segment.tools || []).map(prettyToolName)].slice(0, 8);
    if (chips.length) card.appendChild(renderSummaryChips(chips));
    if ((segment.model_messages || []).length) card.appendChild(renderModelMessages(segment.model_messages));
    if ((segment.representative_forecasts || []).length) card.appendChild(renderRepresentativeForecasts(segment.representative_forecasts));
    card.appendChild(renderRawDetails('Raw trace', segmentEvents, resultById, {
      count: Number(segment.tool_call_count) || segmentEvents.length,
      loadEvents: () => loadRawEventsForSegment(meta, bounds),
    }));
    return card;
  }

  async function loadRawEventsForDay(meta) {
    const day = await loadDayTrace(meta);
    return {
      events: visibleActionEvents(day.events),
      resultById: resultMap(day.events),
    };
  }

  async function loadRawEventsForSegment(meta, bounds) {
    const raw = await loadRawEventsForDay(meta);
    return {
      events: raw.events.filter((event) => event.idx >= bounds.start && event.idx <= bounds.end),
      resultById: raw.resultById,
    };
  }

  function segmentEventBounds(segment) {
    const range = segment.event_range || {};
    const start = segment.event_idx_start != null ? segment.event_idx_start : (range.start_idx != null ? range.start_idx : range.start);
    const end = segment.event_idx_end != null ? segment.event_idx_end : (range.end_idx != null ? range.end_idx : range.end);
    return {
      start: start == null ? 0 : Number(start),
      end: end == null ? Infinity : Number(end),
    };
  }

  function renderSummaryChips(values) {
    const list = document.createElement('div');
    list.className = 'trace-summary-chips';
    for (const value of values) list.appendChild(el('span', value));
    return list;
  }

  function renderModelMessages(messages) {
    const wrap = document.createElement('div');
    wrap.className = 'trace-summary-messages';
    for (const message of messages) wrap.appendChild(el('p', message));
    return wrap;
  }

  function renderRepresentativeForecasts(forecasts) {
    const wrap = document.createElement('div');
    wrap.className = 'trace-summary-forecasts';
    for (const forecast of forecasts.slice(0, 3)) {
      const item = document.createElement('article');
      item.className = 'trace-summary-forecast';
      const question = forecast.question_title || `Question ${forecast.question_id || ''}`.trim();
      item.appendChild(el('h5', question || 'Forecast question'));
      const bars = renderVerticalForecastBars(forecast.outcomes || {}, forecast.previous_outcomes || {});
      if (bars) item.appendChild(bars);
      else if (forecast.summary) item.appendChild(el('p', forecast.summary));
      wrap.appendChild(item);
    }
    return wrap;
  }

  function renderVerticalForecastBars(outcomes, previous) {
    const rows = Object.entries(outcomes)
      .filter(([, value]) => Number.isFinite(Number(value)))
      .sort((a, b) => Number(b[1]) - Number(a[1]))
      .slice(0, 5);
    if (!rows.length) return null;
    const hasPrevious = Object.keys(previous || {}).length > 0;
    const chart = document.createElement('div');
    chart.className = 'forecast-mini-bars';
    for (const [name, value] of rows) {
      const prob = Number(value);
      const prior = Number(previous[name]);
      const bar = document.createElement('div');
      bar.className = 'forecast-mini-bar';
      const track = document.createElement('div');
      track.className = 'forecast-mini-track';
      const fill = document.createElement('i');
      fill.style.height = `${Math.max(0, Math.min(100, prob * 100))}%`;
      track.appendChild(fill);
      bar.appendChild(track);
      bar.appendChild(el('strong', formatProbability(prob)));
      bar.appendChild(el('span', name));
      if (Number.isFinite(prior)) bar.appendChild(el('em', formatDelta(prob - prior), prob - prior >= 0 ? 'is-up' : 'is-down'));
      else if (hasPrevious) bar.appendChild(el('em', 'new'));
      chart.appendChild(bar);
    }
    return chart;
  }

  function renderRawDetails(label, events, resultById, options = {}) {
    const details = document.createElement('details');
    details.className = 'trace-raw-details';
    details.appendChild(el('summary', label));
    details.addEventListener('toggle', async () => {
      if (!details.open || details.dataset.loaded) return;
      details.dataset.loaded = 'true';
      const loading = el('div', 'Loading raw trace...', 'trace-empty');
      details.appendChild(loading);
      try {
        const raw = options.loadEvents ? await options.loadEvents() : { events, resultById };
        loading.remove();
        if (raw.events.length) details.appendChild(renderRawEventList(raw.events, raw.resultById));
        else details.appendChild(el('div', 'No raw trace entries in this summary range.', 'trace-empty'));
      } catch (error) {
        loading.textContent = `Could not load raw trace (${error.message}).`;
      }
    });
    return details;
  }

  function resultMap(events) {
    const resultById = new Map();
    for (const event of events || []) {
      for (const block of event.blocks || []) {
        if (block.type === 'tool_result' && block.tool_use_id) resultById.set(block.tool_use_id, block);
      }
    }
    return resultById;
  }

  function renderDayHeader(meta, day) {
    const header = document.createElement('header');
    header.className = 'trace-day-header';
    const date = document.createElement('div');
    date.appendChild(el('span', 'Simulation day', 'trace-day-eyebrow'));
    date.appendChild(el('h2', formatShortDate(meta.date)));
    header.appendChild(date);
    const stats = document.createElement('div');
    stats.className = 'trace-day-header-stats';
    stats.appendChild(el('span', `${meta.tool_call_count || 0} tool calls`));
    stats.appendChild(el('span', `${meta.forecast_count || 0} forecasts`));
    header.appendChild(stats);
    return header;
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
          'aria-label': `${runOptionLabel(series.run)}, ${point.date}, ${metricLabel(state.metric)} ${formatMetric(point.value, state.metric)}, ${dayMeta ? dayMeta.tool_call_count : 0} tool calls`,
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

  function renderRunStats(run) {
    els.stats.replaceChildren();
    if (!run) return;
    const days = sortedDays(run);
    const totals = days.reduce((acc, day) => {
      acc.toolCalls += Number(day.tool_call_count) || 0;
      acc.forecasts += Number(day.forecast_count) || 0;
      acc.compactions += Number(day.compaction_count) || 0;
      return acc;
    }, { toolCalls: 0, forecasts: 0, compactions: 0 });
    const pairs = [
      ['model', run.agent_name || run.agent_slug],
      ['run', runOptionLabel(run)],
      ['days', days.length],
      ['tool calls', totals.toolCalls],
      ['forecast submits', totals.forecasts],
      ['recorded compactions', compactionCountLabel(Number(run.compaction_count) || totals.compactions)],
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
      const button = document.createElement('a');
      button.href = `#trace-day-${day.date}`;
      button.className = `trace-day-button${day.date === state.day ? ' is-active' : ''}`;
      button.dataset.day = day.date;
      button.title = `${formatShortDate(day.date)}\n${day.tool_call_count} tool calls\n${day.forecast_count} forecasts`;
      button.setAttribute('aria-pressed', String(day.date === state.day));
      button.appendChild(el('span', formatShortDate(day.date), 'trace-day-date'));
      button.appendChild(el('span', `${day.tool_call_count || 0} tool calls`, 'trace-day-meta'));
      button.addEventListener('click', (event) => {
        event.preventDefault();
        event.stopPropagation();
        selectDay(day.date);
      });
      els.dayList.appendChild(button);
    }
  }

  function renderToolList(run) {
    const counts = new Map(Object.entries((run && run.tool_counts) || {}));
    const compactions = Number(run && run.compaction_count) || 0;
    if (compactions) counts.set('__compactions__', compactions);
    els.tools.replaceChildren();
    for (const [name, count] of [...counts.entries()].sort((a, b) => b[1] - a[1])) {
      const row = document.createElement('div');
      row.className = 'trace-tool-row';
      row.appendChild(el('span', prettyToolName(name)));
      row.appendChild(el('strong', String(count)));
      els.tools.appendChild(row);
    }
    if (!compactions && run) {
      const row = document.createElement('div');
      row.className = 'trace-tool-row';
      row.appendChild(el('span', 'Context compactions'));
      row.appendChild(el('strong', 'not recorded'));
      els.tools.appendChild(row);
    }
    if (!counts.size && !run) els.tools.appendChild(el('div', 'No tool calls in this run.'));
  }

  function compactionCountLabel(count) {
    return count > 0 ? String(count) : 'not recorded';
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
        els.workspaceStatus.textContent = `${state.day} · no relevant files`;
        return;
      }
      const selected = files.find((file) => file.path === state.workspaceFile) || defaultWorkspaceFile(files, state.day);
      state.workspaceFile = selected ? selected.path : '';
      els.workspaceStatus.textContent = `${state.day} · ${files.length}/${workspace.files.length} files`;
      for (const file of files) {
        const button = document.createElement('button');
        button.type = 'button';
        button.className = `trace-workspace-file${file.path === state.workspaceFile ? ' is-active' : ''}`;
        button.title = `${file.label}${file.date ? `\n${file.date}` : ''}\n${formatBytes(file.size)}`;
        button.appendChild(el('strong', workspaceFileName(file.label)));
        button.appendChild(el('span', [file.kind, file.date ? `as of ${file.date}` : 'final file', fileSourceLabel(file), formatBytes(file.size)].filter(Boolean).join(' - ')));
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
    const exact = files.filter((file) => file.date === day);
    const cumulative = files.filter((file) => !file.date && file.kind === 'memory');
    const priorMemory = latestFilesBefore(files, day, 'memory');
    const priorPredictions = latestFilesBefore(files, day, 'predictions');
    const seen = new Set();
    return [...exact, ...priorMemory, ...priorPredictions, ...cumulative]
      .filter(Boolean)
      .filter((file) => {
        if (seen.has(file.label)) return false;
        seen.add(file.label);
        return true;
      })
      .sort((a, b) => workspaceFileRank(a, day) - workspaceFileRank(b, day) || a.label.localeCompare(b.label));
  }

  function latestFilesBefore(files, day, kind) {
    const latest = new Map();
    for (const file of files
      .filter((file) => file.kind === kind && file.date && file.date <= day)
      .sort((a, b) => b.date.localeCompare(a.date) || a.label.localeCompare(b.label))) {
      if (!latest.has(file.label)) latest.set(file.label, file);
    }
    return [...latest.values()];
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

  function fileSourceLabel(file) {
    if (file.source === 'trace_history') return 'trace';
    if (file.source === 'final_workspace') return 'workspace';
    return '';
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
    if (isNextDayTool(block.name)) return renderNextDayTool(block, result);

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
    const command = bashCommand(block);
    const details = document.createElement('details');
    details.className = 'tool-bash-details';
    details.open = Boolean(result && result.is_error);
    const summary = document.createElement('summary');
    summary.appendChild(el('strong', 'Bash'));
    summary.appendChild(el('code', command ? `$ ${command}` : '$'));
    details.appendChild(summary);
    const terminal = document.createElement('pre');
    terminal.className = 'tool-terminal';
    terminal.textContent = command ? `$ ${command}` : '$';
    details.appendChild(terminal);
    appendToolOutput(details, result);
    wrap.appendChild(details);
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

  function renderNextDayTool(block, result) {
    const wrap = document.createElement('section');
    wrap.className = `tool-call tool-call-next-day${result && result.is_error ? ' trace-error' : ''}`;
    const header = document.createElement('div');
    header.className = 'tool-call-header';
    const title = document.createElement('div');
    title.className = 'tool-call-title';
    title.appendChild(el('strong', 'Next Day'));
    header.appendChild(title);
    header.appendChild(el('span', 'advance', 'tool-pill'));
    wrap.appendChild(header);
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
    const nextDay = parseNextDayOutput(text);
    if (nextDay) return renderNextDayOutput(nextDay);
    const chunks = parseNewsChunks(text);
    if (!chunks.length) return pre(text);
    const list = document.createElement('div');
    list.className = 'news-results';
    for (const chunk of chunks) {
      const item = document.createElement('article');
      item.className = 'news-chunk';
      const header = document.createElement('header');
      const title = chunk.articleChunk ? `${chunk.headline || 'Article'} (chunk ${chunk.articleChunk})` : chunk.headline || `Article ${chunk.index}`;
      header.appendChild(el('strong', title));
      const meta = [chunk.source, chunk.published, chunk.duplicateCount > 1 ? `${chunk.duplicateCount} duplicate hits` : ''].filter(Boolean).join(' - ');
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
      body.appendChild(el('summary', chunk.articleChunk ? `Article chunk ${chunk.articleChunk}` : `Article result ${chunk.index}`));
      body.appendChild(el('p', chunk.body));
      item.appendChild(body);
      list.appendChild(item);
    }
    return list;
  }

  function outputText(content) {
    if (typeof content !== 'string') return preText(content);
    let text = content;
    const output = text.match(/(?:^|\n)Output:\s*([\s\S]*)$/);
    if (output) text = output[1].trim();
    try {
      const parsed = JSON.parse(text);
      if (parsed && typeof parsed.result === 'string') return parsed.result;
    } catch (_) {}
    return text;
  }

  function parseNextDayOutput(text) {
    if (!/^Day advanced to 20\d{2}-\d{2}-\d{2}\./.test(text)) return null;
    const lines = text.split('\n');
    const advanced = (lines[0].match(/Day advanced to (20\d{2}-\d{2}-\d{2})/) || [])[1] || '';
    const articles = (text.match(/([\d,]+) new articles/) || [])[1] || '';
    const active = (text.match(/(\d+) question\(s\) are still active\./) || [])[1] || '';
    const important = lines.find((line) => line.startsWith('**IMPORTANT**')) || '';
    const results = text.match(/## RESULTS SINCE YOUR LAST SESSION[^\n]*\n\n([\s\S]*?)(?=\n## YOUR CUMULATIVE PERFORMANCE|\n## |$)/);
    const performance = text.match(/## YOUR CUMULATIVE PERFORMANCE[^\n]*\n([\s\S]*)$/);
    return {
      advanced,
      articles,
      active,
      important: important.replace(/\*\*/g, ''),
      results: results ? parseResultBullets(results[1]) : [],
      performance: performance ? performance[1].trim() : '',
    };
  }

  function parseResultBullets(text) {
    return text.trim().split(/\n(?=- ")/).map((entry) => {
      const lines = entry.replace(/^- /, '').split('\n').map((line) => line.trim()).filter(Boolean);
      const question = (lines[0] || '').replace(/^"|"$/g, '');
      const distribution = (lines.find((line) => line.startsWith('Your prediction distribution:')) || '').replace('Your prediction distribution:', '').trim();
      const score = lines.find((line) => line.startsWith('Brier:')) || '';
      return { question, distribution, score };
    }).filter((item) => item.question);
  }

  function renderNextDayOutput(data) {
    const wrap = document.createElement('div');
    wrap.className = 'next-day-output';

    const summary = document.createElement('div');
    summary.className = 'next-day-summary';
    if (data.advanced) summary.appendChild(el('span', `Advanced to ${formatShortDate(data.advanced)}`));
    if (data.articles) summary.appendChild(el('span', `${data.articles} new articles`));
    if (data.active) summary.appendChild(el('span', `${data.active} active questions`));
    wrap.appendChild(summary);

    if (data.important) wrap.appendChild(el('div', data.important, 'next-day-warning'));

    if (data.results.length) {
      const section = document.createElement('section');
      section.className = 'next-day-section';
      section.appendChild(el('strong', 'Resolved since last session'));
      const list = document.createElement('div');
      list.className = 'next-day-results';
      for (const result of data.results) {
        const item = document.createElement('article');
        item.appendChild(el('p', result.question));
        if (result.distribution) item.appendChild(el('span', result.distribution));
        if (result.score) item.appendChild(el('em', result.score));
        list.appendChild(item);
      }
      section.appendChild(list);
      wrap.appendChild(section);
    }

    if (data.performance) {
      const details = document.createElement('details');
      details.className = 'next-day-performance';
      details.appendChild(el('summary', 'Cumulative performance'));
      details.appendChild(el('pre', data.performance));
      wrap.appendChild(details);
    }
    return wrap;
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
    const unique = [];
    const duplicates = new Map();
    const seen = new Map();
    for (const chunk of chunks) {
      const key = [normaliseArticleUrl(chunk.url), chunk.headline, chunk.body].join('\n');
      duplicates.set(key, (duplicates.get(key) || 0) + 1);
      if (!seen.has(key)) {
        seen.set(key, chunk);
        unique.push(chunk);
      }
    }

    const articleCounts = new Map();
    for (const chunk of unique) {
      const key = articleKey(chunk);
      articleCounts.set(key, (articleCounts.get(key) || 0) + 1);
    }
    const articleSeen = new Map();
    for (const chunk of unique) {
      const duplicateKey = [normaliseArticleUrl(chunk.url), chunk.headline, chunk.body].join('\n');
      chunk.duplicateCount = duplicates.get(duplicateKey) || 1;
      const key = articleKey(chunk);
      if (articleCounts.get(key) > 1) {
        const count = (articleSeen.get(key) || 0) + 1;
        articleSeen.set(key, count);
        chunk.articleChunk = count;
      }
    }
    return unique;
  }

  function normaliseArticleUrl(url) {
    return String(url || '').split(/[?#]/)[0].replace(/\/$/, '');
  }

  function articleKey(chunk) {
    return normaliseArticleUrl(chunk.url) || [chunk.source, chunk.headline].join('\n');
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

  function isNextDayTool(name) {
    return String(name || '').includes('next_day');
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
    if (name === '__compactions__') return 'Context compactions';
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
    selectRunDay(state.runId, date, { instant: true });
    jumpToLoadedDay(date);
  }

  function selectRunDay(runId, date, options = {}) {
    const targetRun = filteredRuns().find((item) => item.run_id === runId);
    if (!targetRun || !targetRun.days.some((day) => day.date === date)) return;
    const sameRun = targetRun.run_id === state.runId;
    state.runId = targetRun.run_id;
    els.run.value = state.runId;
    renderTrajectory();
    if (sameRun && state.loadedRunKey === `${state.agent}/${state.runId}` && state.currentDays.size) {
      scrollToDay(date, options);
      return;
    }
    state.day = date;
    state.workspaceFile = '';
    populateDays(date);
    loadSelection({ scrollTo: date, instant: options.instant });
  }

  function scrollToDay(date, options = {}) {
    if (options.instant && dayObserver) dayObserver.disconnect();
    setActiveDay(date, { scrollRail: true, instant: options.instant });
    const section = document.getElementById(`trace-day-${date}`);
    if (section) {
      if (options.instant) {
        jumpToSection(section);
        requestAnimationFrame(() => jumpToSection(section));
        setTimeout(() => jumpToSection(section), 120);
        setTimeout(() => {
          jumpToSection(section);
          setActiveDay(date, { scrollRail: true, instant: true });
          setupDayObserver();
        }, 500);
      } else {
        const top = section.getBoundingClientRect().top + window.pageYOffset - 10;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    }
  }

  function jumpToLoadedDay(date) {
    const section = document.getElementById(`trace-day-${date}`);
    if (!section) return;
    if (dayObserver) dayObserver.disconnect();
    setActiveDay(date, { scrollRail: true, instant: true });
    jumpToSection(section);
    requestAnimationFrame(() => jumpToSection(section));
    setTimeout(() => jumpToSection(section), 120);
    setTimeout(() => {
      jumpToSection(section);
      setActiveDay(date, { scrollRail: true, instant: true });
      setupDayObserver();
    }, 500);
  }

  function jumpToSection(section) {
    const top = section.getBoundingClientRect().top + window.pageYOffset - 10;
    instantScrollTo(top);
  }

  function instantScrollTo(top) {
    const previous = document.documentElement.style.scrollBehavior;
    document.documentElement.style.scrollBehavior = 'auto';
    window.scrollTo(0, top);
    document.documentElement.style.scrollBehavior = previous;
  }

  function setupDayObserver() {
    if (dayObserver) dayObserver.disconnect();
    const sections = [...els.events.querySelectorAll('.trace-day-section')];
    if (!sections.length || !('IntersectionObserver' in window)) return;
    dayObserver = new IntersectionObserver((entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (visible[0]) setActiveDay(visible[0].target.dataset.day, { scrollRail: true });
    }, { rootMargin: '-140px 0px -70% 0px', threshold: 0 });
    for (const section of sections) dayObserver.observe(section);
  }

  function setActiveDay(date, options = {}) {
    if (!date) return;
    const changed = date !== state.day;
    if (changed) {
      state.day = date;
      state.workspaceFile = '';
    }
    if (els.day) els.day.value = date;
    for (const button of els.dayList.querySelectorAll('.trace-day-button')) {
      const active = button.dataset.day === date;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
      if (active && options.scrollRail) {
        scrollDayRailToButton(button, options.instant);
      }
    }
    for (const section of els.events.querySelectorAll('.trace-day-section')) {
      section.classList.toggle('is-active', section.dataset.day === date);
    }
    if (changed) renderWorkspace(selectedRun());
  }

  function scrollDayRailToButton(button, instant) {
    const rail = els.dayList.parentElement;
    if (!rail) return;
    const left = button.offsetLeft - (rail.clientWidth - button.offsetWidth) / 2;
    const top = button.offsetTop - (rail.clientHeight - button.offsetHeight) / 2;
    rail.scrollTo({ left: Math.max(0, left), top: Math.max(0, top), behavior: instant ? 'auto' : 'smooth' });
  }

  function showTooltip(tooltip, point, dayMeta, x, y, width, metric, run) {
    const toolCalls = dayMeta ? dayMeta.tool_call_count : 0;
    const forecasts = dayMeta ? dayMeta.forecast_count : 0;
    tooltip.replaceChildren();
    if (run) tooltip.appendChild(el('span', runOptionLabel(run)));
    tooltip.appendChild(el('strong', point.date));
    tooltip.appendChild(el('span', `${metricLabel(metric)}: ${formatMetric(point.value, metric)}`));
    tooltip.appendChild(el('span', `${toolCalls} tool calls`));
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

  function formatSignedMetric(value, digits) {
    const number = Number(value);
    const sign = number > 0 ? '+' : '';
    return `${sign}${number.toFixed(digits)}`;
  }

  function hasMetricValue(value) {
    return value !== null && value !== '' && Number.isFinite(Number(value));
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
