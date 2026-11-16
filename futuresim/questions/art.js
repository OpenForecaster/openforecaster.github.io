/* Pictograms for the mosaic in the FutureSim Questions section: one per question, drawn in white on
 * the colour of the question's category. A pictogram shows what the question is about and never how
 * it resolved. questions.js reads window.FQ_ART; a question that has no drawing of its own gets its
 * category's.
 *
 * Every drawing is the inside of an <svg viewBox="0 0 300 200">, built from the classes below
 * (styled under .fq-art in questions.css):
 *   a  solid white      b  white at 55%      c  white at 26%
 *   k  the tile's own colour, for details cut out of a white shape
 *   s  7px line   u  4px line   t  4px line at 60%   n  2.5px line at 60%   w  11px line
 *   ks, kn, ko    5px, 2.5px and 15px lines in the tile's colour
 * Two translucent shapes never overlap, so no drawing shows a seam.
 */
(function () {
  'use strict';

  const f = (value) => String(Math.round(value * 100) / 100);
  const P = (cls, d, more) => '<path class="' + cls + '" d="' + d + '"' + (more || '') + '/>';
  const C = (cls, cx, cy, r) => '<circle class="' + cls + '" cx="' + f(cx) + '" cy="' + f(cy) + '" r="' + r + '"/>';
  const E = (cls, cx, cy, rx, ry, turn) => '<ellipse class="' + cls + '" cx="' + f(cx) + '" cy="' + f(cy) + '" rx="' + rx + '" ry="' + ry + '"'
    + (turn ? ' transform="rotate(' + f(turn) + ' ' + f(cx) + ' ' + f(cy) + ')"' : '') + '/>';
  const R = (cls, x, y, w, h, r) => '<rect class="' + cls + '" x="' + f(x) + '" y="' + f(y) + '" width="' + w + '" height="' + h + '"'
    + (r ? ' rx="' + r + '"' : '') + '/>';
  const L = (cls, x1, y1, x2, y2) => '<line class="' + cls + '" x1="' + f(x1) + '" y1="' + f(y1) + '" x2="' + f(x2) + '" y2="' + f(y2) + '"/>';
  const G = (transform, parts) => '<g transform="' + transform + '">' + parts.join('') + '</g>';
  const each = (n, draw) => Array.from({ length: n }, (_, i) => draw(i)).join('');
  // A point at `deg` degrees anticlockwise from three o'clock, as on a compass rose.
  const polar = (cx, cy, r, deg) => [cx + r * Math.cos(deg * Math.PI / 180), cy - r * Math.sin(deg * Math.PI / 180)];
  const points = (list) => list.map((p) => f(p[0]) + ' ' + f(p[1])).join(' ');

  // Part of a circle, anticlockwise from `from` to `to` degrees.
  function arc(cls, cx, cy, r, from, to) {
    return P(cls, 'M' + points([polar(cx, cy, r, from)]) + 'A' + r + ' ' + r + ' 0 0 0 ' + points([polar(cx, cy, r, to)]));
  }

  function ngon(cls, cx, cy, r, n, turn) {
    return '<polygon class="' + cls + '" points="' + points(Array.from({ length: n }, (_, i) => polar(cx, cy, r, (turn || 0) + i * 360 / n))) + '"/>';
  }

  function star(cls, cx, cy, r) {
    return '<polygon class="' + cls + '" points="'
      + points(Array.from({ length: 10 }, (_, i) => polar(cx, cy, i % 2 ? r * 0.42 : r, 90 + i * 36))) + '"/>';
  }

  // A four-pointed glint.
  function glint(cls, cx, cy, r) {
    const q = 'Q' + cx + ' ' + cy + ' ';
    return P(cls, 'M' + cx + ' ' + (cy - r) + q + (cx + r) + ' ' + cy + q + cx + ' ' + (cy + r) + q + (cx - r) + ' ' + cy + q + cx + ' ' + (cy - r) + 'Z');
  }

  function wave(cls, x, y, n) {
    return P(cls, 'M' + x + ' ' + y + 'q6 -6 12 0t12 0'.repeat(n));
  }

  // A closed curve through the given points.
  function blob(cls, list) {
    const n = list.length;
    let d = 'M' + f(list[0][0]) + ' ' + f(list[0][1]);
    for (let i = 0; i < n; i++) {
      const p0 = list[(i + n - 1) % n];
      const p1 = list[i];
      const p2 = list[(i + 1) % n];
      const p3 = list[(i + 2) % n];
      d += 'C' + f(p1[0] + (p2[0] - p0[0]) / 6) + ' ' + f(p1[1] + (p2[1] - p0[1]) / 6)
        + ' ' + f(p2[0] - (p3[0] - p1[0]) / 6) + ' ' + f(p2[1] - (p3[1] - p1[1]) / 6)
        + ' ' + f(p2[0]) + ' ' + f(p2[1]);
    }
    return P(cls, d + 'Z');
  }

  function football(cx, cy, r) {
    return C('a', cx, cy, r) + ngon('k', cx, cy, r * 0.38, 5, 90)
      + each(5, (i) => {
        const from = polar(cx, cy, r * 0.38, 90 + i * 72);
        const to = polar(cx, cy, r * 0.96, 90 + i * 72);
        return L('kn', from[0], from[1], to[0], to[1]);
      });
  }

  function pin(cx, cy, r) {
    return P('a', 'M' + cx + ' ' + (cy + r * 1.75) + 'C' + cx + ' ' + (cy + r * 1.75) + ' ' + (cx - r) + ' ' + (cy + r * 0.7) + ' ' + (cx - r) + ' ' + cy
      + 'A' + r + ' ' + r + ' 0 1 1 ' + (cx + r) + ' ' + cy
      + 'C' + (cx + r) + ' ' + (cy + r * 0.7) + ' ' + cx + ' ' + (cy + r * 1.75) + ' ' + cx + ' ' + (cy + r * 1.75) + 'Z')
      + C('k', cx, cy, r * 0.38);
  }

  // An aircraft seen from above, nose to the right, about 50 wide.
  const AIRLINER = [
    P('a', 'M-24 -3.5H14Q24 0 14 3.5H-24Z'),
    P('a', 'M7 -3L-8 -22H-15L-6 -3Z'), P('a', 'M7 3L-8 22H-15L-6 3Z'),
    P('a', 'M-16 -3L-22 -11H-27L-24 -3Z'), P('a', 'M-16 3L-22 11H-27L-24 3Z'),
  ];

  function ballotBox(x, y) {
    return R('b', x + 26, y - 38, 30, 46, 3) + P('ks', 'M' + (x + 33) + ' ' + (y - 19) + 'l6 7l11 -14')
      + R('a', x, y, 84, 60, 6) + R('k', x + 19, y + 13, 46, 7, 3.5);
  }

  // Two branches meeting under the subject. Drawn solid and faded as one group, so stem and leaves
  // do not show where they overlap.
  function laurel(cx, cy, r) {
    const branch = (dir) => {
      const x = (px) => (dir < 0 ? px : 2 * cx - px);
      const leaf = (angle, tilt) => {
        const base = polar(cx, cy, r, angle);
        const turn = 180 - angle - tilt;
        const rad = turn * Math.PI / 180;
        return E('a', x(base[0] + 11 * Math.sin(rad)), base[1] - 11 * Math.cos(rad), 5, 12.5, dir < 0 ? turn : -turn);
      };
      const from = polar(cx, cy, r, 262);
      const to = polar(cx, cy, r, 118);
      return P('u', 'M' + f(x(from[0])) + ' ' + f(from[1]) + 'A' + r + ' ' + r + ' 0 0 ' + (dir < 0 ? 1 : 0) + ' ' + f(x(to[0])) + ' ' + f(to[1]))
        + each(6, (i) => leaf(238 - i * 21, 40) + leaf(238 - i * 21, -40)) + leaf(118, 0);
    };
    return '<g opacity=".6">' + branch(-1) + branch(1) + '</g>';
  }

  // A television showing a theatre mask; the two Emmy questions differ in the mask's face.
  function televisedMask(face) {
    return [
      L('u', 150, 46, 126, 20), L('u', 150, 46, 174, 20),
      R('a', 64, 46, 172, 112, 14), R('k', 76, 58, 148, 88, 7),
      L('s', 104, 160, 96, 176), L('s', 196, 160, 204, 176),
      P('a', 'M120 66Q150 76 180 66V100C180 124 165 138 150 138C135 138 120 124 120 100Z'),
    ].concat(face);
  }

  const ART = {
    /* Geopolitics ---------------------------------------------------------- */

    // Ukraine's next top commander: an officer's cap over a row of rank stars.
    249565: [
      P('a', 'M72 92Q150 34 228 92L212 112H88Z'),
      R('b', 88, 112, 124, 14),
      P('a', 'M96 126H204Q200 152 150 152Q100 152 96 126Z'),
      C('k', 150, 86, 12), star('a', 150, 86, 8),
      [108, 136, 164, 192].map((x) => star('b', x, 176, 9)).join(''),
    ],
    // A US strike on Iran-aligned groups: a jet closing on a target.
    339902: [
      C('s', 180, 112, 46), C('t', 180, 112, 22), C('a', 180, 112, 6),
      L('s', 180, 52, 180, 78), L('s', 180, 146, 180, 172), L('s', 120, 112, 146, 112), L('s', 214, 112, 240, 112),
      G('translate(88 62) rotate(33) scale(.82)', [
        P('a', 'M-42 -5H22Q40 0 22 5H-42Z'),
        P('a', 'M12 -5L-18 -36H-30L-10 -5Z'), P('a', 'M12 5L-18 36H-30L-10 5Z'),
        P('a', 'M-30 -5L-42 -18H-49L-42 -5Z'), P('a', 'M-30 5L-42 18H-49L-42 5Z'),
      ]),
    ],
    // The Security Council's straw poll: fifteen seats in a horseshoe around a ballot.
    238968: [
      each(15, (i) => {
        const at = polar(150, 116, 76, -30 + i * 240 / 14);
        return C('b', at[0], at[1], 7);
      }),
      R('a', 126, 82, 48, 62, 5), P('ks', 'M138 114l9 10l17 -22'),
    ],
    // Clearing the Strait of Hormuz: a moored sea mine under the waves.
    817209: [
      wave('t', 54, 28, 8), wave('t', 66, 42, 7),
      each(8, (i) => {
        const from = polar(150, 110, 30, 22.5 + i * 45);
        const to = polar(150, 110, 50, 22.5 + i * 45);
        return L('s', from[0], from[1], to[0], to[1]) + C('a', to[0], to[1], 6);
      }),
      C('a', 150, 110, 34), P('ks', 'M133 100a20 20 0 0 1 13 -11'),
      E('t', 150, 160, 5, 8), E('t', 150, 176, 5, 8), E('t', 150, 192, 5, 8),
    ],
    // Recognising sovereignty over the Golan Heights: a flag planted on a plateau.
    112235: [
      P('b', 'M20 178L92 92L128 128H40ZM176 128L204 76L282 178H236L190 128Z'),
      P('a', 'M34 178L88 128H190L244 178Z'),
      L('s', 138, 128, 138, 42), P('a', 'M138 44H196L184 62L196 80H138Z'),
    ],
    // Xi Jinping's first Middle East visit of the year: a flight to a place on the map.
    834692: [
      P('c', 'M20 186Q84 134 150 172Q212 144 280 186Z'),
      P('t', 'M54 134Q104 40 184 66', ' stroke-dasharray="0.1 11"'),
      G('translate(107 73) rotate(-31) scale(1.45)', AIRLINER),
      pin(216, 88, 30),
    ],
    // Putin's counterpart at the SCO summit: two chairs set for bilateral talks.
    921981: [
      P('b', 'M128 34L96 40L100 62L133 55Z'), P('b', 'M172 34L204 40L200 62L167 55Z'),
      L('u', 128, 34, 143, 102), L('u', 172, 34, 157, 102),
      R('a', 58, 74, 14, 62, 6), R('a', 58, 116, 64, 14, 6), L('s', 68, 132, 68, 166), L('s', 112, 132, 112, 166),
      R('a', 228, 74, 14, 62, 6), R('a', 178, 116, 64, 14, 6), L('s', 232, 132, 232, 166), L('s', 188, 132, 188, 166),
      R('a', 130, 104, 40, 8, 4), L('s', 150, 110, 150, 162), R('a', 134, 160, 32, 7, 3),
    ],
    // A venue for three-way ceasefire talks: three seats around a table, pinned on the map.
    174389: [
      C('b', 150, 112, 36),
      [90, 210, 330].map((at) => {
        const seat = polar(150, 112, 57, at);
        return C('a', seat[0], seat[1], 12) + arc('s', 150, 112, 76, at - 17, at + 17);
      }).join(''),
      pin(150, 104, 15),
    ],
    // Weapons in orbit: a satellite in the cross-hairs above the Earth.
    870914: [
      C('b', 92, 176, 72), P('kn', 'M28 150Q92 176 158 146M40 196Q96 214 150 190'),
      P('t', 'M28 86Q160 12 272 118'),
      G('translate(196 68) rotate(22)', [
        R('a', -13, -11, 26, 22, 4), R('a', -52, -8, 32, 16, 2), R('a', 20, -8, 32, 16, 2),
        L('u', 0, 11, 0, 22), C('a', 0, 25, 4),
      ]),
      P('u', 'M146 40V24H162M230 24H246V40M246 96V112H230M162 112H146V96'),
    ],
    // A private request about the Houthis, who threaten Red Sea shipping: a ship and a sealed message.
    56802: [
      R('a', 66, 26, 96, 52, 14), P('a', 'M92 72L86 96L116 76Z'),
      R('k', 104, 50, 20, 16, 3), P('ks', 'M108 50v-4a6 6 0 0 1 12 0v4'),
      R('b', 94, 116, 30, 18, 2), R('b', 128, 116, 30, 18, 2), R('b', 162, 116, 30, 18, 2), R('b', 128, 94, 30, 18, 2),
      R('a', 202, 98, 24, 38, 3),
      P('a', 'M60 138H242L224 166H82Z'),
      wave('t', 42, 184, 9),
    ],

    /* Politics & law ------------------------------------------------------- */

    // A party leader resigning as an MP to fight the by-election: Westminster's clock tower and a ballot box.
    754639: [
      P('a', 'M62 54L86 12L110 54Z'),
      R('a', 64, 54, 44, 44, 2), C('k', 86, 76, 14), P('u', 'M86 76V66M86 76H94'),
      R('a', 70, 98, 32, 80),
      [77, 85, 93].map((x) => R('k', x - 1.5, 110, 3, 56)).join(''),
      ballotBox(150, 116),
    ],
    // Moldova's parliament electing a prime minister: the chamber's benches around a lectern.
    76066: [
      [[50, 5], [76, 8], [102, 11]].map((row) => each(row[1], (i) => {
        const at = polar(150, 156, row[0], 180 * i / (row[1] - 1));
        return C('b', at[0], at[1], 7);
      })).join(''),
      R('a', 130, 122, 40, 8, 3), P('a', 'M135 130H165L160 164H140Z'),
    ],
    // A party primary for the US Senate: a campaign rosette.
    883794: [
      P('a', 'M124 112L104 182L128 168L144 186L156 120Z'), P('a', 'M176 112L196 182L172 168L156 186L144 120Z'),
      each(12, (i) => {
        const at = polar(150, 84, 46, i * 30);
        return C('b', at[0], at[1], 11);
      }),
      C('a', 150, 84, 42), C('k', 150, 84, 32), C('a', 150, 84, 27), star('k', 150, 84, 17),
    ],
    // A nominee to run the Food and Drug Administration: medicines.
    970733: [
      G('translate(112 100) rotate(-38)', [
        P('a', 'M0 -24H-34A24 24 0 0 0 -34 24H0Z'), P('b', 'M0 -24H34A24 24 0 0 1 34 24H0Z'),
      ]),
      C('a', 208, 140, 27), L('ks', 189, 140, 227, 140),
      P('b', 'M214 36h18v16h16v18h-16v16h-18v-16h-16v-18h16Z'),
    ],
    // An arrest over the Nord Stream bombings: handcuffs above a ruptured undersea pipeline.
    903565: [
      C('s', 104, 72, 25), C('s', 186, 72, 25),
      R('a', 125, 62, 10, 20, 3), R('a', 155, 62, 10, 20, 3), E('u', 145, 72, 10, 5),
      R('b', 20, 138, 176, 30, 3), R('a', 196, 130, 12, 46, 3),
      R('b', 256, 138, 40, 30, 3), R('a', 244, 130, 12, 46, 3),
      C('u', 226, 142, 7), C('u', 233, 118, 5), C('u', 222, 100, 4),
    ],
    // Norway's reigning monarch: a crown on its cushion.
    120116: [
      P('a', 'M96 114L82 60L118 90L150 44L182 90L218 60L204 114Z'),
      C('a', 82, 56, 7), C('a', 150, 39, 8), C('a', 218, 56, 7),
      R('a', 94, 118, 112, 18, 4), C('k', 120, 127, 4), C('k', 150, 127, 4), C('k', 180, 127, 4),
      P('b', 'M74 150Q150 140 226 150Q234 162 226 174Q150 184 74 174Q66 162 74 150Z'),
    ],
    // A Supreme Court justice suspending the police chief: a gavel and a police badge.
    880660: [
      P('b', 'M202 48L242 62V100C242 128 224 146 202 156C180 146 162 128 162 100V62Z'),
      star('a', 202, 100, 22),
      G('translate(98 80) rotate(-35)', [
        R('a', -5, 10, 10, 86, 5), R('a', -36, -17, 72, 34, 7), R('k', -23, -17, 4, 34), R('k', 19, -17, 4, 34),
      ]),
      R('a', 36, 152, 76, 12, 4), R('b', 46, 166, 56, 8, 3),
    ],
    // Okinawa choosing a governor: a ballot box beside a subtropical island.
    581343: [
      P('b', 'M36 168Q90 132 146 168Z'),
      P('s', 'M88 152Q92 114 104 86'),
      ['M104 86Q82 68 62 82', 'M104 86Q90 58 68 54', 'M104 86Q110 58 96 42', 'M104 86Q126 62 146 70', 'M104 86Q130 82 140 102']
        .map((d) => P('u', d)).join(''),
      ballotBox(170, 108),
      wave('t', 36, 186, 10),
    ],
    // The largest vote share in Berlin's state election: the television tower beside the parties' bars.
    81247: [
      L('t', 40, 174, 260, 174),
      P('a', 'M60 168L65 80H71L76 168Z'), C('a', 68, 72, 17), R('k', 50, 71, 36, 4), L('u', 68, 55, 68, 22),
      R('a', 106, 84, 24, 84, 3), R('b', 138, 110, 24, 58, 3), R('b', 170, 100, 24, 68, 3),
      R('b', 202, 130, 24, 38, 3), R('b', 234, 146, 24, 22, 3),
    ],
    // Whether state gambling law covers event contracts: a die weighed against a contract.
    76365: [
      L('s', 150, 54, 150, 160), R('a', 114, 160, 72, 11, 4), C('a', 150, 46, 9),
      L('s', 80, 66, 220, 66),
      P('u', 'M80 66L56 122M80 66L104 122M220 66L196 122M220 66L244 122'),
      P('a', 'M46 122H114Q108 146 80 146Q52 146 46 122Z'), P('a', 'M186 122H254Q248 146 220 146Q192 146 186 122Z'),
      R('b', 69, 98, 22, 22, 5), C('k', 75, 104, 2.4), C('k', 80, 109, 2.4), C('k', 85, 114, 2.4),
      R('b', 210, 94, 20, 26, 3), P('kn', 'M214.500 102h11M214.500 108h11M214.500 114h7'),
    ],
    // The king of Morocco appointing a prime minister: a royal decree in a palace gateway.
    935351: [
      each(6, (i) => R('b', 86 + i * 23.2, 24, 12, 12, 2)),
      P('b', 'M86 36H214V178H86ZM124 178V120A34 34 0 1 1 176 120V178Z', ' fill-rule="evenodd"'),
      R('a', 134, 116, 32, 48, 3), P('kn', 'M140 126h20M140 134h20M140 142h12'),
      C('k', 162, 162, 12), C('a', 162, 162, 9), C('k', 162, 162, 3.5),
    ],

    /* Economy & business --------------------------------------------------- */

    // A record stock-market listing: the opening bell and a rising price.
    279946: [
      C('a', 110, 46, 8),
      P('a', 'M62 136C62 136 76 124 76 96C76 70 92 52 110 52C128 52 144 70 144 96C144 124 158 136 158 136Z'),
      P('a', 'M96 144a14 14 0 0 0 28 0Z'),
      P('s', 'M170 158L196 128L214 142L248 96'), P('s', 'M228 96H248V116'),
    ],
    // The world's most valuable company: the tallest of three towers.
    329053: [
      L('t', 56, 178, 244, 178),
      R('b', 74, 102, 44, 70, 3), R('a', 127, 60, 46, 112, 3), R('b', 182, 118, 44, 54, 3),
      [72, 92, 112, 132, 152].map((y) => R('k', 137, y, 9, 9, 1.5) + R('k', 154, y, 9, 9, 1.5)).join(''),
      [114, 134, 154].map((y) => R('k', 85, y, 8, 8, 1.5) + R('k', 99, y, 8, 8, 1.5)).join(''),
      [130, 150].map((y) => R('k', 193, y, 8, 8, 1.5) + R('k', 207, y, 8, 8, 1.5)).join(''),
      L('u', 150, 60, 150, 26), P('a', 'M150 26L178 35L150 44Z'),
    ],
    // A country singled out for tariffs: a shipping container with a duty on it.
    605397: [
      P('u', 'M146 18V50M146 50L96 94M146 50L196 94'),
      R('a', 62, 94, 168, 66, 4),
      each(9, (i) => L('kn', 80 + i * 16.5, 105, 80 + i * 16.5, 149)),
      C('k', 224, 152, 32), C('a', 224, 152, 26),
      C('ks', 215, 143, 5.5), C('ks', 233, 161, 5.5), L('ks', 235, 140, 213, 164),
    ],
    // Votes for a rate rise at the Federal Reserve: the central bank and an upward arrow.
    942650: [
      P('a', 'M52 84L118 44L184 84Z'), C('k', 118, 68, 7),
      R('a', 56, 88, 124, 10, 2),
      [66, 96, 126, 156].map((x) => R('b', x, 102, 16, 52, 2)).join(''),
      R('a', 52, 158, 132, 12, 3),
      L('s', 226, 166, 226, 72), P('s', 'M204 94L226 68L248 94'),
    ],
    // The fastest-rising part of the food price index: grain, oil and milk under a climbing line.
    205592: [
      P('s', 'M62 68L122 52L172 60L238 24'), P('s', 'M216 22H240V46'),
      L('u', 92, 176, 92, 106),
      [110, 128, 146].map((y) => E('a', 83.5, y, 5.5, 11, -32) + E('a', 100.5, y, 5.5, 11, 32)).join(''),
      E('a', 92, 94, 5.5, 11),
      P('a', 'M150 102C150 102 126 136 126 152A24 24 0 0 0 174 152C174 136 150 102 150 102Z'),
      P('a', 'M196 100H216V114L228 130V176H184V130L196 114Z'), R('k', 184, 142, 44, 14),
    ],

    /* Science & environment ------------------------------------------------ */

    // Where a typhoon comes ashore: a cyclone off a coastline.
    66613: [
      P('b', 'M24 12H90Q70 56 98 92Q116 122 86 150Q70 172 80 198H24Z'),
      P('s', 'M190 66C224 66 240 98 226 128'), P('s', 'M190 130C156 130 140 98 154 68'),
      P('t', 'M190 40C248 40 270 104 238 152'), P('t', 'M190 156C132 156 110 92 142 44'),
      C('a', 190, 98, 16), C('k', 190, 98, 6),
    ],
    // A halt on building large data centres: server racks, paused.
    803035: [
      [46, 100, 154].map((x) => R('b', x, 40, 46, 124, 5)
        + each(6, (i) => R('k', x + 7, 51 + i * 18.5, 32, 10, 2) + C('a', x + 13, 56 + i * 18.5, 2.2))).join(''),
      C('k', 226, 140, 37), C('a', 226, 140, 31), R('k', 213, 125, 9, 30, 2), R('k', 230, 125, 9, 30, 2),
    ],
    // A national emergency over wildfires: a forest on fire.
    149811: [
      L('t', 36, 178, 264, 178),
      P('c', 'M238 84L256 114H247L262 142H251L268 170H208L225 142H214L229 114H220Z'),
      P('b', 'M88 42L112 84H100L120 120H106L128 160H48L70 120H56L76 84H64Z'), R('b', 82, 160, 12, 14),
      P('a', 'M172 34C178 68 212 86 212 126C212 152 196 172 172 172C148 172 132 152 132 126C132 104 148 94 152 72C160 82 163 90 164 98C168 78 168 58 172 34Z'),
      P('k', 'M172 112C176 128 190 134 190 148C190 160 182 168 172 168C162 168 154 160 154 148C154 136 168 130 172 112Z'),
    ],
    // Nuclear plants shut down by drought: cooling towers on cracked ground under the sun.
    772343: [
      C('a', 234, 50, 15),
      each(8, (i) => {
        const from = polar(234, 50, 23, i * 45);
        const to = polar(234, 50, 32, i * 45);
        return L('u', from[0], from[1], to[0], to[1]);
      }),
      P('b', 'M160 158C168 128 172 112 168 86H208C204 112 208 128 216 158Z'),
      P('a', 'M66 158C78 116 84 96 78 50H142C136 96 142 116 154 158Z'),
      R('b', 40, 162, 220, 22, 3), P('kn', 'M84 162l9 8l-7 14M150 162l-8 9l9 13M214 162l8 8l-8 14'),
    ],
    // A 100-metre race between humanoid robots: a robot at full sprint.
    48050: [
      L('t', 36, 180, 264, 180),
      P('t', 'M44 70H84M30 96H76M48 122H82'),
      P('w', 'M150 88L124 102L114 126'), P('w', 'M152 126L130 150L98 144L92 158'),
      G('rotate(14 162 100)', [R('a', 140, 70, 42, 58, 10)]),
      R('a', 162, 26, 38, 32, 8), R('k', 181, 38, 14, 8, 4), L('u', 176, 26, 176, 20), C('a', 176, 17, 4.5),
      P('w', 'M170 88L198 100L212 78'), P('w', 'M166 128L198 134L198 168L214 168'),
    ],
    // The year's first measles death: the virus and its rash.
    903529: [
      each(10, (i) => {
        const from = polar(150, 100, 34, 10 + i * 36);
        const to = polar(150, 100, 53, 10 + i * 36);
        return L('u', from[0], from[1], to[0], to[1]) + C('a', to[0], to[1], 6.5);
      }),
      C('a', 150, 100, 36), C('k', 138, 90, 7), C('k', 163, 101, 5), C('k', 146, 115, 4),
      C('b', 66, 56, 7), C('c', 80, 150, 9), C('b', 238, 60, 5), C('c', 232, 148, 8),
      C('b', 50, 108, 4), C('b', 254, 104, 4.5), C('c', 104, 26, 5), C('c', 200, 178, 5),
    ],
    // A court asked to halt work on a chatbot: a chat bubble and a stop sign.
    133827: [
      P('a', 'M66 38H186A18 18 0 0 1 204 56V110A18 18 0 0 1 186 128H118L90 154V128H66A18 18 0 0 1 48 110V56A18 18 0 0 1 66 38Z'),
      glint('k', 112, 84, 30), glint('k', 160, 58, 13),
      ngon('k', 216, 138, 43, 8, 22.5), ngon('a', 216, 138, 36, 8, 22.5), R('k', 203, 125, 26, 26, 4),
    ],

    /* Arts & entertainment ------------------------------------------------- */

    // A broadcaster boycotting the song contest: a microphone, struck out.
    964047: [
      R('a', 133, 44, 34, 58, 17),
      P('s', 'M118 84a32 32 0 0 0 64 0'), L('s', 150, 116, 150, 140), L('s', 130, 142, 170, 142),
      E('a', 96, 122, 8, 6, -20), L('u', 103, 120, 103, 90), P('u', 'M103 90q10 2 12 12'),
      E('a', 196, 104, 8, 6, -20), L('u', 203, 102, 203, 72), P('u', 'M203 72q10 2 12 12'),
      C('s', 150, 100, 74),
      L('ko', 100, 150, 200, 50), L('s', 97.700, 152.300, 202.300, 47.700),
    ],
    // A prize at the Venice Film Festival: a film reel in a laurel wreath.
    52657: [
      laurel(150, 102, 74),
      C('a', 150, 100, 40), C('k', 150, 100, 7),
      each(5, (i) => {
        const at = polar(150, 100, 23, 90 + i * 72);
        return C('k', at[0], at[1], 9.5);
      }),
    ],
    // The Emmy for best comedy series: the laughing mask on television.
    216881: televisedMask([
      P('ks', 'M131 94q7.5 -9 15 0M154 94q7.5 -9 15 0'), P('k', 'M133 108Q150 132 167 108Q150 116 133 108Z'),
    ]),
    // The Emmy for best drama series: the weeping mask on television.
    873349: televisedMask([
      P('ks', 'M131 90q7.5 9 15 0M154 90q7.5 9 15 0'), P('k', 'M133 124Q150 100 167 124Q150 114 133 124Z'),
    ]),

    /* Sport ---------------------------------------------------------------- */

    // The Women's T20 World Cup: bat, ball and stumps.
    258607: [
      [178, 198, 218].map((x) => R('a', x, 66, 9, 106, 3)).join(''), R('a', 176, 56, 24, 7, 3), R('a', 205, 56, 24, 7, 3),
      G('translate(102 106) rotate(27)', [R('b', -5.500, -76, 11, 44, 4), R('a', -16, -32, 32, 100, 8)]),
      C('a', 142, 160, 13), P('kn', 'M131 155q11 9 22 0'),
    ],
    // The Wimbledon singles title: a racket and ball on grass.
    846335: [
      P('b', 'M36 190' + each(19, (i) => 'l6 -' + (i % 2 ? 20 : 13) + 'l6 ' + (i % 2 ? 20 : 13)) + 'Z'),
      G('translate(142 78) rotate(38)', [
        [-17, 0, 17].map((x) => L('n', x, x ? -36 : -42, x, x ? 36 : 42)).join(''),
        [-21, 0, 21].map((y) => L('n', y ? -29 : -34, y, y ? 29 : 34, y)).join(''),
        E('s', 0, 0, 34, 42), P('u', 'M-11 40L0 62L11 40'), R('a', -6, 60, 12, 48, 5),
      ]),
      C('a', 220, 112, 16), P('kn', 'M208 104q12 8 8 22'),
    ],
    // A mountain stage of the Tour de France: a racing bike against the day's profile.
    24813: [
      P('c', 'M24 180L64 152L96 162L136 104L168 128L212 50L244 100L276 88V180Z'),
      C('s', 100, 138, 30), C('s', 200, 138, 30),
      P('u', 'M100 138L132 92H184L150 138ZM132 92L150 138M180 78L200 138M128 84L132 92'),
      L('s', 118, 84, 140, 84), L('s', 172, 76, 190, 76),
      C('a', 150, 138, 6),
    ],
    // The men's football World Cup: a winner's cup.
    241292: [
      P('s', 'M96 58C66 58 68 98 102 100'), P('s', 'M164 58C194 58 192 98 158 100'),
      P('a', 'M92 42H168V78C168 106 152 122 130 122C108 122 92 106 92 78Z'),
      star('k', 130, 78, 16),
      R('a', 123, 120, 14, 26), R('a', 102, 144, 56, 12, 4), R('b', 92, 158, 76, 12, 4),
      football(216, 146, 24),
    ],
    // The World Cup's top scorer: a boot and a ball.
    201629: [
      P('a', 'M60 150V90C60 82 66 78 74 78H92C98 78 102 82 104 88L108 100L164 118C182 124 194 134 194 150Z'),
      P('ks', 'M118 104l-6 15M135 110l-6 15M152 116l-6 15'), L('kn', 62, 94, 103, 94),
      R('b', 56, 152, 142, 8, 3),
      [66, 92, 150, 176].map((x) => R('a', x, 162, 12, 11, 2)).join(''),
      football(230, 148, 23),
      glint('a', 152, 58, 17), glint('b', 190, 88, 9),
    ],
    // Where a basketball star signs next: a ball dropping through the hoop.
    981188: [
      R('b', 92, 26, 116, 80, 6),
      C('k', 150, 62, 27), C('a', 150, 62, 23), P('kn', 'M127 62H173M150 39V85M134 46Q146 62 134 78M166 46Q154 62 166 78'),
      E('s', 150, 112, 36, 9),
      P('n', 'M116 115L130 164M132 120L140 164M150 121V164M168 120L160 164M184 115L170 164M123 136H177M127 151H173'),
    ],
    // A footballer's next club: a shirt changing hands.
    810891: [
      P('a', 'M118 38L96 46L58 78L80 110L100 94V166H200V94L220 110L242 78L204 46L182 38C174 54 126 54 118 38Z'),
      P('ks', 'M126 108H172M160 96L174 108L160 120'), P('ks', 'M174 142H128M140 130L126 142L140 154'),
    ],
    // A title fight in mixed martial arts: a champion's belt in the octagon.
    40115: [
      ngon('c', 150, 100, 84, 8, 22.5),
      R('a', 50, 84, 200, 34, 6),
      R('k', 84, 78, 26, 46, 6), R('a', 87, 81, 20, 40, 4), R('k', 190, 78, 26, 46, 6), R('a', 193, 81, 20, 40, 4),
      C('k', 150, 101, 43), C('a', 150, 101, 38), C('kn', 150, 101, 29), star('k', 150, 101, 16),
    ],
    // The Women's Africa Cup of Nations: a football beside the continent.
    616886: [
      blob('b', [[112, 30], [138, 24], [160, 36], [184, 38], [196, 62], [208, 82], [234, 84], [218, 108], [206, 126], [206, 146],
        [192, 168], [176, 186], [160, 186], [152, 166], [150, 142], [140, 120], [142, 104], [124, 98], [100, 102], [82, 92], [74, 72], [86, 48]]),
      football(98, 150, 25),
    ],
    // A Premier League season opener: the pitch at kick-off.
    97251: [
      R('c', 46, 34, 208, 132, 6), R('u', 46, 34, 208, 132, 6),
      L('u', 150, 34, 150, 166), C('u', 150, 100, 30),
      R('u', 46, 64, 38, 72), R('u', 216, 64, 38, 72),
      C('k', 150, 100, 17), football(150, 100, 14),
    ],
    // The Italian Grand Prix: a racing car and the chequered flag.
    668636: [
      L('t', 30, 170, 270, 170), P('t', 'M20 106H46M12 124H40'),
      L('u', 206, 86, 206, 20),
      each(12, (i) => R((i + Math.floor(i / 4)) % 2 ? 'c' : 'a', 208 + (i % 4) * 12, 20 + Math.floor(i / 4) * 12, 12, 12)),
      R('a', 50, 86, 32, 9, 2), R('a', 60, 92, 9, 40, 2),
      P('a', 'M62 140L80 122L126 118L142 100H170L182 118L226 124L250 140Z'),
      R('a', 238, 138, 26, 7, 2),
      C('k', 100, 144, 24), C('a', 100, 144, 18), C('k', 100, 144, 6),
      C('k', 208, 144, 24), C('a', 208, 144, 18), C('k', 208, 144, 6),
      C('k', 157, 109, 8),
    ],
    // The US Open singles title: a ball in play on a hard court.
    891014: [
      R('c', 58, 38, 184, 124, 3), R('u', 58, 38, 184, 124, 3),
      P('n', 'M58 56H242M58 144H242M104 56V144M196 56V144M104 100H196'),
      L('s', 150, 28, 150, 172),
      C('k', 222, 84, 18), C('a', 222, 84, 14), P('kn', 'M211 78q11 6 8 20'),
    ],
    // The 100 metres at the Asian Games: the lanes and a stopwatch.
    686508: [
      P('t', 'M24 182L104 50M76 182L120 50M128 182L136 50M180 182L152 50'),
      L('u', 93, 68, 156, 68),
      R('a', 222, 44, 12, 16, 3), G('rotate(42 228 108)', [R('a', 223, 52, 10, 13, 2)]),
      C('s', 228, 108, 38), L('u', 228, 108, 228, 84), L('u', 228, 108, 244, 118), C('a', 228, 108, 5),
    ],
  };

  // One plain drawing per category, for a question added to the data before it has its own.
  const FALLBACK = {
    geopolitics: [C('s', 150, 100, 62), E('u', 150, 100, 27, 62), P('u', 'M88 100H212M98 68Q150 84 202 68M98 132Q150 116 202 132')],
    politics: [ballotBox(108, 96)],
    economy: [
      L('t', 56, 172, 244, 172),
      R('b', 76, 126, 28, 40, 3), R('b', 116, 104, 28, 62, 3), R('b', 156, 84, 28, 82, 3), R('a', 196, 58, 28, 108, 3),
    ],
    science: [
      P('a', 'M130 34H170V46H164V84L206 158C210 166 204 174 196 174H104C96 174 90 166 94 158L136 84V46H130Z'),
      P('k', 'M119 132H181L198 162H102Z'), C('k', 148, 112, 5),
    ],
    culture: [
      R('a', 70, 86, 160, 84, 6), P('a', 'M68 60L224 34L228 58L72 84Z'),
      P('kn', 'M96 55.500l10 22M136 49l10 22M176 42.500l10 22'),
    ],
    sport: [
      P('b', 'M116 26H140L156 84H132Z'), P('b', 'M184 26H160L144 84H168Z'),
      C('a', 150, 122, 46), C('k', 150, 122, 35), C('a', 150, 122, 30), star('k', 150, 122, 18),
    ],
  };

  const join = (parts) => parts.join('');
  const out = { byId: {}, byCategory: {} };
  Object.keys(ART).forEach((id) => { out.byId[id] = join(ART[id]); });
  Object.keys(FALLBACK).forEach((id) => { out.byCategory[id] = join(FALLBACK[id]); });
  window.FQ_ART = out;
})();
