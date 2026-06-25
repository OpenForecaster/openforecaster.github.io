(function () {
  const root = document.querySelector('[data-futuresim-leaderboard]');
  if (!root) return;

  const dataBase = (window.FSIM_TRACE_DATA_BASE || '/futuresim/traces/data/').replace(/\/?$/, '/');
  const chart = root.querySelector('[data-futuresim-leaderboard-chart]');
  const buttons = root.querySelectorAll('[data-futuresim-metric]');
  const colors = ['#0f766e', '#2563eb', '#b45309', '#9333ea', '#be123c', '#047857', '#4f46e5', '#a16207', '#0e7490'];
  let leaderboard = null;
  let metric = 'brier_skill_score';

  async function init() {
    try {
      const response = await fetch(dataBase + 'leaderboard.json', { cache: 'no-store' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      leaderboard = await response.json();
      for (const button of buttons) {
        button.addEventListener('click', () => {
          metric = button.dataset.futuresimMetric;
          for (const item of buttons) item.setAttribute('aria-pressed', String(item === button));
          render();
        });
      }
      render();
    } catch (error) {
      chart.textContent = `Could not load official metrics (${error.message}).`;
    }
  }

  function render() {
    const series = modelSeries(metric);
    chart.replaceChildren();
    if (!series.length) {
      chart.textContent = 'No official run metrics available.';
      return;
    }

    const all = series.flatMap((item) => item.values.flatMap((point) => [point.mean - point.std, point.mean + point.std]));
    const allDays = series.flatMap((item) => item.values.map((point) => point.day));
    const minDay = Math.min(...allDays);
    const maxDay = Math.max(...allDays);
    let minValue = Math.min(...all);
    let maxValue = Math.max(...all);
    const pad = Math.max((maxValue - minValue) * 0.08, metric === 'top1_accuracy' ? 1 : 0.01);
    minValue -= pad;
    maxValue += pad;

    const width = 720;
    const height = 330;
    const margin = { top: 22, right: 12, bottom: 32, left: 58 };
    const plotW = width - margin.left - margin.right;
    const plotH = height - margin.top - margin.bottom;
    const x = (day) => margin.left + (maxDay === minDay ? plotW / 2 : (day - minDay) / (maxDay - minDay) * plotW);
    const y = (value) => margin.top + (maxValue === minValue ? plotH / 2 : (maxValue - value) / (maxValue - minValue) * plotH);

    const tooltip = document.createElement('div');
    tooltip.className = 'futuresim-leaderboard-tooltip';
    chart.appendChild(tooltip);

    const svg = svgEl('svg', { viewBox: `0 0 ${width} ${height}`, role: 'img', 'aria-label': `Current leaderboard ${label(metric)}` });
    for (const tick of valueTicks(minValue, maxValue, 5)) {
      svg.appendChild(svgEl('line', { x1: margin.left, x2: width - margin.right, y1: y(tick), y2: y(tick), class: 'futuresim-leaderboard-grid' }));
      const node = svgEl('text', { x: margin.left - 9, y: y(tick) + 4, 'text-anchor': 'end', class: 'futuresim-leaderboard-axis-label' });
      node.textContent = format(tick, metric);
      svg.appendChild(node);
    }
    for (const tick of dayTicks(minDay, maxDay, 5)) {
      const node = svgEl('text', { x: x(tick), y: height - 12, 'text-anchor': 'middle', class: 'futuresim-leaderboard-axis-label' });
      node.textContent = tick === 0 ? 'Day 0' : `Day ${tick}`;
      svg.appendChild(node);
    }
    svg.appendChild(svgEl('line', { x1: margin.left, x2: width - margin.right, y1: height - margin.bottom, y2: height - margin.bottom, class: 'futuresim-leaderboard-axis' }));
    svg.appendChild(svgEl('line', { x1: margin.left, x2: margin.left, y1: margin.top, y2: height - margin.bottom, class: 'futuresim-leaderboard-axis' }));

    for (const item of series) {
      const bandTop = item.values.map((point, index) => `${index ? 'L' : 'M'}${x(point.day).toFixed(1)},${y(point.mean + point.std).toFixed(1)}`);
      const bandBottom = item.values.slice().reverse().map((point) => `L${x(point.day).toFixed(1)},${y(point.mean - point.std).toFixed(1)}`);
      svg.appendChild(svgEl('path', { d: `${bandTop.join(' ')} ${bandBottom.join(' ')} Z`, fill: item.color, class: 'futuresim-leaderboard-band' }));
      svg.appendChild(svgEl('path', { d: item.values.map((point, index) => `${index ? 'L' : 'M'}${x(point.day).toFixed(1)},${y(point.mean).toFixed(1)}`).join(' '), stroke: item.color, class: 'futuresim-leaderboard-line' }));

      const last = item.values[item.values.length - 1];
      const labelNode = svgEl('text', { x: x(last.day) - 4, y: y(last.mean) - 7, 'text-anchor': 'end', fill: item.color, class: 'futuresim-leaderboard-series-label' });
      labelNode.textContent = item.name;
      svg.appendChild(labelNode);

      for (const point of item.values) {
        const hit = svgEl('circle', { cx: x(point.day), cy: y(point.mean), r: 8, class: 'futuresim-leaderboard-hit', tabindex: '0' });
        hit.addEventListener('mouseenter', () => showTooltip(tooltip, item, point, x(point.day), y(point.mean), width));
        hit.addEventListener('mousemove', () => showTooltip(tooltip, item, point, x(point.day), y(point.mean), width));
        hit.addEventListener('mouseleave', () => tooltip.classList.remove('is-visible'));
        hit.addEventListener('focus', () => showTooltip(tooltip, item, point, x(point.day), y(point.mean), width));
        hit.addEventListener('blur', () => tooltip.classList.remove('is-visible'));
        svg.appendChild(hit);
      }
    }
    chart.appendChild(svg);
  }

  function modelSeries(metricName) {
    return (leaderboard.models || []).map((model, index) => {
      const values = (model.points || []).map((point) => ({
        date: point.date,
        day: dayIndex(point.date),
        mean: Number(point[`${metricName}_mean`]),
        std: Number(point[`${metricName}_std`]),
        n: point.seed_count,
        questionCount: point.question_count,
      })).filter((point) => Number.isFinite(point.mean) && Number.isFinite(point.std));
      return { name: model.agent_name, color: colors[index % colors.length], seedCount: model.seed_count, values };
    }).filter((item) => item.values.length);
  }

  function showTooltip(tooltip, item, point, x, y, width) {
    tooltip.replaceChildren();
    tooltip.appendChild(el('strong', item.name));
    tooltip.appendChild(el('span', point.date));
    tooltip.appendChild(el('span', `${label(metric)}: ${format(point.mean, metric)} +/- ${format(point.std, metric)}`));
    tooltip.appendChild(el('span', `${point.n} seed${point.n === 1 ? '' : 's'} x ${point.questionCount} questions`));
    tooltip.style.left = `${x / width * 100}%`;
    tooltip.style.top = `${y / 330 * 100}%`;
    tooltip.classList.toggle('is-right', x > width - 190);
    tooltip.classList.add('is-visible');
  }

  function dayIndex(date) {
    return Math.round((Date.parse(`${date}T00:00:00Z`) - Date.UTC(2025, 11, 24)) / 86400000);
  }

  function valueTicks(min, max, count) {
    const ticks = [];
    for (let i = 0; i < count; i += 1) ticks.push(min + (max - min) * i / (count - 1));
    return ticks;
  }

  function dayTicks(min, max, count) {
    const ticks = [];
    for (let i = 0; i < count; i += 1) ticks.push(Math.round(min + (max - min) * i / (count - 1)));
    return [...new Set(ticks)];
  }

  function label(metricName) {
    return metricName === 'top1_accuracy' ? 'Top 1 accuracy' : 'Brier skill score';
  }

  function format(value, metricName) {
    return metricName === 'top1_accuracy' ? `${value.toFixed(1)}%` : value.toFixed(3);
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

  init();
})();
