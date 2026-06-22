---
version: alpha
name: SDSC Plotting & Data Visualization
description: >-
  Visual identity for Swiss Data Science Center scientific charts — CVD-safe
  categorical/sequential/diverging palettes, perceptually-uniform colormaps, and
  chart-design rules for any charting stack (matplotlib, plotly, D3, Vega,
  ggplot, CSS/JS, …; ready-made themes for the first three). Chart colours encode
  data and must be distinguishable from each other, so they differ deliberately
  from the sdsc-ui-kit interface palette. The brand anchor (Chart Dark Blue)
  matches SDSC Secondary #26235C; all values are verified by
  scripts/verify_chart_palettes.py.
colors:
  cat-1-dark-blue: "#26235C"
  cat-2-green: "#73A235"
  cat-3-orange: "#B34A00"
  cat-4-sky-blue: "#56B4E9"
  cat-5-pink: "#CC79A7"
  focus-muted: "#B8B8B8"
  seq-1: "#26235C"
  seq-2: "#4A4889"
  seq-3: "#7A7AB5"
  seq-4: "#AAAED7"
  seq-5: "#DDDEEC"
  div-strong-negative: "#26235C"
  div-negative: "#7A7AB5"
  div-neutral: "#F0EEEB"
  div-positive: "#CF7D42"
  div-strong-positive: "#B34A00"
  dark-cat-1-blue: "#8A94C9"
  dark-cat-2-green: "#90CA42"
  dark-cat-3-orange: "#E07B39"
typography:
  title:
    fontFamily: Space Grotesk
    fontWeight: 600
  axis-label:
    fontFamily: Switzer
    fontWeight: 400
  annotation:
    fontFamily: Switzer
    fontWeight: 400
components:
  chart-series-1:
    backgroundColor: "{colors.cat-1-dark-blue}"
  chart-series-2:
    backgroundColor: "{colors.cat-2-green}"
  chart-focus-highlight:
    backgroundColor: "{colors.cat-1-dark-blue}"
  chart-focus-context:
    backgroundColor: "{colors.focus-muted}"
---

## Overview

SDSC charts treat colour as a **data encoding**, not decoration — so this
identity is governed by distinguishability and accessibility, not brand styling.
Every categorical colour must be told apart from the *other* series (not just the
background) and must survive colour-vision-deficiency (CVD) simulation. The
palettes are anchored to the SDSC brand (Chart Dark Blue = Secondary `#26235C`)
but diverge from the `sdsc-ui-kit` interface colours on purpose: interface
colours are tuned to sit against a page, data colours to separate from each
other. Use this skill for plots, charts, heatmaps, and figures; interface chrome
(buttons, forms, layout) belongs to `sdsc-ui-kit`.

The frontmatter tokens are the normative palette; the prose explains how to apply
them. They are not hand-tuned aesthetics — `scripts/verify_chart_palettes.py`
re-derives their contrast, CVD separation, and CIELAB ΔE from scratch (no
dependencies) and gates on mutual distinguishability. Re-run it after any change.

## Colors

Four palette types cover all scenarios — pick by data structure:

- **Categorical** (unordered groups): use in order Dark Blue → Green → Orange →
  Sky Blue → Pink, **max 5**. Single-variable bar charts use one colour, not one
  per bar — colour varies only when it encodes something.
- **Focus / highlight**: colour one series (Dark Blue or Green), mute the rest to
  `#B8B8B8`. Scales far beyond 5 series.
- **Sequential** (ordered categories): brand dark blue at evenly spaced lightness,
  `#26235C` → `#DDDEEC`, 3–5 steps. Lightest steps fall below 3:1 on white —
  separate with thin borders and label directly.
- **Diverging** (meaningful midpoint only): `#26235C` ↔ neutral `#F0EEEB` ↔
  `#B34A00`; keep which end is "negative" consistent across a product.
- **Dark mode**: the categorical palette inverts poorly (`#26235C` vanishes on
  `#2d2d2d`) — swap to lightened variants and prefer ≤ 4 series.
- **Continuous fields (colormaps)**: never build colormaps from brand colours —
  use established perceptually-uniform, CVD-safe maps (`viridis`, `cividis`,
  `batlow`; diverging `vik`, `roma`, `RdBu`; cyclic `twilight`, `romaO`).

## Typography

Chart text uses the SDSC fonts — Space Grotesk for figure titles, Switzer for
axis labels, tick labels, and annotations — at the sizes set by the per-stack
themes (`assets/sdsc_theme.py`, `assets/sdsc_plotly_theme.py`). Keep text large
enough to read at final print size, label series directly instead of relying on a
distant legend where possible, and never encode meaning by colour alone — pair it
with labels, markers, or line styles.

## Layout

Favour clarity over density: start bar axes at zero, remove chart junk
(unnecessary gridlines, heavy borders, 3-D effects), and give continuous plots a
labelled colour bar with units, noting any clipping or log transform. Always name
the uncertainty interval shown (e.g. "95% CI", "±1 SD") rather than drawing an
unlabelled band. For greyscale print, verify the colormap is monotonic in
lightness.

## Shapes

Distinguish series by more than hue where it helps accessibility: vary marker
shape and line style alongside colour, thicken lines and enlarge markers for any
low-contrast series (Sky Blue `#56B4E9` is ~2.3:1 on white — intentionally chosen
for CVD separation, so reinforce it with weight). Separate adjacent sequential
bands with thin white/grey borders when the lightest steps approach the page
colour.

## Components

- **Series (categorical / focus)** — the `chart-series-*` and `chart-focus-*`
  tokens map to the palette in order; consume them via the shipped themes, never
  by hard-coding hex per plot.
- **Colour bar** — required for any continuous colormap; show units and scale
  transforms.
- **Legend / direct labels** — prefer direct labels on series; when a legend is
  needed, keep series count within the palette limits so entries stay
  distinguishable.
- **Gridlines / axes** — light, minimal; bars and area baselines start at zero.

## Do's and Don'ts

- **Do** apply colour via the themes (`import sdsc_theme`, `template="sdsc"`) so
  hex values stay out of individual plots.
- **Do** keep categorical series ≤ 5 (≤ 4 in dark mode); group the rest into
  "Other" or use small multiples.
- **Do** run `scripts/verify_chart_palettes.py` after any palette edit.
- **Don't** use rainbow / jet colormaps, or red–green for continuous data — they
  create false boundaries and fail for CVD (a correctness issue, not a style one).
- **Don't** build colormaps out of brand colours, or reuse interface (`sdsc-ui-kit`)
  colours as data encodings.
- **Don't** rely on colour alone, draw unlabelled uncertainty bands, or start a
  bar axis above zero.
