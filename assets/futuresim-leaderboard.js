/* Interactive FutureSim leaderboard chart.
 *
 * Reads futuresim/data/q1_results.json and q2_results.json (built by
 * scripts/build_futuresim_q1_chart_data.py and build_futuresim_q2_chart_data.py)
 * and draws one SVG line chart with a period switch, a metric switch, a
 * hover/touch/keyboard crosshair that reads every model's score for a day, a
 * legend that shows or hides models, and a table view. A period whose data
 * cannot be loaded shows its static PNG figure instead.
 */
(function () {
  'use strict';

  const root = document.querySelector('[data-futuresim-q2-results]');
  if (!root) return;
  const host = root.querySelector('[data-futuresim-chart]');
  if (!host) return;
  const metricButtons = Array.from(root.querySelectorAll('[data-futuresim-metric]'));
  const periodButtons = Array.from(root.querySelectorAll('[data-futuresim-period]'));
  const tableHost = root.querySelector('[data-futuresim-table]');
  const downloadLink = root.querySelector('[data-futuresim-download]');

  const SVG_NS = 'http://www.w3.org/2000/svg';
  const LOGOS = { openai: 'openai.svg', anthropic: 'anthropic.svg', deepseek: 'deepseek.svg', zhipu: 'zhipu.png', qwen: 'qwen.svg' };
  const minus = (text) => text.replace('-', '−');
  const fixed = (value, digits) => minus((Math.abs(value) < 0.5 * Math.pow(10, -digits) ? 0 : value).toFixed(digits));

  const METRICS = {
    top1: {
      key: 'accuracy',
      title: 'Top-1 accuracy',
      axis: 'Accuracy (%)',
      value: (v) => fixed(v, 1) + '%',
      spread: (v) => '±' + v.toFixed(1),
      end: (v) => fixed(v, 0) + '%',
      includeZero: false,
      floor: 0,
    },
    brier: {
      key: 'brier',
      title: 'Brier skill score',
      axis: 'Brier Skill Score (↑)',
      value: (v) => fixed(v, 3),
      spread: (v) => '±' + v.toFixed(3),
      end: (v) => fixed(v, 2),
      includeZero: true,
      floor: -Infinity,
    },
  };

  const dayFormat = new Intl.DateTimeFormat('en-US', { month: 'short', day: 'numeric', timeZone: 'UTC' });
  const fullDayFormat = new Intl.DateTimeFormat('en-US', {
    weekday: 'short',
    month: 'short',
    day: 'numeric',
    year: 'numeric',
    timeZone: 'UTC',
  });

  function svg(name, attrs, parent) {
    const node = document.createElementNS(SVG_NS, name);
    for (const key in attrs) node.setAttribute(key, attrs[key]);
    if (parent) parent.appendChild(node);
    return node;
  }

  function html(tag, className, text, parent) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    if (parent) parent.appendChild(node);
    return node;
  }

  function niceStep(raw) {
    const power = Math.pow(10, Math.floor(Math.log10(raw)));
    const fraction = raw / power;
    return (fraction < 1.5 ? 1 : fraction < 3.5 ? 2 : fraction < 7.5 ? 5 : 10) * power;
  }

  /* Place labels at their targets, pushed apart by `gap` where they would
   * overlap. Each overlapping run stays centred on the mean of its targets. */
  function spreadLabels(targets, gap, lo, hi) {
    const blocks = [];
    const centre = (block) => {
      const half = ((block.n - 1) * gap) / 2;
      return Math.min(Math.max(block.sum / block.n, lo + half), Math.max(lo + half, hi - half));
    };
    for (const target of targets) {
      blocks.push({ n: 1, sum: target });
      while (blocks.length > 1) {
        const lower = blocks[blocks.length - 1];
        const upper = blocks[blocks.length - 2];
        const upperEnd = centre(upper) + ((upper.n - 1) * gap) / 2;
        const lowerStart = centre(lower) - ((lower.n - 1) * gap) / 2;
        if (lowerStart - upperEnd >= gap) break;
        upper.n += lower.n;
        upper.sum += lower.sum;
        blocks.pop();
      }
    }
    const out = [];
    for (const block of blocks) {
      const start = centre(block) - ((block.n - 1) * gap) / 2;
      for (let k = 0; k < block.n; k += 1) out.push(start + k * gap);
    }
    return out;
  }

  /* One entry per period button: where its scores live, which static figures stand in
   * for them, and which models the reader has hidden there. */
  const periods = new Map(
    periodButtons.map((button) => [
      button.dataset.futuresimPeriod,
      {
        id: button.dataset.futuresimPeriod,
        label: button.textContent.trim(),
        src: button.dataset.src,
        fallback: { top1: button.dataset.fallbackTop1, brier: button.dataset.fallbackBrier },
        hidden: new Set(),
        request: null,
      },
    ])
  );
  const pressed =
    periodButtons.find((button) => button.getAttribute('aria-pressed') === 'true') || periodButtons[periodButtons.length - 1];
  if (!pressed) return;
  /* What the reader has chosen; it carries over when the period changes. */
  const selection = { period: pressed.dataset.futuresimPeriod, metric: 'top1', bands: true };
  /* The chart or static figure currently in the host: { setMetric, destroy }. */
  let view = null;

  /* Static figure for a period whose scores could not be loaded. */
  function fallbackView(period) {
    host.textContent = '';
    host.classList.remove('is-ready', 'is-compact');
    host.classList.add('is-fallback');
    if (tableHost) tableHost.hidden = true;
    const image = html('img', '', null, host);
    const setMetric = (metric) => {
      image.src = period.fallback[metric];
      image.alt = METRICS[metric].title + ' trajectories for agents evaluated on FutureSim ' + period.label + '.';
    };
    setMetric(selection.metric);
    return { setMetric, destroy: () => host.classList.remove('is-fallback') };
  }

  function chartView(data, period) {
    const dates = data.dates.map((value) => new Date(value + 'T00:00:00Z'));
    const count = dates.length;
    const models = data.models;
    const logoBase = host.dataset.logos || '';
    const state = {
      metric: selection.metric,
      hidden: period.hidden,
      emphasis: null,
      index: null,
      pointerY: null,
      bands: selection.bands,
    };
    let geometry = null;

    host.textContent = '';
    host.classList.add('is-ready');

    /* ---- toolbar: legend + band toggle ---- */
    const toolbar = html('div', 'fsim-toolbar', null, host);
    const legend = html('ul', 'fsim-legend', null, toolbar);
    legend.setAttribute('aria-label', 'Models. Select one to show or hide it.');
    const legendButtons = new Map();
    for (const model of models) {
      const item = html('li', '', null, legend);
      const button = html('button', '', null, item);
      button.type = 'button';
      button.setAttribute('aria-pressed', String(!state.hidden.has(model.id)));
      const key = html('span', 'fsim-key', null, button);
      key.style.setProperty('--series', model.color);
      html('span', '', model.name, button);
      button.addEventListener('click', () => toggleModel(model.id));
      button.addEventListener('pointerenter', () => setEmphasis(model.id));
      button.addEventListener('pointerleave', () => setEmphasis(null));
      button.addEventListener('focus', () => setEmphasis(model.id));
      button.addEventListener('blur', () => setEmphasis(null));
      legendButtons.set(model.id, button);
    }
    const bandLabel = html('label', 'fsim-band-toggle', null, toolbar);
    const bandInput = html('input', '', null, bandLabel);
    bandInput.type = 'checkbox';
    bandInput.checked = state.bands;
    html('span', '', '±1 std bands', bandLabel);
    bandInput.addEventListener('change', () => {
      selection.bands = state.bands = bandInput.checked;
      render();
    });

    /* ---- plot ---- */
    const plot = html('div', 'fsim-plot', null, host);
    plot.tabIndex = 0;
    plot.setAttribute('role', 'group');
    plot.setAttribute('aria-label', 'Daily scores. Use the left and right arrow keys to step through days.');
    const chart = svg('svg', { role: 'img' }, plot);
    const tooltip = html('div', 'fsim-tooltip', null, plot);
    tooltip.hidden = true;
    tooltip.setAttribute('aria-hidden', 'true');
    const live = html('p', 'fsim-visually-hidden', null, host);
    live.setAttribute('aria-live', 'polite');
    html(
      'p',
      'fsim-note',
      'Hover or tap the chart to read every model on a given day. Select a model name to hide or show it. ' +
        'Lines are means over seeds; bands are ±1 standard deviation from a bootstrap over questions and seeds.',
      host
    );

    const visibleModels = () => models.filter((model) => !state.hidden.has(model.id));

    function toggleModel(id) {
      if (state.hidden.has(id)) state.hidden.delete(id);
      else if (visibleModels().length > 1) state.hidden.add(id);
      if (state.hidden.has(id) && state.emphasis === id) state.emphasis = null;
      for (const [modelId, button] of legendButtons) {
        button.setAttribute('aria-pressed', String(!state.hidden.has(modelId)));
      }
      render();
    }

    function setEmphasis(id) {
      const next = id && !state.hidden.has(id) ? id : null;
      if (next === state.emphasis) return;
      state.emphasis = next;
      applyEmphasis();
      updateHover();
    }

    function applyEmphasis() {
      chart.querySelectorAll('[data-series]').forEach((node) => {
        const id = node.getAttribute('data-series');
        node.classList.toggle('is-dimmed', state.emphasis !== null && id !== state.emphasis);
        node.classList.toggle('is-emphasized', id === state.emphasis);
      });
    }

    function render() {
      const metric = METRICS[state.metric];
      const visible = visibleModels();
      const width = Math.max(280, Math.round(plot.clientWidth));
      const compact = width < 560;
      const height = compact ? 360 : Math.round(Math.min(540, Math.max(440, width * 0.56)));
      const badge = compact ? 11 : 16;
      host.classList.toggle('is-compact', compact);

      let lo = Infinity;
      let hi = -Infinity;
      for (const model of visible) {
        const series = model[metric.key];
        for (let i = 0; i < count; i += 1) {
          const spread = state.bands ? series.std[i] : 0;
          lo = Math.min(lo, series.mean[i] - spread);
          hi = Math.max(hi, series.mean[i] + spread);
        }
      }
      if (metric.includeZero) {
        lo = Math.min(lo, 0);
        hi = Math.max(hi, 0);
      }
      const pad = (hi - lo || 1) * 0.06;
      lo = Math.max(metric.floor, lo - pad);
      hi += pad;

      const step = niceStep((hi - lo) / (compact ? 4 : 5));
      const digits = Math.max(0, -Math.floor(Math.log10(step) + 1e-9));
      const ticks = [];
      for (let tick = Math.ceil(lo / step - 1e-9) * step; tick <= hi + 1e-9; tick += step) ticks.push(tick);

      chart.textContent = '';
      /* Margins hold the axis title, the tick labels and the badge + final-value labels, so they track
       * the font sizes in blog.css. The left one follows the widest y tick label, which keeps the axis
       * title the same distance from the numbers for every metric. */
      const tickTextWidth = (text) => {
        const probe = svg('text', { class: 'fsim-tick' }, chart);
        probe.textContent = text;
        const measured = probe.getComputedTextLength() || text.length * (compact ? 9 : 12);
        chart.removeChild(probe);
        return measured;
      };
      const tickWidth = Math.max(...ticks.map((tick) => tickTextWidth(fixed(tick, digits))));
      const tickGap = compact ? 7 : 10;
      const titleX = compact ? 9 : 13; /* half the line box of .fsim-axis-title */
      const margin = {
        top: compact ? 16 : 20,
        right: compact ? 86 : 128,
        bottom: compact ? 36 : 48,
        left: Math.ceil(titleX * 2 + (compact ? 6 : 12) + tickWidth + tickGap),
      };
      const plotWidth = width - margin.left - margin.right;
      const plotHeight = height - margin.top - margin.bottom;
      const x = (index) => margin.left + (count === 1 ? 0 : (index / (count - 1)) * plotWidth);
      const y = (value) => margin.top + (1 - (value - lo) / (hi - lo)) * plotHeight;
      geometry = { width, height, margin, plotWidth, x, y, compact };

      chart.setAttribute('viewBox', '0 0 ' + width + ' ' + height);
      chart.setAttribute('width', width);
      chart.setAttribute('height', height);
      chart.setAttribute(
        'aria-label',
        metric.title +
          ' by simulation day, ' +
          fullDayFormat.format(dates[0]) +
          ' to ' +
          fullDayFormat.format(dates[count - 1]) +
          '. Final values: ' +
          visible.map((model) => model.name + ' ' + metric.value(model[metric.key].mean[count - 1])).join(', ') +
          '.'
      );

      /* grid + axes */
      const grid = svg('g', { class: 'fsim-grid' }, chart);
      for (const tick of ticks) {
        const ty = y(tick);
        const isZero = Math.abs(tick) < step / 1e6;
        svg(
          'line',
          {
            x1: margin.left,
            x2: margin.left + plotWidth,
            y1: ty,
            y2: ty,
            class: isZero && metric.includeZero ? 'fsim-zero' : '',
          },
          grid
        );
        const label = svg('text', { x: margin.left - tickGap, y: ty, class: 'fsim-tick fsim-tick-y' }, grid);
        label.textContent = fixed(tick, digits);
      }
      /* y-axis title: reads bottom to top along the axis, centred on the plot area */
      const titleY = margin.top + plotHeight / 2;
      const axisTitle = svg(
        'text',
        { x: titleX, y: titleY, transform: 'rotate(-90 ' + titleX + ' ' + titleY + ')', class: 'fsim-axis-title' },
        grid
      );
      axisTitle.textContent = metric.axis;

      /* Both ends and every month start, working back from the last day: a label that
       * would crowd the one to its right is dropped. */
      const tickIndexes = [];
      dates.forEach((date, index) => {
        if (index === 0 || index === count - 1 || date.getUTCDate() === 1) tickIndexes.push(index);
      });
      const lastX = x(count - 1);
      const xTicks = [];
      let leftEdge = Infinity;
      for (let k = tickIndexes.length - 1; k >= 0; k -= 1) {
        const index = tickIndexes[k];
        const half = tickTextWidth(dayFormat.format(dates[index])) / 2;
        if (x(index) + half <= leftEdge - (compact ? 8 : 16)) {
          xTicks.unshift(index);
          leftEdge = x(index) - half;
        }
      }
      for (const index of xTicks) {
        svg('line', { x1: x(index), x2: x(index), y1: margin.top + plotHeight, y2: margin.top + plotHeight + 6, class: 'fsim-tickmark' }, grid);
        const label = svg('text', { x: x(index), y: margin.top + plotHeight + (compact ? 24 : 31), class: 'fsim-tick fsim-tick-x' }, grid);
        label.textContent = dayFormat.format(dates[index]);
      }
      svg('line', { x1: margin.left, x2: margin.left + plotWidth, y1: margin.top + plotHeight, y2: margin.top + plotHeight, class: 'fsim-baseline' }, grid);

      /* bands under every line, then lines */
      const point = (index, value) => x(index).toFixed(2) + ' ' + y(value).toFixed(2);
      if (state.bands) {
        const bands = svg('g', { class: 'fsim-bands' }, chart);
        for (const model of visible) {
          const series = model[metric.key];
          let path = '';
          for (let i = 0; i < count; i += 1) path += (i ? 'L' : 'M') + point(i, series.mean[i] + series.std[i]);
          for (let i = count - 1; i >= 0; i -= 1) path += 'L' + point(i, series.mean[i] - series.std[i]);
          svg('path', { d: path + 'Z', fill: model.color, 'data-series': model.id }, bands);
        }
      }
      const lines = svg('g', { class: 'fsim-lines' }, chart);
      for (const model of visible) {
        const series = model[metric.key];
        let path = '';
        for (let i = 0; i < count; i += 1) path += (i ? 'L' : 'M') + point(i, series.mean[i]);
        svg('path', { d: path, stroke: model.color, 'data-series': model.id }, lines);
      }

      /* end labels: vendor badge + final value, spread apart where lines converge */
      const ends = visible
        .map((model) => ({ model, value: model[metric.key].mean[count - 1] }))
        .sort((a, b) => b.value - a.value);
      const labelY = spreadLabels(
        ends.map((end) => y(end.value)),
        badge * 2 + 3,
        margin.top + badge - 6,
        margin.top + plotHeight - badge + 6
      );
      const endLayer = svg('g', { class: 'fsim-ends' }, chart);
      const badgeX = lastX + (compact ? 21 : 33);
      ends.forEach((end, order) => {
        const group = svg('g', { class: 'fsim-end', 'data-series': end.model.id }, endLayer);
        const endY = y(end.value);
        svg('path', { d: 'M' + lastX + ' ' + endY + 'L' + (badgeX - badge) + ' ' + labelY[order], stroke: end.model.color, class: 'fsim-leader' }, group);
        svg('circle', { cx: lastX, cy: endY, r: compact ? 4 : 5, fill: end.model.color }, group);
        svg('circle', { cx: badgeX, cy: labelY[order], r: badge, stroke: end.model.color, class: 'fsim-badge' }, group);
        const logo = LOGOS[end.model.vendor];
        if (logo) {
          const size = badge * 1.24;
          svg('image', { href: logoBase + logo, x: badgeX - size / 2, y: labelY[order] - size / 2, width: size, height: size }, group);
        }
        const value = svg(
          'text',
          { x: badgeX + badge + (compact ? 6 : 8), y: labelY[order], fill: end.model.color, class: 'fsim-end-value' },
          group
        );
        value.textContent = metric.end(end.value);
        const title = svg('title', {}, group);
        title.textContent = end.model.name + ': ' + metric.value(end.value) + ' on ' + dayFormat.format(dates[count - 1]);
        group.addEventListener('pointerenter', () => setEmphasis(end.model.id));
        group.addEventListener('pointerleave', () => setEmphasis(null));
      });

      /* hover layer */
      const hover = svg('g', { class: 'fsim-hover' }, chart);
      svg('line', { class: 'fsim-crosshair', y1: margin.top, y2: margin.top + plotHeight }, hover);
      for (const model of visible) {
        svg('circle', { r: compact ? 5.5 : 6.5, fill: model.color, 'data-dot': model.id }, hover);
      }

      applyEmphasis();
      updateHover();
      renderTable();
    }

    function updateHover() {
      if (!geometry) return;
      const hover = chart.querySelector('.fsim-hover');
      if (!hover) return;
      const index = state.index;
      if (index === null) {
        hover.style.display = 'none';
        tooltip.hidden = true;
        return;
      }
      const metric = METRICS[state.metric];
      const visible = visibleModels();
      const cx = geometry.x(index);
      hover.style.display = '';
      const crosshair = hover.querySelector('.fsim-crosshair');
      crosshair.setAttribute('x1', cx);
      crosshair.setAttribute('x2', cx);
      for (const model of visible) {
        const dot = hover.querySelector('[data-dot="' + model.id + '"]');
        if (!dot) continue;
        dot.setAttribute('cx', cx);
        dot.setAttribute('cy', geometry.y(model[metric.key].mean[index]));
        dot.classList.toggle('is-dimmed', state.emphasis !== null && model.id !== state.emphasis);
      }

      tooltip.textContent = '';
      const head = html('div', 'fsim-tooltip-head', null, tooltip);
      html('div', 'fsim-tooltip-date', fullDayFormat.format(dates[index]), head);
      html('div', 'fsim-tooltip-metric', metric.title, head);
      const rows = html('div', 'fsim-tooltip-rows', null, tooltip);
      const ranked = visible.slice().sort((a, b) => b[metric.key].mean[index] - a[metric.key].mean[index]);
      for (const model of ranked) {
        const series = model[metric.key];
        const row = html('div', 'fsim-tooltip-row' + (model.id === state.emphasis ? ' is-emphasized' : ''), null, rows);
        const key = html('span', 'fsim-key', null, row);
        key.style.setProperty('--series', model.color);
        html('span', 'fsim-tooltip-name', model.name, row);
        html('span', 'fsim-tooltip-value', metric.value(series.mean[index]), row);
        html('span', 'fsim-tooltip-spread', metric.spread(series.std[index]), row);
      }
      tooltip.hidden = false;
      if (geometry.compact) {
        /* Narrow screens: the readout docks under the plot instead of covering it,
         * and stays put once opened so nothing below the chart jumps on the next tap. */
        tooltip.style.left = '';
        tooltip.style.top = '';
        return;
      }
      const boxWidth = tooltip.offsetWidth;
      const boxHeight = tooltip.offsetHeight;
      let left = cx + 14;
      if (left + boxWidth > geometry.width - 4) left = cx - 14 - boxWidth;
      left = Math.max(4, Math.min(left, geometry.width - boxWidth - 4));
      const anchorY = state.pointerY === null ? geometry.margin.top + boxHeight / 2 + 6 : state.pointerY;
      const top = Math.max(4, Math.min(anchorY - boxHeight / 2, geometry.height - boxHeight - 4));
      tooltip.style.left = left + 'px';
      tooltip.style.top = top + 'px';
    }

    function setIndex(index, pointerY) {
      state.index = index === null ? null : Math.max(0, Math.min(count - 1, index));
      state.pointerY = pointerY == null ? null : pointerY;
      updateHover();
    }

    function indexFromEvent(event) {
      const box = chart.getBoundingClientRect();
      const px = event.clientX - box.left;
      const index = Math.round(((px - geometry.margin.left) / geometry.plotWidth) * (count - 1));
      return { index, y: event.clientY - box.top };
    }

    chart.addEventListener('pointermove', (event) => {
      if (!geometry) return;
      const at = indexFromEvent(event);
      setIndex(at.index, at.y);
    });
    chart.addEventListener('pointerdown', (event) => {
      if (!geometry) return;
      const at = indexFromEvent(event);
      setIndex(at.index, at.y);
    });
    chart.addEventListener('pointerleave', (event) => {
      if (event.pointerType === 'mouse') setIndex(null);
    });
    const docked = () => Boolean(geometry && geometry.compact);
    const onDocumentPointerDown = (event) => {
      if (state.index !== null && !docked() && !plot.contains(event.target)) setIndex(null);
    };
    document.addEventListener('pointerdown', onDocumentPointerDown);

    plot.addEventListener('keydown', (event) => {
      const jump = event.shiftKey ? 7 : 1;
      const current = state.index === null ? count - 1 : state.index;
      let next = null;
      if (event.key === 'ArrowLeft') next = current - jump;
      else if (event.key === 'ArrowRight') next = state.index === null ? current : current + jump;
      else if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = count - 1;
      else if (event.key === 'Escape') {
        setIndex(null);
        return;
      } else return;
      event.preventDefault();
      setIndex(next, null);
      const metric = METRICS[state.metric];
      live.textContent =
        fullDayFormat.format(dates[state.index]) +
        ': ' +
        visibleModels()
          .map((model) => model.name + ' ' + metric.value(model[metric.key].mean[state.index]))
          .join(', ');
    });
    plot.addEventListener('blur', () => {
      if (!docked()) setIndex(null);
    });

    /* ---- table view ---- */
    function renderTable() {
      if (!tableHost) return;
      const metric = METRICS[state.metric];
      const body = tableHost.querySelector('[data-futuresim-table-body]');
      if (!body) return;
      const columns = [];
      dates.forEach((date, index) => {
        const day = date.getUTCDate();
        if (index === 0 || day === 1 || day === 15) columns.push(index);
      });
      if (columns[columns.length - 1] !== count - 1) columns.push(count - 1);

      body.textContent = '';
      /* The caption sits outside the scroller so it wraps on narrow screens instead of
       * running off with the table. */
      const caption = html('p', 'fsim-table-caption', metric.title + ' on selected days (mean over seeds; final day ±1 std)', body);
      caption.id = 'fsim-table-caption';
      const scroller = html('div', 'fsim-table-scroll', null, body);
      scroller.tabIndex = 0;
      scroller.setAttribute('role', 'region');
      scroller.setAttribute('aria-labelledby', caption.id);
      const table = html('table', 'fsim-table', null, scroller);
      table.setAttribute('aria-labelledby', caption.id);
      const headRow = html('tr', '', null, html('thead', '', null, table));
      html('th', '', 'Model', headRow).scope = 'col';
      for (const index of columns) html('th', '', dayFormat.format(dates[index]), headRow).scope = 'col';
      const tbody = html('tbody', '', null, table);
      const ranked = models.slice().sort((a, b) => b[metric.key].mean[count - 1] - a[metric.key].mean[count - 1]);
      for (const model of ranked) {
        const series = model[metric.key];
        const row = html('tr', '', null, tbody);
        const name = html('th', '', null, row);
        name.scope = 'row';
        const key = html('span', 'fsim-key', null, name);
        key.style.setProperty('--series', model.color);
        html('span', '', model.name, name);
        html('span', 'fsim-table-sub', model.harness + ' \u00b7 ' + model.seeds + ' seeds', name);
        columns.forEach((index, position) => {
          const last = position === columns.length - 1;
          const cell = html('td', last ? 'fsim-table-final' : '', metric.value(series.mean[index]), row);
          if (last) html('span', 'fsim-table-spread', ' ' + metric.spread(series.std[index]), cell);
        });
      }
      tableHost.hidden = false;
    }

    /* ---- resize ---- */
    let lastWidth = 0;
    const onResize = () => {
      const width = Math.round(plot.clientWidth);
      if (width === lastWidth) return;
      lastWidth = width;
      render();
    };
    const observer = typeof ResizeObserver === 'function' ? new ResizeObserver(onResize) : null;
    if (observer) observer.observe(plot);
    else window.addEventListener('resize', onResize);
    onResize();

    return {
      setMetric(metric) {
        state.metric = metric;
        render();
      },
      destroy() {
        if (observer) observer.disconnect();
        else window.removeEventListener('resize', onResize);
        document.removeEventListener('pointerdown', onDocumentPointerDown);
        host.classList.remove('is-ready', 'is-compact');
      },
    };
  }

  /* ---- period + metric switches ---- */
  function load(period) {
    if (!period.request) {
      period.request = fetch(period.src).then((response) => {
        if (!response.ok) throw new Error('HTTP ' + response.status);
        return response.json();
      });
      /* A failed download is retried the next time the period is chosen. */
      period.request.catch(() => {
        period.request = null;
      });
    }
    return period.request;
  }

  function show(make) {
    if (view) view.destroy();
    view = null;
    view = make();
  }

  function selectPeriod(id) {
    const period = periods.get(id);
    selection.period = id;
    for (const button of periodButtons) {
      button.setAttribute('aria-pressed', String(button.dataset.futuresimPeriod === id));
    }
    root.querySelectorAll('[data-futuresim-period-label]').forEach((node) => {
      node.textContent = period.label;
    });
    if (downloadLink) {
      downloadLink.href = period.src.split('?')[0];
      downloadLink.download = 'futuresim_' + id.replace(/-/g, '_') + '_results.json';
    }
    /* The previous period stays on screen until this one has loaded. */
    load(period)
      .then((data) => {
        if (selection.period === id) show(() => chartView(data, period));
      })
      .catch((error) => {
        console.error('FutureSim chart: showing the static figure for ' + period.label + '.', error);
        if (selection.period === id) show(() => fallbackView(period));
      });
  }

  for (const button of metricButtons) {
    button.addEventListener('click', () => {
      selection.metric = button.dataset.futuresimMetric in METRICS ? button.dataset.futuresimMetric : 'top1';
      for (const item of metricButtons) item.setAttribute('aria-pressed', String(item === button));
      if (view) view.setMetric(selection.metric);
    });
  }
  for (const button of periodButtons) {
    button.addEventListener('click', () => {
      if (button.dataset.futuresimPeriod !== selection.period) selectPeriod(button.dataset.futuresimPeriod);
    });
  }
  selectPeriod(selection.period);
})();
