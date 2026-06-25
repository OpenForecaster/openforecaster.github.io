(function () {
  const dataBase = (window.FSIM_TRACE_DATA_BASE || './data/').replace(/\/?$/, '/');
  const state = { manifest: null, agent: '', runId: '', day: '', metric: 'brier_skill_score', currentDay: null };
  const chartColors = ['#0f766e', '#2563eb', '#b45309', '#9333ea', '#be123c', '#047857', '#4f46e5', '#a16207'];

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
    summary: document.getElementById('trace-summary'),
    stats: document.getElementById('trace-day-stats'),
    tools: document.getElementById('trace-tool-list'),
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
      populateRuns();
      loadSelection();
    });
    els.run.addEventListener('change', () => {
      state.runId = els.run.value;
      populateDays();
      renderTrajectory();
      loadSelection();
    });
    els.day.addEventListener('change', () => {
      state.day = els.day.value;
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
    fillSelect(els.day, ((run && run.days) || []).map((day) => ({
      value: day.date,
      label: `${day.date} - ${day.event_count} actions`,
    })));
    if (preferredDay && run && run.days.some((day) => day.date === preferredDay)) els.day.value = preferredDay;
    state.day = els.day.value;
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

  async function loadSelection() {
    const run = selectedRun();
    const day = run && run.days.find((item) => item.date === state.day);
    if (!run || !day) {
      state.currentDay = null;
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
    renderCurrentDay();
  }

  function renderCurrentDay() {
    const run = selectedRun();
    const day = state.currentDay;
    renderSummary(run, day);
    els.events.replaceChildren();
    if (!run || !day) {
      els.status.textContent = 'No trace day selected.';
      els.stats.replaceChildren();
      els.tools.replaceChildren();
      return;
    }

    const resultById = new Map();
    for (const event of day.events) {
      for (const block of event.blocks || []) {
        if (block.type === 'tool_result' && block.tool_use_id) resultById.set(block.tool_use_id, block);
      }
    }

    const visible = day.events.filter((event) => shouldShowEvent(event));
    els.status.textContent = visible.length ? '' : 'No visible actions for this day.';
    for (let i = 0; i < visible.length; i += 1) {
      const event = visible[i];
      if (isOnlyToolResults(event)) continue;
      if (isMarketCsvBashEvent(event) && isMarketCsvBashEvent(visible[i + 1])) {
        const group = [];
        while (i < visible.length && isMarketCsvBashEvent(visible[i])) {
          group.push(visible[i]);
          i += 1;
        }
        i -= 1;
        els.events.appendChild(renderBashGroup(group, resultById));
        continue;
      }
      els.events.appendChild(renderEvent(event, resultById));
    }

    renderStats(day, visible);
    renderToolList(day);
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
    const margin = { top: 16, right: 24, bottom: 38, left: 58 };
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
      label.textContent = tick === 0 ? 'Day 0' : `Day ${tick}`;
      svg.appendChild(label);
    }
    svg.appendChild(svgEl('line', { x1: margin.left, x2: width - margin.right, y1: height - margin.bottom, y2: height - margin.bottom, class: 'trace-chart-axis' }));
    svg.appendChild(svgEl('line', { x1: margin.left, x2: margin.left, y1: margin.top, y2: height - margin.bottom, class: 'trace-chart-axis' }));

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

  function renderSummary(run, day) {
    els.summary.replaceChildren();
    if (!run) return;
    const title = document.createElement('div');
    title.className = 'trace-summary-title';
    title.appendChild(el('h2', run.agent_name || run.agent_slug));
    title.appendChild(el('p', [run.model, runOptionLabel(run)].filter(Boolean).join(' - ')));
    els.summary.appendChild(title);

    const dayMeta = run.days.find((item) => item.date === state.day);
    const stats = [
      ['Day', state.day || '-'],
      ['Actions', dayMeta ? dayMeta.event_count : countActions(day)],
      ['Tool calls', dayMeta ? dayMeta.tool_call_count : countToolCalls(day)],
      ['Forecasts', dayMeta ? dayMeta.forecast_count : countForecasts(day)],
    ];
    for (const [label, value] of stats) {
      const item = document.createElement('div');
      item.className = 'trace-stat';
      item.appendChild(el('strong', String(value)));
      item.appendChild(el('span', label));
      els.summary.appendChild(item);
    }
  }

  function renderStats(day, visible) {
    const pairs = [
      ['visible events', visible.length],
      ['model notes', day.events.filter((event) => event.kind === 'assistant' && (event.blocks || []).some((block) => block.type === 'text')).length],
      ['tool calls', countToolCalls(day)],
      ['forecast submits', countForecasts(day)],
      ['compactions', day.events.filter((event) => event.kind === 'compaction').length],
    ];
    els.stats.replaceChildren();
    for (const [label, value] of pairs) {
      els.stats.appendChild(el('dt', label));
      els.stats.appendChild(el('dd', String(value)));
    }
  }

  function renderToolList(day) {
    const counts = new Map();
    for (const event of day.events) {
      for (const block of event.blocks || []) {
        if (block.type === 'tool_use') counts.set(block.name, (counts.get(block.name) || 0) + 1);
      }
    }
    els.tools.replaceChildren();
    for (const [name, count] of [...counts.entries()].sort((a, b) => b[1] - a[1])) {
      const row = document.createElement('div');
      row.className = 'trace-tool-row';
      row.appendChild(el('span', prettyToolName(name)));
      row.appendChild(el('strong', String(count)));
      els.tools.appendChild(row);
    }
    if (!counts.size) els.tools.appendChild(el('div', 'No tool calls on this day.'));
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
    details.appendChild(pre(result.content || result.output || ''));
    wrap.appendChild(details);
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
    const bits = [run.run_label || run.run_id];
    if (run.seed_label && run.seed_label !== run.run_id && !String(run.seed_label).startsWith(run.run_id + ' ')) {
      bits.push(run.seed_label);
    } else if (run.seed_label && String(run.seed_label).startsWith(run.run_id + ' ')) {
      bits.push(String(run.seed_label).slice(run.run_id.length + 1));
    }
    return bits.filter(Boolean).join(' - ');
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
    const run = selectedRun();
    const targetRun = filteredRuns().find((item) => item.run_id === runId);
    if (!targetRun || !targetRun.days.some((day) => day.date === date)) return;
    state.runId = targetRun.run_id;
    els.run.value = state.runId;
    state.day = date;
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

  function countToolCalls(day) {
    if (!day) return 0;
    return day.events.reduce((total, event) => total + (event.blocks || []).filter((block) => block.type === 'tool_use').length, 0);
  }

  function countActions(day) {
    if (!day) return 0;
    return day.events.filter((event) => shouldShowEvent(event)).length;
  }

  function countForecasts(day) {
    if (!day) return 0;
    return day.events.reduce((total, event) => total + (event.blocks || []).filter((block) => block.type === 'tool_use' && String(block.name).includes('submit_forecasts')).length, 0);
  }

  function el(tag, text, className) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    node.textContent = text;
    return node;
  }

  if (document.querySelector('[data-trace-app]')) init();
})();
