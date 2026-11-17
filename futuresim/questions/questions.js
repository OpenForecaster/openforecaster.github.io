/* The Questions section of the FutureSim front page (_includes/futuresim-questions.html).
 *
 * Reads futuresim/questions/data/q3_questions.json (built by
 * scripts/build_futuresim_questions_data.py) and draws two views of the 50 previewed questions,
 * with a switch between them:
 *   - a mosaic: a block per category, sized by how many questions it holds, and in it a tile per
 *     question carrying that question's pictogram (art.js); pointing at a tile shows a summary,
 *   - cards: a category filter, search and sort over one card per question, with the answer, a
 *     sparkline and a per-agent result strip.
 * Either way a question opens in a detail dialog with its forecast chart: a line per agent, a
 * day scrubber with replay, and each agent's forecast in force on the chosen day.
 * A question is addressable as #q-<id>.
 */
(function () {
  'use strict';

  const root = document.querySelector('[data-fq-app]');
  if (!root) return;

  const SVG_NS = 'http://www.w3.org/2000/svg';
  const DAY_MS = 86400000;
  // The summary shown on pointing at a tile gives the forecasts of this many days before the
  // question resolved.
  const LEAD_DAYS = 7;
  const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const MONTHS_LONG = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  const LOGOS = { openai: 'openai.svg', anthropic: 'anthropic.svg', deepseek: 'deepseek.svg', zhipu: 'zhipu.png', qwen: 'qwen.svg', meta: 'meta.svg', google: 'gemini.svg' };
  // How to work the chart, worded for a mouse or for a touch screen.
  const HINTS = !window.matchMedia || window.matchMedia('(hover: hover)').matches
    ? {
      day: 'Click or drag the chart to pick a day.',
      hide: 'Click to hide this line',
      show: 'Click to show this line',
      mosaic: 'Point at a tile for a summary, or click it to see how the forecasts moved.',
    }
    : {
      day: 'Tap or drag the chart to pick a day.',
      hide: 'Tap to hide this line',
      show: 'Tap to show this line',
      mosaic: 'Tap a tile for a summary, and tap again to see how the forecasts moved.',
    };

  // `steps`, `intervals` and `span` shape the value axis, which is fitted to each question (fitAxis).
  const METRICS = {
    p: {
      label: 'Probability on the ground truth',
      steps: [0.01, 0.02, 0.05, 0.1, 0.2],
      intervals: 6,
      span: 0.05,
      tick: (v) => Math.round(v * 100) + '%',
      note: 'Each line is the mean of an agent’s runs. ' + HINTS.day,
    },
    b: {
      label: 'Brier skill score',
      steps: [0.02, 0.05, 0.1, 0.2, 0.25, 0.5],
      intervals: 7,
      span: 0.1,
      tick: (v) => (v < 0 ? '−' : '') + Math.abs(v),
      note: '1 is a perfect forecast, 0 is no forecast, and below 0 is confident and wrong. ' + HINTS.day,
    },
  };
  const SORTS = {
    date: (a, b) => a.day - b.day,
    category: (a, b) => a.cat.index - b.cat.index || a.top.index - b.top.index,
    hard: (a, b) => a.right - b.right || a.conf - b.conf,
    easy: (a, b) => b.right - a.right || b.conf - a.conf,
    swing: (a, b) => b.swing - a.swing,
  };

  const iconBase = root.getAttribute('data-icons') || '';
  const logoBase = root.getAttribute('data-logos') || '';
  const reduceMotion = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  const $ = (selector) => root.querySelector(selector);

  const els = {
    mosaic: $('[data-fq-mosaic]'),
    mosaicNote: $('[data-fq-mosaic-note]'),
    filters: $('[data-fq-filters]'),
    search: $('[data-fq-search]'),
    sort: $('[data-fq-sort]'),
    count: $('[data-fq-count]'),
    key: $('[data-fq-key]'),
    list: $('[data-fq-list]'),
    dialog: $('[data-fq-dialog]'),
  };

  let data = null;
  let startMs = 0;
  let totalDays = 0;
  const byId = {};
  const selected = new Set();
  let query = '';
  let sort = 'date';
  let visible = [];
  let view = 'mosaic';

  /* Small helpers ----------------------------------------------------------- */

  function h(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function s(tag, attrs) {
    const node = document.createElementNS(SVG_NS, tag);
    if (attrs) Object.keys(attrs).forEach((name) => node.setAttribute(name, attrs[name]));
    return node;
  }

  function icon(name) {
    const svg = s('svg', { class: 'fq-icon', 'aria-hidden': 'true', focusable: 'false' });
    svg.appendChild(s('use', { href: iconBase + '#qi-' + name }));
    return svg;
  }

  function logo(model) {
    const file = LOGOS[model.vendor];
    if (!file) return null;
    const img = h('img');
    img.alt = '';
    img.decoding = 'async';
    img.addEventListener('error', () => img.remove());
    img.src = logoBase + file;
    return img;
  }

  /* A model's mark: its maker's logo in a ring of the model's colour, as at the line ends of the chart. */
  function badge(model) {
    const ring = h('span', 'fq-badge');
    ring.style.setProperty('--fq-series', model.color);
    const mark = logo(model);
    if (mark) ring.appendChild(mark);
    return ring;
  }

  const clamp = (value, lo, hi) => Math.min(hi, Math.max(lo, value));
  const f = (value) => String(Math.round(value * 100) / 100);
  const isoMs = (iso) => {
    const parts = iso.split('-');
    return Date.UTC(+parts[0], +parts[1] - 1, +parts[2]);
  };
  const isoDay = (iso) => Math.round((isoMs(iso) - startMs) / DAY_MS);
  const dayDate = (day) => new Date(startMs + day * DAY_MS);
  const shortOf = (date) => date.getUTCDate() + ' ' + MONTHS[date.getUTCMonth()];
  const longOf = (date) => date.getUTCDate() + ' ' + MONTHS_LONG[date.getUTCMonth()] + ' ' + date.getUTCFullYear();
  const shortDate = (day) => shortOf(dayDate(day));
  const longDate = (day) => longOf(dayDate(day));
  const fmtP = (v) => (v > 0 && v < 0.005 ? '<1%' : Math.round(v * 100) + '%');
  const fmtB = (v) => {
    const text = Math.abs(v).toFixed(2);
    return (v < 0 && text !== '0.00' ? '−' : '') + text;
  };
  const plural = (n, word) => n + ' ' + word + (n === 1 ? '' : 's');
  // Search matches whichever apostrophe or quote style was typed.
  const plainQuotes = (text) => text.replace(/[\u2018\u2019]/g, "'").replace(/[\u201C\u201D]/g, '"');

  /* Index of the forecast in force on `day`: the last change on or before it. */
  function stepIndex(days, day) {
    let index = -1;
    for (let i = 0; i < days.length && days[i] <= day; i++) index = i;
    return index;
  }

  /* The day a question's summary describes: LEAD_DAYS before it resolved (its first day, if it
   * ran for less than that). */
  function leadDay(q) {
    return Math.max(0, q.day - LEAD_DAYS);
  }

  /* Moves label centres at least `gap` apart, each as near its target as the range lo..hi allows.
   * Labels that would overlap are stacked as one group around the mean of their targets. */
  function spread(targets, gap, lo, hi) {
    const order = targets.map((_, index) => index).sort((a, b) => targets[a] - targets[b] || a - b);
    const groups = [];
    const settle = (group) => {
      const n = group.members.length;
      group.top = clamp(group.sum / n, lo, Math.max(lo, hi - (n - 1) * gap));
    };
    order.forEach((index) => {
      let group = { members: [index], sum: targets[index] };
      settle(group);
      while (groups.length) {
        const above = groups[groups.length - 1];
        if (above.top + above.members.length * gap <= group.top) break;
        groups.pop();
        group = {
          members: above.members.concat(group.members),
          sum: above.sum + group.sum - group.members.length * above.members.length * gap,
        };
        settle(group);
      }
      groups.push(group);
    });
    const centres = [];
    groups.forEach((group) => {
      group.members.forEach((index, k) => {
        centres[index] = group.top + k * gap;
      });
    });
    return centres;
  }

  /* A value axis that fits lo..hi. The step is the finest of `steps` that covers the range in at
   * most `intervals` gaps, and the bottom is moved out to a multiple of it. The top is the next
   * multiple only when the highest value is nearly there (within AXIS_SNAP of the plot height);
   * otherwise it stops AXIS_ROOM of the plot height above the highest value, so the best line
   * always runs close to the top of the plot. */
  const AXIS_SNAP = 0.1;
  const AXIS_ROOM = 0.05;

  function fitAxis(lo, hi, steps, intervals) {
    const first = (step) => Math.floor(lo / step + 1e-9);
    const last = (step) => Math.ceil(hi / step - 1e-9);
    const step = steps.find((size) => last(size) - first(size) <= intervals) || steps[steps.length - 1];
    const bottom = first(step) * step;
    const grid = last(step) * step;
    const top = grid - hi <= AXIS_SNAP * (grid - bottom) ? grid : hi + (AXIS_ROOM / (1 - AXIS_ROOM)) * (hi - bottom);
    const ticks = [];
    for (let k = first(step); k * step <= top + 1e-9; k++) ticks.push(Math.round(k * step * 100) / 100);
    return { lo: ticks[0], hi: Math.round(top * 1e4) / 1e4, ticks: ticks };
  }

  function prepare() {
    startMs = isoMs(data.sim_start);
    totalDays = isoDay(data.sim_end);
    const categoryById = {};
    data.categories.forEach((category, index) => {
      category.index = index;
      category.topics = 0;
      categoryById[category.id] = category;
    });
    const topicById = {};
    data.topics.forEach((topic, index) => {
      topic.index = index;
      topicById[topic.id] = topic;
      categoryById[topic.category].topics += 1;
    });
    data.questions.forEach((q, index) => {
      q.index = index;
      q.day = Math.max(1, isoDay(q.resolves));
      q.cat = categoryById[q.category];
      q.top = topicById[q.topic];
      // "Sport · Tennis"; a category with a single topic needs no second name.
      q.filed = q.cat.topics > 1 ? q.cat.label + ' · ' + q.top.label : q.cat.label;
      // Average probability on the answer across agents; an agent with no forecast yet counts as 0.
      q.avg = [];
      for (let day = 0; day <= q.day; day++) {
        let sum = 0;
        data.models.forEach((model) => {
          const series = q.series[model.id];
          const i = series ? stepIndex(series.d, day) : -1;
          if (i >= 0) sum += series.p[i];
        });
        q.avg.push(sum / data.models.length);
      }
      q.swing = Math.max.apply(null, q.avg) - Math.min.apply(null, q.avg);
      let right = 0;
      let conf = 0;
      data.models.forEach((model) => {
        const final = q.final[model.id] || {};
        right += final.a || 0;
        conf += final.p || 0;
      });
      q.right = right / data.models.length;
      q.conf = conf / data.models.length;
      q.search = plainQuotes((q.title + ' ' + q.answer + ' ' + q.cat.label + ' ' + q.top.label).toLowerCase());
      byId[q.id] = q;
    });
  }

  /* Category filter --------------------------------------------------------- */

  const chips = {};

  function chip(label, count, iconName, onClick) {
    const button = h('button', 'fq-chip');
    button.type = 'button';
    button.setAttribute('aria-pressed', 'false');
    button.setAttribute('aria-label', label + ', ' + plural(count, 'question'));
    if (iconName) button.appendChild(icon(iconName));
    button.append(h('span', null, label), h('span', 'fq-chip-n', String(count)));
    button.addEventListener('click', onClick);
    return button;
  }

  function renderFilters() {
    chips.all = chip('All', data.questions.length, null, () => {
      selected.clear();
      applyFilters();
    });
    els.filters.replaceChildren(chips.all);
    data.categories.forEach((category) => {
      chips[category.id] = chip(category.label, category.preview, category.icon, () => {
        if (selected.has(category.id)) selected.delete(category.id);
        else selected.add(category.id);
        applyFilters();
      });
      els.filters.appendChild(chips[category.id]);
    });
  }

  /* Question cards ---------------------------------------------------------- */

  function sparkline(q) {
    const width = 100;
    const height = 26;
    // Each sparkline spans the question's own life: 24 Jun on the left, its resolution on the right.
    const x = (day) => 1 + (day / Math.max(1, q.day)) * (width - 2);
    const y = (p) => height - 3 - p * (height - 6);
    const svg = s('svg', { class: 'fq-spark', viewBox: '0 0 ' + width + ' ' + height, 'aria-hidden': 'true', focusable: 'false' });
    svg.appendChild(s('line', { class: 'fq-spark-base', x1: 1, x2: width - 1, y1: height - 2.5, y2: height - 2.5 }));
    let path = 'M' + f(x(0)) + ' ' + f(y(q.avg[0]));
    for (let day = 1; day <= q.day; day++) {
      if (q.avg[day] !== q.avg[day - 1]) path += 'H' + f(x(day)) + 'V' + f(y(q.avg[day]));
    }
    path += 'H' + f(x(q.day));
    svg.appendChild(s('path', { class: 'fq-spark-area', d: path + 'V' + f(y(0)) + 'H' + f(x(0)) + 'Z' }));
    svg.appendChild(s('path', { class: 'fq-spark-line', d: path, pathLength: 1 }));
    svg.appendChild(s('circle', { class: 'fq-spark-end', cx: f(x(q.day)), cy: f(y(q.avg[q.day])), r: 2.2 }));
    return svg;
  }

  function resultStrip(q) {
    const strip = h('span', 'fq-strip');
    const parts = [];
    data.models.forEach((model) => {
      const final = q.final[model.id] || {};
      const hits = Math.round((final.a || 0) * model.seeds);
      const square = h('span', 'fq-sq');
      square.style.setProperty('--fq-sq', model.color);
      square.dataset.state = hits >= model.seeds ? 'all' : hits > 0 ? 'some' : 'none';
      const text = model.name + ': top pick right in ' + hits + ' of ' + plural(model.seeds, 'run');
      square.title = text;
      parts.push(text);
      strip.appendChild(square);
    });
    strip.setAttribute('role', 'img');
    strip.setAttribute('aria-label', parts.join('; '));
    return strip;
  }

  function buildCard(q) {
    const item = h('li');
    const link = h('a', 'fq-card');
    link.href = '#q-' + q.id;
    const category = h('span', 'fq-card-cat');
    category.append(icon(q.topic), h('span', null, q.cat.label));
    const answer = h('span', 'fq-card-answer');
    answer.append(icon('check'), h('span', null, q.answer));
    const trend = h('span', 'fq-card-trend');
    trend.title = 'Average probability on the answer: ' + fmtP(q.avg[0]) + ' on ' + shortDate(0)
      + ', ' + fmtP(q.avg[q.day]) + ' when it resolved';
    trend.appendChild(sparkline(q));
    const result = h('span', 'fq-card-result');
    result.append(trend, resultStrip(q));
    const foot = h('span', 'fq-card-foot');
    foot.append(h('span', 'fq-card-when', 'Answer · resolved ' + shortDate(q.day)), answer, result);
    link.append(category, h('span', 'fq-card-title', q.title), foot);
    link.addEventListener('click', (event) => {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      navigate(q, true);
    });
    item.appendChild(link);
    q.card = item;
  }

  function renderKey() {
    const squares = h('span', 'fq-key-part');
    squares.appendChild(h('span', null, 'Was the agent’s top pick right when the question resolved?'));
    [['all', 'in every run'], ['some', 'in some runs'], ['none', 'in none']].forEach((pair) => {
      const item = h('span', 'fq-key-item');
      const square = h('span', 'fq-sq');
      square.dataset.state = pair[0];
      item.append(square, pair[1]);
      squares.appendChild(item);
    });
    const agents = h('span', 'fq-key-part');
    agents.appendChild(h('span', null, 'One square per agent, left to right:'));
    data.models.forEach((model) => {
      const item = h('span', 'fq-key-item');
      const swatch = h('span', 'fq-sq');
      swatch.style.setProperty('--fq-sq', model.color);
      swatch.dataset.state = 'all';
      item.appendChild(swatch);
      const mark = logo(model);
      if (mark) item.appendChild(mark);
      item.append(model.name);
      agents.appendChild(item);
    });
    const spark = h('span', 'fq-key-part fq-key-line');
    const glyph = s('svg', { class: 'fq-key-spark', viewBox: '0 0 26 12', 'aria-hidden': 'true', focusable: 'false' });
    glyph.appendChild(s('path', { d: 'M1 10H7V7H13V8.5H19V2.5H25' }));
    spark.append(glyph, h('span', null, 'average probability the ' + data.models.length
      + ' agents put on the answer, from ' + shortDate(0) + ' to the day it resolved'));
    els.key.replaceChildren(squares, agents, spark);
  }

  function applyFilters() {
    const terms = plainQuotes(query.trim().toLowerCase()).split(/\s+/).filter(Boolean);
    visible = data.questions.filter((q) => {
      if (selected.size && !selected.has(q.category)) return false;
      return terms.every((term) => q.search.indexOf(term) !== -1);
    });
    const compare = SORTS[sort] || SORTS.date;
    visible.sort((a, b) => compare(a, b) || a.day - b.day || a.index - b.index);

    chips.all.setAttribute('aria-pressed', selected.size ? 'false' : 'true');
    data.categories.forEach((category) => {
      chips[category.id].setAttribute('aria-pressed', selected.has(category.id) ? 'true' : 'false');
    });

    const total = data.questions.length;
    els.count.textContent = visible.length === total
      ? plural(total, 'question')
      : visible.length + ' of ' + plural(total, 'question');
    if (visible.length) {
      els.list.replaceChildren.apply(els.list, visible.map((q) => q.card));
    } else {
      const empty = h('li', 'fq-empty');
      empty.textContent = terms.length
        ? 'No question in this preview matches “' + query.trim() + '”' + (selected.size ? ' in the selected categories.' : '.')
        : 'No question in this preview is in the selected categories.';
      els.list.replaceChildren(empty);
    }
  }

  /* Mosaic ------------------------------------------------------------------ */

  const ART_BOX = '18 12 264 176'; // the part of art.js's 300 by 200 canvas a tile shows
  const BLOCK_GAP = 6;
  const TILE_GAP = 3;              // between tiles, and between the tiles and their block's edge
  const BLOCK_ASPECT = 1.5;        // the shape the blocks aim for; the pictograms are 3:2 too
  const TILE_ASPECT = 1.5;
  const mosaic = { blocks: [], order: [], width: 0, height: 0 };
  const peek = { el: null, q: null, pinned: false, timer: 0 };
  let touched = null;  // the question whose tile a finger last went down on
  let quietUntil = 0;  // no pop-up for the focus that returns to a tile as the dialog closes

  function art(q) {
    const drawn = window.FQ_ART || {};
    const markup = (drawn.byId || {})[q.id] || (drawn.byCategory || {})[q.category];
    if (!markup) {
      const plain = icon(q.topic);
      plain.setAttribute('class', 'fq-icon fq-art-plain');
      return plain;
    }
    const svg = s('svg', { class: 'fq-art', viewBox: ART_BOX, 'aria-hidden': 'true', focusable: 'false' });
    svg.innerHTML = markup;
    return svg;
  }

  /* A squarified treemap (Bruls, Huizing and van Wijk): fills the rectangle strip by strip along
   * its shorter side, and closes a strip once another cell would make its cells less square. */
  function squarify(weights, width, height) {
    const total = weights.reduce((sum, weight) => sum + weight, 0);
    const areas = weights.map((weight) => weight / total * width * height);
    const cells = [];
    let x = 0;
    let y = 0;
    let strip = [];
    let stripArea = 0;
    const worst = (list, area, side) => {
      const thick = area / side;
      return list.reduce((sofar, i) => {
        const length = areas[i] / thick;
        return Math.max(sofar, length / thick, thick / length);
      }, 0);
    };
    const close = () => {
      const upright = width >= height;
      const thick = stripArea / (upright ? height : width);
      let along = 0;
      strip.forEach((i) => {
        const length = areas[i] / thick;
        cells[i] = upright ? { x: x, y: y + along, w: thick, h: length } : { x: x + along, y: y, w: length, h: thick };
        along += length;
      });
      if (upright) {
        x += thick;
        width -= thick;
      } else {
        y += thick;
        height -= thick;
      }
      strip = [];
      stripArea = 0;
    };
    areas.forEach((area, i) => {
      const side = Math.min(width, height);
      if (strip.length && worst(strip.concat(i), stripArea + area, side) > worst(strip, stripArea, side)) close();
      strip.push(i);
      stripArea += area;
    });
    close();
    return cells;
  }

  /* How many rows of tiles suit a block: the count that keeps the tiles closest to 3:2. */
  function rowsFor(count, width, height) {
    let best = 1;
    let bestCost = Infinity;
    for (let rows = 1; rows <= count; rows++) {
      const tileHeight = (height - (rows - 1) * TILE_GAP) / rows;
      const few = Math.floor(count / rows);
      const cost = [[few, rows - count % rows], [few + 1, count % rows]].reduce((sum, pair) => {
        if (!pair[1]) return sum;
        const tileWidth = (width - (pair[0] - 1) * TILE_GAP) / pair[0];
        if (tileWidth <= 0 || tileHeight <= 0) return Infinity;
        return sum + pair[0] * pair[1] * Math.abs(Math.log(tileWidth / tileHeight / TILE_ASPECT));
      }, 0);
      if (cost < bestCost) {
        best = rows;
        bestCost = cost;
      }
    }
    return best;
  }

  function buildTile(q) {
    const tile = h('a', 'fq-tile');
    tile.href = '#q-' + q.id;
    tile.setAttribute('aria-label', q.title);
    tile.appendChild(art(q));
    tile.addEventListener('pointerenter', (event) => {
      if (event.pointerType !== 'mouse') return;
      clearTimeout(peek.timer);
      // The first pop-up waits a moment; moving on to a neighbour follows the pointer at once.
      if (peek.q) showPeek(q, false);
      else peek.timer = setTimeout(() => showPeek(q, false), 90);
    });
    tile.addEventListener('pointerleave', (event) => {
      if (event.pointerType !== 'mouse' || peek.pinned) return;
      clearTimeout(peek.timer);
      peek.timer = setTimeout(hidePeek, 110);
    });
    tile.addEventListener('pointerdown', (event) => {
      touched = event.pointerType === 'mouse' ? null : q;
    });
    tile.addEventListener('focus', () => {
      let keyboard = false;
      try { keyboard = tile.matches(':focus-visible'); } catch (error) { /* an old browser */ }
      if (keyboard && performance.now() > quietUntil) showPeek(q, false);
    });
    tile.addEventListener('blur', () => {
      if (peek.q === q && !peek.pinned) hidePeek();
    });
    tile.addEventListener('click', (event) => {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      // A finger cannot point, so its first tap shows the summary and its second opens the question.
      const firstTap = touched === q && peek.q !== q;
      touched = null;
      if (firstTap) {
        showPeek(q, true);
        return;
      }
      hidePeek();
      navigate(q, true);
    });
    q.tile = tile;
  }

  function buildPeek() {
    const el = h('div', 'fq-peek');
    el.id = 'fq-peek';
    el.setAttribute('role', 'tooltip');
    el.hidden = true;
    peek.art = h('span', 'fq-peek-art');
    peek.filed = h('span', 'fq-peek-filed');
    peek.topic = h('span', 'fq-peek-topic');
    peek.when = h('span', 'fq-peek-when');
    const meta = h('span', 'fq-peek-meta');
    meta.append(peek.filed, peek.topic, peek.when);
    peek.band = h('div', 'fq-peek-band');
    peek.band.append(peek.art, meta);
    peek.title = h('p', 'fq-peek-title');
    peek.answer = h('span', 'fq-peek-answer');
    const answer = h('p', 'fq-peek-fact');
    answer.append(h('span', 'fq-peek-label', 'Answer'), peek.answer);
    const rows = h('div', 'fq-peek-rows');
    peek.rows = data.models.map((model) => {
      const row = h('div', 'fq-peek-row');
      const fill = h('span', 'fq-peek-fill');
      fill.style.setProperty('--fq-series', model.color);
      const track = h('span', 'fq-peek-track');
      track.appendChild(fill);
      const value = h('span', 'fq-peek-value');
      row.append(logo(model) || h('span'), h('span', 'fq-peek-name', model.name), track, value);
      rows.appendChild(row);
      return { model: model, fill: fill, value: value };
    });
    const agents = h('div', 'fq-peek-agents');
    peek.label = h('p', 'fq-peek-label');
    agents.append(peek.label, rows);
    peek.hint = h('p', 'fq-peek-hint');
    const body = h('div', 'fq-peek-body');
    body.append(peek.title, answer, agents, peek.hint);
    el.append(peek.band, body);
    el.addEventListener('click', () => {
      const q = peek.q;
      if (!q) return;
      hidePeek();
      navigate(q, true);
    });
    peek.el = el;
  }

  function showPeek(q, pinned) {
    clearTimeout(peek.timer);
    if (view !== 'mosaic') return;
    if (peek.q === q && peek.pinned === pinned) return;
    if (peek.q) {
      peek.q.tile.classList.remove('is-peeked');
      peek.q.tile.removeAttribute('aria-describedby');
    }
    peek.q = q;
    peek.pinned = pinned;

    peek.el.dataset.fqCat = q.category;
    peek.art.replaceChildren(art(q));
    peek.filed.textContent = q.cat.label;
    peek.topic.textContent = q.top.label;
    peek.topic.hidden = q.cat.topics < 2;
    peek.when.textContent = 'Resolved ' + shortDate(q.day);
    peek.title.textContent = q.title;
    peek.answer.textContent = q.answer;
    const day = leadDay(q);
    peek.label.textContent = 'Probability on the answer ' + plural(q.day - day, 'day') + ' before it resolved';
    peek.rows.forEach((row) => {
      const series = q.series[row.model.id];
      const i = series ? stepIndex(series.d, day) : -1;
      const p = i < 0 ? null : series.p[i];
      row.fill.style.width = p == null ? '0' : f(clamp(p, 0, 1) * 100) + '%';
      row.value.textContent = p == null ? '–' : fmtP(p);
    });
    peek.hint.textContent = pinned ? 'Tap to open the forecast chart' : 'Click to open the forecast chart';
    peek.el.classList.toggle('is-pinned', pinned);
    peek.el.hidden = false;

    q.tile.classList.add('is-peeked');
    q.tile.setAttribute('aria-describedby', peek.el.id);
    els.mosaic.classList.add('has-peek');
    placePeek(q.tile);
  }

  // Above the tile where there is room under the site's fixed bar, else below it, else beside it.
  function placePeek(tile) {
    const frame = els.mosaic.getBoundingClientRect();
    const box = tile.getBoundingClientRect();
    const width = peek.el.offsetWidth;
    const height = peek.el.offsetHeight;
    const bar = document.querySelector('.topbar');
    const ceiling = (bar && getComputedStyle(bar).position === 'fixed' ? bar.getBoundingClientRect().bottom : 0) + 8;
    const floor = window.innerHeight - 8;
    const reach = 11;
    const above = box.top - reach - ceiling;
    const below = floor - box.bottom - reach;
    const after = document.documentElement.clientWidth - 8 - box.right - reach;
    const before = box.left - reach - 8;
    let side = above >= below ? 'above' : 'below';
    if (above >= height) side = 'above';
    else if (below >= height) side = 'below';
    else if (floor - ceiling >= height && Math.max(after, before) >= width) side = after >= width ? 'right' : 'left';

    let x;
    let y;
    let caret;
    if (side === 'above' || side === 'below') {
      const middle = box.left + box.width / 2;
      x = clamp(middle - width / 2, frame.left, Math.max(frame.left, frame.right - width));
      y = side === 'above' ? box.top - reach - height : box.bottom + reach;
      caret = clamp(middle - x, 18, width - 18);
    } else {
      const middle = box.top + box.height / 2;
      x = side === 'right' ? box.right + reach : box.left - reach - width;
      y = clamp(middle - height / 2, ceiling, floor - height);
      caret = clamp(middle - y, 18, height - 18);
    }
    peek.el.dataset.side = side;
    peek.el.style.left = f(x - frame.left) + 'px';
    peek.el.style.top = f(y - frame.top) + 'px';
    peek.el.style.setProperty('--fq-caret', f(caret) + 'px');
    // The pointer takes the colour of the part of the summary it sits against.
    const onBand = side === 'below' || (side !== 'above' && caret < peek.band.offsetHeight);
    peek.el.classList.toggle('is-on-band', onBand);
  }

  function hidePeek() {
    clearTimeout(peek.timer);
    if (!peek.q) return;
    peek.q.tile.classList.remove('is-peeked');
    peek.q.tile.removeAttribute('aria-describedby');
    peek.q = null;
    peek.pinned = false;
    peek.el.hidden = true;
    els.mosaic.classList.remove('has-peek');
  }

  function buildMosaic() {
    // Largest category first, which is the order a treemap wants; in a block, by resolution date.
    mosaic.blocks = data.categories.map((category) => ({
      category: category,
      questions: data.questions.filter((q) => q.cat === category).sort((a, b) => a.day - b.day || a.index - b.index),
      rows: 0,
    })).filter((block) => block.questions.length)
      .sort((a, b) => b.questions.length - a.questions.length || a.category.index - b.category.index);

    mosaic.blocks.forEach((block) => {
      const count = block.questions.length;
      block.el = h('section', 'fq-block');
      block.el.dataset.fqCat = block.category.id;
      block.el.setAttribute('aria-label', block.category.label + ', ' + plural(count, 'question'));
      const head = h('h3', 'fq-block-head');
      const tally = h('span', 'fq-block-n', String(count));
      tally.appendChild(h('span', 'fq-visually-hidden', count === 1 ? ' question' : ' questions'));
      // "Arts & entertainment" becomes "Arts" where the block is too narrow for the whole name.
      block.short = block.category.label.split(' & ')[0];
      block.name = h('span', 'fq-block-name', block.category.label);
      head.append(icon(block.category.icon), block.name, tally);
      block.tiles = h('div', 'fq-tiles');
      block.el.append(head, block.tiles);
      block.questions.forEach(buildTile);
      mosaic.order = mosaic.order.concat(block.questions);
    });

    buildPeek();
    els.mosaic.replaceChildren.apply(els.mosaic, mosaic.blocks.map((block) => block.el).concat(peek.el));
    els.mosaicNote.textContent = 'Each tile is one question. A block’s size shows how many of the '
      + data.questions.length + ' fall in that category. ' + HINTS.mosaic;

    els.mosaic.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && peek.q) hidePeek();
    });
    document.addEventListener('pointerdown', (event) => {
      if (!peek.pinned) return;
      const target = event.target;
      if (!target || !target.closest || !target.closest('.fq-tile, .fq-peek')) hidePeek();
    });
    if ('ResizeObserver' in window) new ResizeObserver(layoutMosaic).observe(els.mosaic);
    else window.addEventListener('resize', layoutMosaic);
    layoutMosaic();
  }

  function layoutMosaic() {
    const width = els.mosaic.clientWidth;
    const height = els.mosaic.clientHeight;
    if (!width || !height || (width === mosaic.width && height === mosaic.height)) return;
    mosaic.width = width;
    mosaic.height = height;
    hidePeek();

    const head = width < 560 ? 26 : 30;
    els.mosaic.style.setProperty('--fq-head', head + 'px');
    // What a cell leaves for its tiles, once the gap around the block, its heading and its edges are taken.
    const room = (cell) => ({
      w: Math.max(1, cell.w - BLOCK_GAP - 2 * TILE_GAP),
      h: Math.max(1, cell.h - BLOCK_GAP - head - TILE_GAP),
    });
    const counts = mosaic.blocks.map((block) => block.questions.length);
    const total = counts.reduce((sum, count) => sum + count, 0);
    const spanX = width + BLOCK_GAP;
    const spanY = height + BLOCK_GAP;
    // A heading takes a larger share of a small block than of a big one. Three more passes hand
    // each block that space back, so a tile covers about the same area in every category.
    let weights = counts;
    let cells = [];
    for (let pass = 0; pass < 4; pass++) {
      cells = squarify(weights, spanX / BLOCK_ASPECT, spanY);
      cells.forEach((cell) => {
        cell.x *= BLOCK_ASPECT;
        cell.w *= BLOCK_ASPECT;
      });
      const taken = cells.map((cell) => cell.w * cell.h - room(cell).w * room(cell).h);
      const perTile = (spanX * spanY - taken.reduce((sum, area) => sum + area, 0)) / total;
      weights = counts.map((count, i) => count * perTile + taken[i]);
    }

    mosaic.blocks.forEach((block, i) => {
      const cell = cells[i];
      const left = Math.round(cell.x);
      const top = Math.round(cell.y);
      block.el.style.left = left + 'px';
      block.el.style.top = top + 'px';
      block.el.style.width = Math.max(0, Math.round(cell.x + cell.w) - left - BLOCK_GAP) + 'px';
      block.el.style.height = Math.max(0, Math.round(cell.y + cell.h) - top - BLOCK_GAP) + 'px';

      const count = block.questions.length;
      const rows = rowsFor(count, room(cell).w, room(cell).h);
      if (rows === block.rows) return;
      block.rows = rows;
      // The rows that hold one tile fewer, and so larger tiles, come first.
      const few = Math.floor(count / rows);
      const fewRows = rows - count % rows;
      let next = 0;
      const lines = [];
      for (let r = 0; r < rows; r++) {
        const line = h('div', 'fq-tile-row');
        for (let size = r < fewRows ? few : few + 1; size > 0; size--) line.appendChild(block.questions[next++].tile);
        lines.push(line);
      }
      block.tiles.replaceChildren.apply(block.tiles, lines);
    });

    mosaic.blocks.forEach((block) => {
      block.name.textContent = block.category.label;
    });
    const cut = mosaic.blocks.filter((block) => block.name.scrollWidth > block.name.clientWidth);
    cut.forEach((block) => {
      block.name.textContent = block.short;
    });
  }

  function setView(next) {
    view = next;
    root.querySelectorAll('[data-fq-view]').forEach((button) => {
      button.setAttribute('aria-pressed', button.getAttribute('data-fq-view') === next ? 'true' : 'false');
    });
    root.querySelectorAll('[data-fq-pane]').forEach((pane) => {
      pane.hidden = pane.getAttribute('data-fq-pane') !== next;
    });
    hidePeek();
    if (next === 'mosaic') layoutMosaic();
  }

  /* Question detail --------------------------------------------------------- */

  const dlg = {};
  const hidden = new Set();
  let current = null;
  let metric = 'p';
  let pin = 0;        // the day the panel below the chart describes
  let hover = null;   // the day under the mouse, if any
  let clip = 0;       // how far the solid part of the lines reaches (fractional while animating)
  let chart = null;
  let anim = null;
  let dragging = false;
  let panelKey = '';

  function iconButton(name, label) {
    const button = h('button', 'fq-icon-button');
    button.type = 'button';
    button.setAttribute('aria-label', label);
    button.title = label;
    button.appendChild(icon(name));
    return button;
  }

  function buildDialog() {
    dlg.el = els.dialog;
    dlg.el.tabIndex = -1;

    const bar = h('div', 'fq-d-bar');
    dlg.art = h('span', 'fq-d-art');
    dlg.domain = h('p', 'fq-d-domain');
    const nav = h('div', 'fq-d-nav');
    dlg.position = h('span', 'fq-d-pos');
    dlg.prev = iconButton('prev', 'Previous question');
    dlg.next = iconButton('next', 'Next question');
    dlg.close = iconButton('close', 'Close');
    nav.append(dlg.position, dlg.prev, dlg.next, dlg.close);
    bar.append(dlg.art, dlg.domain, nav);

    // The question, across the full width, with its answer right under it.
    const hero = h('header', 'fq-d-hero');
    dlg.title = h('h2');
    dlg.title.id = 'fq-d-title';
    const facts = h('dl', 'fq-d-facts');
    const fact = (className, term) => {
      const wrap = h('div', className);
      const value = h('dd');
      wrap.append(h('dt', null, term), value);
      facts.appendChild(wrap);
      return value;
    };
    dlg.answer = fact('fq-fact-answer', 'Answer');
    dlg.resolved = fact('fq-fact-resolved', 'Resolved');
    dlg.source = fact('fq-fact-source', 'Source');
    hero.append(dlg.title, facts);

    dlg.body = h('div', 'fq-d-body');
    const chartBox = h('section', 'fq-chart');
    chartBox.setAttribute('aria-label', 'How the forecasts moved');

    dlg.legend = h('ul', 'fq-legend');
    dlg.legendButtons = {};
    data.models.forEach((model) => {
      const item = h('li');
      const button = h('button');
      button.type = 'button';
      button.append(badge(model), h('span', null, model.name));
      button.addEventListener('pointerenter', () => emphasize(model.id));
      button.addEventListener('pointerleave', () => emphasize(null));
      button.addEventListener('focus', () => emphasize(model.id));
      button.addEventListener('blur', () => emphasize(null));
      button.addEventListener('click', () => {
        if (hidden.has(model.id)) hidden.delete(model.id);
        else if (hidden.size < data.models.length - 1) hidden.add(model.id);
        else return;
        stopAnim();
        renderChart();
        renderPanel(true);
        emphasize(hidden.has(model.id) ? null : model.id);
      });
      dlg.legendButtons[model.id] = button;
      item.appendChild(button);
      // The space lets the names wrap in even rows (Firefox only balances at spaces).
      dlg.legend.append(item, ' ');
    });

    // What the chart measures, on the same row as the legend.
    const seg = h('div', 'fq-seg');
    seg.setAttribute('role', 'group');
    seg.setAttribute('aria-label', 'Measure');
    dlg.metricButtons = {};
    Object.keys(METRICS).forEach((key) => {
      const button = h('button', null, METRICS[key].label);
      button.type = 'button';
      button.addEventListener('click', () => {
        if (metric === key) return;
        metric = key;
        stopAnim();
        renderChart();
        renderPanel(true);
      });
      dlg.metricButtons[key] = button;
      seg.appendChild(button);
    });

    const head = h('div', 'fq-chart-head');
    head.append(dlg.legend, seg);
    dlg.plot = h('div', 'fq-plot');
    dlg.tip = h('div', 'fq-tip fq-chart-tip');
    dlg.tip.hidden = true;
    dlg.tipDate = h('span', 'fq-tip-meta');
    dlg.tip.appendChild(dlg.tipDate);
    dlg.tipValues = {};
    data.models.forEach((model) => {
      const row = h('span', 'fq-tip-row');
      const value = h('span', 'fq-tip-value');
      row.append(badge(model), h('span', 'fq-tip-name', model.name), value);
      dlg.tipValues[model.id] = { row: row, value: value };
      dlg.tip.appendChild(row);
    });

    // The timeline under the plot. Its track covers the same days at the same places as the
    // plot above it (renderChart passes the plot's left and right margins on).
    dlg.scrub = h('div', 'fq-scrub');
    dlg.play = h('button', 'fq-play');
    dlg.play.type = 'button';
    dlg.playIcon = icon('replay');
    dlg.playLabel = h('span', 'fq-visually-hidden', 'Replay');
    dlg.play.append(dlg.playIcon, dlg.playLabel);
    const track = h('div', 'fq-scrub-track');
    const rail = h('span', 'fq-scrub-rail');
    rail.appendChild(h('span', 'fq-scrub-fill'));
    dlg.range = h('input');
    dlg.range.type = 'range';
    dlg.range.min = '0';
    dlg.range.step = '1';
    dlg.range.setAttribute('aria-label', 'Day shown below the chart');
    track.append(rail, dlg.range);
    dlg.date = h('span', 'fq-scrub-date');
    dlg.scrub.append(dlg.play, track, dlg.date);

    dlg.note = h('p', 'fq-chart-note');
    chartBox.append(head, dlg.plot, dlg.scrub, dlg.note);

    const dayBox = h('section', 'fq-day');
    const dayHead = h('h3');
    dlg.dayLabel = h('span');
    dayHead.append('Forecasts on ', dlg.dayLabel);
    dlg.dayGrid = h('div', 'fq-day-grid');
    // Up to five cards to a row; with more agents the rows fill evenly (six sit three and three).
    const agentRows = Math.ceil(data.models.length / 5);
    dlg.dayGrid.style.setProperty('--fq-per-row', Math.ceil(data.models.length / agentRows));
    dayBox.append(dayHead, dlg.dayGrid);

    dlg.criteria = h('details', 'fq-criteria');
    dlg.criteria.appendChild(h('summary', null, 'Resolution Criteria'));
    dlg.criteriaList = h('dl');
    dlg.criteria.appendChild(dlg.criteriaList);

    dlg.body.append(chartBox, dayBox, dlg.criteria);
    dlg.el.replaceChildren(bar, hero, dlg.body);

    dlg.prev.addEventListener('click', () => step(-1));
    dlg.next.addEventListener('click', () => step(1));
    dlg.close.addEventListener('click', () => dlg.el.close());
    dlg.play.addEventListener('click', togglePlay);
    dlg.range.addEventListener('input', () => setPin(+dlg.range.value));

    // A click on the backdrop lands on the dialog element itself.
    dlg.el.addEventListener('click', (event) => {
      if (event.target === dlg.el) dlg.el.close();
    });
    dlg.el.addEventListener('keydown', (event) => {
      if (event.altKey || event.ctrlKey || event.metaKey) return;
      if (/^(INPUT|SELECT|TEXTAREA)$/.test(event.target.tagName)) return;
      if (event.key === 'ArrowLeft') step(-1);
      else if (event.key === 'ArrowRight') step(1);
      else return;
      event.preventDefault();
    });
    dlg.el.addEventListener('close', () => {
      stopAnim();
      current = null;
      chart = null;
      quietUntil = performance.now() + 400;
      document.documentElement.classList.remove('fq-lock');
      if (hashId()) {
        if (history.state && history.state.fq) history.back();
        // The page was opened on this question: leave its address at the section.
        else history.replaceState(null, '', location.pathname + location.search + (root.id ? '#' + root.id : ''));
      }
    });

    dlg.plot.addEventListener('pointermove', (event) => {
      if (!chart) return;
      const day = dayAt(event);
      if (dragging) {
        setPin(day);
      } else if (event.pointerType === 'mouse' && !(anim && anim.replay) && hover !== day) {
        hover = day;
        updateDay();
      }
    });
    dlg.plot.addEventListener('pointerdown', (event) => {
      if (!chart || event.button > 0) return;
      dragging = true;
      try { dlg.plot.setPointerCapture(event.pointerId); } catch (error) { /* not capturable */ }
      if (event.pointerType === 'mouse') hover = dayAt(event);
      setPin(dayAt(event));
    });
    const release = () => { dragging = false; };
    dlg.plot.addEventListener('pointerup', release);
    dlg.plot.addEventListener('pointercancel', release);
    dlg.plot.addEventListener('pointerleave', () => {
      if (hover == null) return;
      hover = null;
      updateDay();
    });
    if ('ResizeObserver' in window) {
      new ResizeObserver(() => {
        if (!current || !chart) return;
        if (Math.round(dlg.plot.clientWidth) !== chart.width) {
          stopAnim();
          renderChart();
        }
      }).observe(dlg.plot);
    }
  }

  /* The questions Previous and Next step through: the view's own order. */
  function navList() {
    if (view === 'mosaic') return mosaic.order;
    return visible.indexOf(current) !== -1 ? visible : data.questions.slice().sort((a, b) => a.day - b.day || a.index - b.index);
  }

  function step(delta) {
    if (!current) return;
    const list = navList();
    const target = list[list.indexOf(current) + delta];
    if (target) navigate(target, false);
  }

  function fillDialog(q) {
    dlg.el.dataset.fqCat = q.category;
    dlg.art.replaceChildren(art(q));
    dlg.domain.replaceChildren(h('b', null, q.cat.label));
    if (q.cat.topics > 1) dlg.domain.append(' · ' + q.top.label);
    const list = navList();
    const at = list.indexOf(q);
    dlg.position.textContent = (at + 1) + ' / ' + list.length;
    dlg.prev.disabled = at <= 0;
    dlg.next.disabled = at >= list.length - 1;

    dlg.title.textContent = q.title;
    dlg.answer.textContent = q.answer;
    dlg.resolved.textContent = longDate(q.day);

    // The headline that settled the question: one line under the title, in full further down.
    const article = q.article || {};
    const publisher = 'Al Jazeera';
    const outlet = publisher + (article.date ? ', ' + longOf(new Date(isoMs(article.date))) : '');
    const headline = () => {
      const text = h('span', null, article.title);
      if (!/^https?:\/\//.test(article.url || '')) return text;
      const link = h('a');
      link.href = article.url;
      link.target = '_blank';
      link.rel = 'noreferrer';
      link.append(text, icon('external'));
      return link;
    };
    dlg.source.parentNode.hidden = !article.title;
    dlg.source.replaceChildren();
    if (article.title) {
      const short = headline();
      short.title = article.title + ' (' + outlet + ')';
      // The publisher follows the headline and stays in view when the headline is cut short.
      const name = h('span', 'fq-fact-outlet', '(' + publisher + ')');
      dlg.source.appendChild(short);
      if (short.tagName === 'A') short.insertBefore(name, short.lastChild);
      else dlg.source.appendChild(name);
    }

    dlg.range.max = String(q.day);

    dlg.criteriaList.replaceChildren();
    (q.criteria || []).forEach((pair) => {
      const wrap = h('div');
      if (pair[0]) wrap.appendChild(h('dt', null, pair[0]));
      wrap.appendChild(h('dd', null, pair[1]));
      dlg.criteriaList.appendChild(wrap);
    });
    if (article.title) {
      const wrap = h('div');
      const value = h('dd');
      value.append(headline(), h('span', null, outlet));
      if (article.related_only) {
        // The question was written from a headline in the article's list of related stories.
        value.appendChild(h('span', null, 'This article is about something else; it names the answer in its list of related stories.'));
      }
      wrap.append(h('dt', null, 'Article that settled it'), value);
      dlg.criteriaList.appendChild(wrap);
    }
    dlg.criteria.hidden = !dlg.criteriaList.childElementCount;
    dlg.criteria.open = false;
  }

  function stepPath(days, values, X, Y, endDay) {
    let path = 'M' + f(X(days[0])) + ' ' + f(Y(values[0]));
    for (let i = 1; i < days.length; i++) {
      path += 'H' + f(X(days[i]));
      if (values[i] !== values[i - 1]) path += 'V' + f(Y(values[i]));
    }
    return path + 'H' + f(X(endDay));
  }

  function bandPath(days, lo, hi, X, Y, endDay) {
    const n = days.length;
    let path = 'M' + f(X(days[0])) + ' ' + f(Y(hi[0]));
    for (let i = 1; i < n; i++) path += 'H' + f(X(days[i])) + 'V' + f(Y(hi[i]));
    path += 'H' + f(X(endDay)) + 'V' + f(Y(lo[n - 1]));
    for (let i = n - 1; i > 0; i--) path += 'H' + f(X(days[i])) + 'V' + f(Y(lo[i - 1]));
    return path + 'H' + f(X(days[0])) + 'Z';
  }

  function renderChart() {
    const q = current;
    if (!q) return;
    const spec = METRICS[metric];
    const width = Math.max(280, Math.round(dlg.plot.clientWidth));
    const narrow = width < 560;
    // Each line ends in a badge with its value, which needs room to the right of the plot
    // and, for a line at the top of the axis, a little above it.
    const ring = narrow ? 10 : 12.5;
    const reach = narrow ? 19 : 27;
    const x0 = 44;
    const x1 = width - reach - ring - (narrow ? 47 : 56);
    const y0 = ring + 4;
    const y1 = y0 + (narrow ? 194 : 282);
    const height = y1 + 32;

    // The value axis fits the lines on show, so its top sits just above the best agent's line and
    // a question where no agent went above 30% is not drawn on an axis that runs to 100%. The range
    // of an agent's runs (the band behind an emphasised line) does not stretch the axis; where it
    // goes past the top it is cut off there.
    let lo = 0;
    let hi = 0;
    data.models.forEach((model) => {
      const series = q.series[model.id];
      if (hidden.has(model.id) || !series || !series.d.length) return;
      lo = Math.min(lo, Math.min.apply(null, series[metric]));
      hi = Math.max(hi, Math.max.apply(null, series[metric]));
    });
    const axis = fitAxis(lo, Math.max(hi, lo + spec.span), spec.steps, spec.intervals);
    const X = (day) => x0 + (day / q.day) * (x1 - x0);
    const Y = (value) => y1 - ((clamp(value, axis.lo, axis.hi) - axis.lo) / (axis.hi - axis.lo)) * (y1 - y0);

    const svg = s('svg', {
      viewBox: '0 0 ' + width + ' ' + height,
      role: 'img',
      class: narrow ? 'is-narrow' : '',
      'aria-label': spec.label + ' for each agent, from ' + shortDate(0) + ' to ' + shortDate(q.day)
        + '. The values for the chosen day are listed below the chart.',
    });

    const defs = s('defs');
    const past = s('rect', { x: 0, y: 0, width: 0, height: height });
    const future = s('rect', { x: 0, y: 0, width: 0, height: height });
    const pastClip = s('clipPath', { id: 'fq-clip-past' });
    const futureClip = s('clipPath', { id: 'fq-clip-future' });
    pastClip.appendChild(past);
    futureClip.appendChild(future);
    defs.append(pastClip, futureClip);
    svg.appendChild(defs);

    axis.ticks.forEach((tick) => {
      const y = Math.round(Y(tick)) + 0.5;
      svg.appendChild(s('line', { class: 'fq-grid' + (tick === 0 ? ' is-zero' : ''), x1: x0, x2: x1, y1: y, y2: y }));
      const label = s('text', { class: 'fq-tick', x: x0 - 9, y: y, dy: '0.32em', 'text-anchor': 'end' });
      label.textContent = spec.tick(tick);
      svg.appendChild(label);
    });

    const maxTicks = narrow ? 4 : 7;
    const stepDays = [1, 2, 3, 7, 14, 21, 28].find((size) => Math.floor(q.day / size) + 1 <= maxTicks) || 28;
    for (let day = 0; day <= q.day; day += stepDays) {
      const x = Math.round(X(day)) + 0.5;
      svg.appendChild(s('line', { class: 'fq-xtick', x1: x, x2: x, y1: y1, y2: y1 + 5 }));
      const label = s('text', { class: 'fq-tick', x: x, y: y1 + 22, 'text-anchor': 'middle' });
      label.textContent = shortDate(day);
      svg.appendChild(label);
    }

    const layer = s('g');
    const groups = {};
    const dots = {};
    const ends = {};
    const playhead = s('line', { class: 'fq-playhead', y1: y0 - 4, y2: y1 });
    const endLayer = s('g', { class: 'fq-ends' });
    const hoverLayer = s('g', { class: 'fq-hover' });
    const cross = s('line', { class: 'fq-cross', y1: y0 - 4, y2: y1 });
    hoverLayer.appendChild(cross);
    data.models.forEach((model) => {
      const series = q.series[model.id];
      if (hidden.has(model.id) || !series || !series.d.length) return;
      const group = s('g', { class: 'fq-series' });
      if (metric === 'p' && series.hi.some((value, i) => value - series.lo[i] > 0.004)) {
        group.appendChild(s('path', { class: 'fq-band', fill: model.color, d: bandPath(series.d, series.lo, series.hi, X, Y, q.day) }));
      }
      const path = stepPath(series.d, series[metric], X, Y, q.day);
      group.appendChild(s('path', { class: 'fq-line', stroke: model.color, d: path, 'clip-path': 'url(#fq-clip-past)' }));
      group.appendChild(s('path', { class: 'fq-line is-future', stroke: model.color, d: path, 'clip-path': 'url(#fq-clip-future)' }));
      layer.appendChild(group);
      groups[model.id] = group;

      // Where the line has got to: a dot on it, tied to the maker's logo and the value.
      const end = s('g', { class: 'fq-end' });
      const leader = s('path', { class: 'fq-leader', stroke: model.color });
      const dot = s('circle', { class: 'fq-end-dot', r: narrow ? 4 : 4.5, fill: model.color });
      const mark = s('g');
      mark.appendChild(s('circle', { class: 'fq-end-ring', r: ring, stroke: model.color }));
      if (LOGOS[model.vendor]) {
        const size = ring * 1.2;
        mark.appendChild(s('image', { href: logoBase + LOGOS[model.vendor], x: -size / 2, y: -size / 2, width: size, height: size }));
      }
      const value = s('text', { class: 'fq-end-value', x: ring + (narrow ? 5 : 7), dy: '0.35em' });
      mark.appendChild(value);
      end.append(leader, dot, mark);
      end.addEventListener('pointerenter', () => emphasize(model.id));
      end.addEventListener('pointerleave', () => emphasize(null));
      endLayer.appendChild(end);
      ends[model.id] = { group: end, leader: leader, dot: dot, mark: mark, value: value };

      const hoverDot = s('circle', { r: narrow ? 4.5 : 5, fill: model.color });
      hoverLayer.appendChild(hoverDot);
      dots[model.id] = hoverDot;
    });
    svg.append(layer, playhead, endLayer, hoverLayer);

    chart = {
      q: q, width: width, height: height, x0: x0, x1: x1, y0: y0, y1: y1, X: X, Y: Y, ring: ring, reach: reach,
      svg: svg, past: past, future: future, playhead: playhead, cross: cross, hover: hoverLayer,
      layer: layer, groups: groups, dots: dots, ends: ends,
    };
    dlg.plot.replaceChildren(svg, dlg.tip);

    Object.keys(dlg.metricButtons).forEach((key) => {
      dlg.metricButtons[key].setAttribute('aria-pressed', key === metric ? 'true' : 'false');
    });
    data.models.forEach((model) => {
      const button = dlg.legendButtons[model.id];
      button.setAttribute('aria-pressed', hidden.has(model.id) ? 'false' : 'true');
      button.title = hidden.has(model.id) ? HINTS.show : HINTS.hide;
    });
    dlg.note.textContent = spec.note;
    dlg.scrub.style.setProperty('--fq-pad-left', f(x0) + 'px');
    dlg.scrub.style.setProperty('--fq-pad-right', f(width - x1) + 'px');
    updateDay();
  }

  function dayAt(event) {
    const rect = chart.svg.getBoundingClientRect();
    const px = (event.clientX - rect.left) * (rect.width ? chart.width / rect.width : 1);
    return clamp(Math.round(((px - chart.x0) / (chart.x1 - chart.x0)) * chart.q.day), 0, chart.q.day);
  }

  function setPin(day) {
    stopAnim();
    pin = day;
    clip = day;
    updateDay();
  }

  /* The badges ride on the chosen day (and on the playhead during a replay), each beside its
   * line's value there, and are spread apart where the lines run together. The playhead marks
   * a chosen day before the resolution; on the resolution day the lines simply end. */
  function placeEnds() {
    const q = current;
    const at = anim && anim.replay ? clip : pin;
    const day = Math.floor(at + 1e-6);
    const x = chart.X(at);
    chart.playhead.setAttribute('x1', f(x));
    chart.playhead.setAttribute('x2', f(x));
    chart.playhead.setAttribute('visibility', at >= q.day ? 'hidden' : 'visible');
    const shown = [];
    data.models.forEach((model) => {
      const end = chart.ends[model.id];
      if (!end) return;
      const series = q.series[model.id];
      const i = stepIndex(series.d, day);
      end.group.setAttribute('visibility', i < 0 ? 'hidden' : 'visible');
      if (i >= 0) shown.push({ end: end, value: series[metric][i] });
    });
    const centres = spread(shown.map((item) => chart.Y(item.value)), chart.ring * 2 + 3, chart.y0, chart.y1 - 4);
    const badgeX = x + chart.reach;
    shown.forEach((item, k) => {
      const y = chart.Y(item.value);
      item.end.dot.setAttribute('cx', f(x));
      item.end.dot.setAttribute('cy', f(y));
      item.end.leader.setAttribute('d', 'M' + f(x) + ' ' + f(y) + 'L' + f(badgeX - chart.ring) + ' ' + f(centres[k]));
      item.end.mark.setAttribute('transform', 'translate(' + f(badgeX) + ' ' + f(centres[k]) + ')');
      item.end.value.textContent = metric === 'p' ? fmtP(item.value) : fmtB(item.value);
    });
  }

  /* Moves the clip, the badges, the crosshair, the scrubber and the panel to the current state. */
  function updateDay() {
    if (!chart || !current) return;
    const q = current;
    const edge = chart.X(clip) + 2;
    chart.past.setAttribute('width', f(edge));
    chart.future.setAttribute('x', f(edge));
    chart.future.setAttribute('width', f(Math.max(0, chart.width - edge)));
    placeEnds();

    chart.hover.setAttribute('visibility', hover == null ? 'hidden' : 'visible');
    if (hover != null) {
      const x = f(chart.X(hover));
      chart.cross.setAttribute('x1', x);
      chart.cross.setAttribute('x2', x);
      data.models.forEach((model) => {
        const dot = chart.dots[model.id];
        if (!dot) return;
        const series = q.series[model.id];
        const i = stepIndex(series.d, hover);
        dot.setAttribute('visibility', i < 0 ? 'hidden' : 'inherit');
        if (i < 0) return;
        dot.setAttribute('cx', x);
        dot.setAttribute('cy', f(chart.Y(series[metric][i])));
      });
    }

    dlg.range.value = String(pin);
    dlg.range.setAttribute('aria-valuetext', longDate(pin));
    dlg.date.textContent = shortDate(pin);
    const replaying = !!(anim && anim.replay);
    const action = replaying ? 'Pause' : pin >= q.day ? 'Replay' : 'Play';
    dlg.playIcon.firstChild.setAttribute('href', iconBase + '#qi-' + action.toLowerCase());
    dlg.playLabel.textContent = action;
    dlg.play.title = action;
    dlg.scrub.style.setProperty('--fq-progress', f((pin / q.day) * 100) + '%');
    renderPanel(false);
    renderTip();
  }

  function renderTip() {
    if (hover == null || !chart || !current) {
      dlg.tip.hidden = true;
      return;
    }
    const q = current;
    dlg.tipDate.textContent = longDate(hover);
    data.models.forEach((model) => {
      const entry = dlg.tipValues[model.id];
      const series = q.series[model.id];
      entry.row.hidden = hidden.has(model.id) || !series;
      if (entry.row.hidden) return;
      const i = stepIndex(series.d, hover);
      entry.value.textContent = i < 0 ? 'no forecast' : metric === 'p' ? fmtP(series.p[i]) : fmtB(series.b[i]);
      entry.value.classList.toggle('is-none', i < 0);
    });
    dlg.tip.hidden = false;
    const rect = chart.svg.getBoundingClientRect();
    const scale = rect.width ? rect.width / chart.width : 1;
    const x = chart.X(hover) * scale;
    const tipWidth = dlg.tip.offsetWidth;
    const left = x + 14 + tipWidth <= rect.width ? x + 14 : x - 14 - tipWidth;
    dlg.tip.style.left = f(clamp(left, 4, Math.max(4, rect.width - tipWidth - 4))) + 'px';
    dlg.tip.style.top = f(chart.y0 + 6) + 'px';
  }

  function renderPanel(force) {
    const q = current;
    if (!q) return;
    dlg.dayLabel.textContent = longDate(pin) + (pin === q.day ? ' (the day it resolved)' : '');
    const indices = data.models.map((model) => {
      const series = q.series[model.id];
      return hidden.has(model.id) ? 'x' : series ? stepIndex(series.d, pin) : -1;
    });
    const key = q.id + '|' + metric + '|' + indices.join(',');
    if (!force && key === panelKey) return;
    panelKey = key;

    dlg.dayGrid.replaceChildren();
    data.models.forEach((model, m) => {
      if (hidden.has(model.id)) return;
      const series = q.series[model.id];
      const i = indices[m];
      const card = h('article', 'fq-agent');
      const head = h('div', 'fq-agent-head');
      head.append(badge(model), h('span', 'fq-agent-name', model.name));
      card.appendChild(head);
      card.addEventListener('pointerenter', () => emphasize(model.id));
      card.addEventListener('pointerleave', () => emphasize(null));

      if (i < 0) {
        card.appendChild(h('p', 'fq-agent-empty', 'No forecast yet'));
        dlg.dayGrid.appendChild(card);
        return;
      }
      // One line of context. The probability itself is the answer's bar below.
      let runs = 'Brier skill ' + fmtB(series.b[i]) + (model.seeds > 1 ? ', mean of ' + plural(model.seeds, 'run') : '');
      if (metric === 'p') runs = '1 run';
      if (metric === 'p' && model.seeds > 1) {
        runs = fmtP(series.lo[i]) === fmtP(series.hi[i])
          ? plural(model.seeds, 'run') + ', all at ' + fmtP(series.p[i])
          : plural(model.seeds, 'run') + ', ' + fmtP(series.lo[i]) + ' to ' + fmtP(series.hi[i]);
      }
      card.appendChild(h('p', 'fq-agent-runs', runs));

      // The answer is always listed, next to the agent's three most likely other outcomes.
      const rows = (series.o[i] || []).slice().sort((a, b) => b[1] - a[1]);
      const answer = rows.find((row) => row[0] === 0) || [0, series.p[i]];
      const shown = rows.filter((row) => row[0] !== 0).slice(0, 3).concat([answer]).sort((a, b) => b[1] - a[1]);
      const list = h('ol', 'fq-outcomes');
      shown.forEach((row) => {
        const isAnswer = row[0] === 0;
        const item = h('li', 'fq-outcome' + (isAnswer ? ' is-answer' : ''));
        const name = h('span', 'fq-outcome-name');
        const text = q.labels[row[0]] || '';
        if (isAnswer) name.appendChild(icon('check'));
        const label = h('span', null, text);
        label.title = text;
        name.appendChild(label);
        const track = h('span', 'fq-outcome-track');
        const fill = h('span', 'fq-outcome-fill');
        fill.style.width = f(clamp(row[1], 0, 1) * 100) + '%';
        if (row[1] <= 0) fill.hidden = true;
        track.appendChild(fill);
        item.append(name, h('span', 'fq-outcome-value', fmtP(row[1])), track);
        list.appendChild(item);
      });
      card.appendChild(list);
      dlg.dayGrid.appendChild(card);
    });
  }

  function emphasize(id) {
    if (!chart) return;
    if (id != null && !chart.groups[id]) id = null;
    data.models.forEach((model) => {
      const group = chart.groups[model.id];
      if (!group) return;
      group.classList.toggle('is-emphasized', id === model.id);
      group.classList.toggle('is-dimmed', id != null && id !== model.id);
      chart.dots[model.id].classList.toggle('is-dimmed', id != null && id !== model.id);
      chart.ends[model.id].group.classList.toggle('is-dimmed', id != null && id !== model.id);
      if (id == null) chart.layer.appendChild(group);
    });
    if (id != null) chart.layer.appendChild(chart.groups[id]);
  }

  function stopAnim() {
    if (!anim) return;
    cancelAnimationFrame(anim.raf);
    anim = null;
    dlg.el.classList.remove('is-drawing', 'is-replaying');
    clip = pin;
    updateDay();
  }

  /* The lines draw in from the left when a question opens. */
  function drawIn() {
    if (reduceMotion || !current) return;
    const q = current;
    const duration = 850;
    let started = null;
    anim = { raf: 0, replay: false };
    dlg.el.classList.add('is-drawing');
    clip = 0;
    updateDay();
    const tick = (now) => {
      if (!anim) return;
      if (started == null) started = now;
      const k = Math.min(1, (now - started) / duration);
      clip = (1 - Math.pow(1 - k, 3)) * q.day;
      updateDay();
      if (k < 1) anim.raf = requestAnimationFrame(tick);
      else stopAnim();
    };
    anim.raf = requestAnimationFrame(tick);
  }

  /* Replay walks the chosen day from the start of the simulation to the resolution day. */
  function togglePlay() {
    if (!current) return;
    if (anim && anim.replay) {
      stopAnim();
      return;
    }
    stopAnim();
    const q = current;
    const from = pin >= q.day ? 0 : pin;
    const duration = clamp(q.day * 70, 2600, 7000) * ((q.day - from) / q.day);
    let started = null;
    hover = null;
    anim = { raf: 0, replay: true };
    dlg.el.classList.add('is-replaying');
    pin = from;
    clip = from;
    updateDay();
    const tick = (now) => {
      if (!anim) return;
      if (started == null) started = now;
      const k = Math.min(1, (now - started) / duration);
      clip = from + k * (q.day - from);
      pin = Math.floor(clip + 1e-6);
      updateDay();
      if (k < 1) anim.raf = requestAnimationFrame(tick);
      else stopAnim();
    };
    anim.raf = requestAnimationFrame(tick);
  }

  function openQuestion(q) {
    stopAnim();
    current = q;
    pin = q.day;
    clip = q.day;
    hover = null;
    dragging = false;
    fillDialog(q);
    if (!dlg.el.open) {
      if (typeof dlg.el.showModal === 'function') dlg.el.showModal();
      else dlg.el.setAttribute('open', '');
      document.documentElement.classList.add('fq-lock');
      // Start on the dialog itself, so no button is ringed before the reader has pressed a key.
      dlg.el.focus({ preventScroll: true });
    }
    dlg.body.scrollTop = 0;
    dlg.el.scrollTop = 0;
    renderChart();
    renderPanel(true);
    drawIn();
  }

  /* Routing: #q-<id> opens that question ----------------------------------- */

  function hashId() {
    const match = /^#q-([\w-]+)$/.exec(location.hash);
    return match ? match[1] : null;
  }

  function navigate(q, push) {
    const url = '#q-' + q.id;
    if (push) history.pushState({ fq: true }, '', url);
    else history.replaceState(history.state, '', url);
    openQuestion(q);
  }

  function syncFromHash() {
    const q = byId[hashId()];
    if (q) {
      if (current !== q || !dlg.el.open) openQuestion(q);
    } else if (dlg.el.open) {
      dlg.el.close();
    }
  }

  /* Start ------------------------------------------------------------------- */

  function start() {
    prepare();
    buildDialog();
    buildMosaic();

    // The Cards view is switched off for now; the mosaic is the only view. To bring it back,
    // un-comment these lines and the two commented blocks of markup in
    // _includes/futuresim-questions.html.
    // renderFilters();
    // renderKey();
    // data.questions.forEach(buildCard);
    // applyFilters();
    // root.querySelectorAll('[data-fq-view]').forEach((button) => {
    //   button.addEventListener('click', () => setView(button.getAttribute('data-fq-view')));
    // });
    // els.search.addEventListener('input', () => {
    //   query = els.search.value;
    //   applyFilters();
    // });
    // els.sort.addEventListener('change', () => {
    //   sort = els.sort.value;
    //   applyFilters();
    // });

    window.addEventListener('popstate', syncFromHash);
    window.addEventListener('hashchange', syncFromHash);
    // A page opened on a question (#q-<id>) starts at this section, so that closing the question
    // leaves the reader at the mosaic and not at the top of the page.
    if (byId[hashId()]) root.scrollIntoView({ behavior: 'instant', block: 'start' });
    syncFromHash();
  }

  fetch(root.getAttribute('data-src'))
    .then((response) => {
      if (!response.ok) throw new Error('HTTP ' + response.status);
      return response.json();
    })
    .then((json) => {
      data = json;
      start();
    })
    .catch((error) => {
      if (window.console) console.error('FutureSim questions:', error);
      const failed = 'The questions could not be loaded. Reload the page to try again.';
      els.mosaic.replaceChildren(h('p', 'fq-empty', failed));
      if (els.list) els.list.replaceChildren(h('li', 'fq-empty', failed));
    });
})();
