---
name: sdsc-plotting
description: >-
  Use this skill when creating scientific plots, charts, or data graphics for
  Swiss Data Science Center (SDSC) platforms, reports, dashboards, or papers —
  choosing CVD-safe categorical / sequential / diverging palettes and
  perceptually-uniform colormaps, applying chart design rules, and visualizing
  uncertainty. Framework-agnostic: the palettes and rules apply to any charting
  stack (matplotlib, plotly, D3, Vega, ggplot, Observable Plot, CSS/JS, …), with
  ready-made themes provided for matplotlib, plotly, and CSS/JS. Use when the
  user asks to make, style, or review a plot, chart, heatmap, or figure for
  SDSC. Do not use for interface chrome (buttons, forms, page layout) — use the
  sdsc-ui-kit skill for UI components.
---

# SDSC Plotting & Data Visualization

Produce scientific charts that are CVD-safe, perceptually honest, and on-brand
for the Swiss Data Science Center. Companion to the SDSC UI Design Kit — but
**chart colours are not interface colours.** UI-kit colours are optimized for
interface chrome; in a chart, colour must *encode data*.

## When to use this skill

Apply whenever generating or reviewing a plot, chart, heatmap, density plot, or
figure for an SDSC platform, report, dashboard, or publication — in any stack
(matplotlib, plotly, D3/JS, etc.). For buttons, forms, and page layout, use the
**sdsc-ui-kit** skill instead.

## Three core principles

1. **Colour encodes meaning, never decoration.** If a colour tells the reader
   nothing, use one colour. (Single-variable bar charts use *one* colour, not
   one per bar.)
2. **Never rely on colour alone.** Pair colour with direct labels, markers, dash
   patterns, or annotation — the single most effective accessibility measure.
   ~5% of users have colour vision deficiency.
3. **Match palette type to data type.** Categorical → categorical palette ·
   ordered → sequential · meaningful midpoint → diverging · continuous field →
   perceptually-uniform colormap.

## Non-negotiable rules

- **Maximum 5 categorical series** (≤ 4 in dark mode). Beyond that, group into
  "Other", use a focus/highlight palette, or small multiples.
- **Never use rainbow / jet colormaps**, and never red–green for continuous
  data — this is a correctness issue (false boundaries), not a style choice.
  Use `viridis`, `cividis`, or `batlow`.
- **Bar charts start at zero. No dual y-axes** (use stacked panels).
- **Always state what an uncertainty interval is** (SD / SEM / 95% CI /
  prediction interval) — every time, in caption or legend.
- **Define the palette once per stack**; never hard-code hex values in
  individual plots — reference the tokens in `assets/`.

## Procedure

1. Identify the data relationship (comparison, trend, distribution, correlation,
   part-of-whole) and pick the chart type — see `references/chart-design.md`.
2. Pick the palette type from the data type and apply it in the defined order —
   see `references/palettes.md`.
3. Define the palette once for the stack rather than hand-writing colours per
   plot. Ready-made themes exist for three stacks — `assets/sdsc_theme.py`
   (matplotlib), `assets/sdsc_plotly_theme.py` (plotly), `assets/tokens.css`
   (CSS/JS). For any other stack (D3, Vega, ggplot, Observable Plot, …) take the
   palette hex values from `references/palettes.md` and set them once in that
   library's theme/scale. See `references/implementation.md`.
4. Add uncertainty honestly if the data has any — see `references/chart-design.md`.
5. Run the accessibility checklist before shipping (also in `chart-design.md`).
6. After any palette change, re-run the verifier:
   `python3 scripts/verify_chart_palettes.py` (no dependencies).

## References — read the one that matches the task

- **`references/palettes.md`** — All four palette types with exact hex values
  (categorical, focus/highlight, sequential, diverging), dark-mode variants,
  colormap recommendations for sequential/diverging/cyclic continuous data, and
  how the palettes were verified (contrast, CVD, ΔLAB). Read when choosing
  colours.
- **`references/chart-design.md`** — Chart-type selection, axes & scales,
  decluttering, uncertainty visualization (gradient/fan, quantile dotplots,
  half-eye/raincloud, HOPs), plot typography, and the full accessibility
  checklist with key thresholds. Read when designing the chart itself.
- **`references/implementation.md`** — How to load and use the themes in
  matplotlib, plotly, and CSS/JS, plus the Crameri scientific-colourmap
  packages. Read when writing the plotting code.

## Assets & scripts

- **`assets/tokens.css`** — chart colour CSS custom properties (light + dark).
- **`assets/sdsc_theme.py`** — matplotlib rcParams theme.
- **`assets/sdsc_plotly_theme.py`** — plotly template named `sdsc`.
- **`scripts/verify_chart_palettes.py`** — dependency-free checker for contrast,
  CVD distinguishability, and pairwise CIELAB difference. Run after palette edits.
