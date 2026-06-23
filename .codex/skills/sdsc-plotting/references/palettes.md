# SDSC Chart Palettes

Four palette types cover all chart scenarios. Choose the type that matches your
data structure. Chart colours differ from UI-kit colours because in a chart
colour must encode data and be distinguishable from *other colours*, not just
from the background.

## Categorical palette

For distinct, unordered categories (line series, grouped bars, scatter groups).
Use **in this order** — ordered so the first colours used are the most
distinguishable.

| Order | Name | Hex | Notes |
|-------|------|-----|-------|
| 1 | Chart Dark Blue | `#26235c` | SDSC primary brand colour |
| 2 | Chart Green | `#73a235` | SDSC accent green, darkened for contrast on white |
| 3 | Chart Orange | `#b34a00` | |
| 4 | Chart Sky Blue | `#56b4e9` | |
| 5 | Chart Pink | `#cc79a7` | |

- **Maximum 5 categories.** Beyond 4–5 series no palette stays readable. Group
  small categories into "Other", or use small multiples (one panel per series).
- **One colour for single-variable bar charts.** Bar charts with one variable
  use one colour (Chart Dark Blue), not one per bar. Colour only varies when it
  encodes something.

## Focus / highlight charts

To draw attention to one series among many, colour it and mute the rest. Scales
far beyond 5 series.

| Hex | Label |
|-----|-------|
| `#26235c` | Highlighted |
| `#73a235` | Highlighted (alt) |
| `#b8b8b8` | Muted context series |

## Sequential palette (ordered categories)

For ordered categories (age bands, quintiles, ratings) in legends, stacked bars,
or simple choropleths. Brand dark blue with evenly spaced lightness
(L\* ≈ 18 / 34 / 53 / 72 / 89).

| Hex | Label |
|-----|-------|
| `#26235c` | Darkest (highest) |
| `#4a4889` | |
| `#7a7ab5` | |
| `#aaaed7` | |
| `#dddeec` | Lightest (lowest) |

Use 3–5 steps. The lightest steps fall below 3:1 contrast on white — separate
areas with thin white/grey borders and label values directly.

## Diverging palette

For data with a meaningful midpoint (above/below zero, agree/disagree). Diverges
from a near-neutral centre to brand blue and chart orange.

| Hex | Label |
|-----|-------|
| `#26235c` | Strong negative |
| `#7a7ab5` | Negative |
| `#f0eeeb` | Neutral mid |
| `#cf7d42` | Positive |
| `#b34a00` | Strong positive |

Only use diverging when the midpoint is meaningful. Which end is "negative" is
your choice — keep it consistent across all charts in the same product or
publication.

## Dark mode

The categorical palette inverts poorly on dark backgrounds (`#26235c` is
invisible on `#2d2d2d`). In dark mode use lightened variants and prefer
**≤ 4 series**.

| Name | Hex | Notes |
|------|-----|-------|
| Dark Blue | `#8a94c9` | Replaces `#26235c` |
| Green | `#90ca42` | Replaces `#73a235` |
| Orange | `#e07b39` | Replaces `#b34a00` |
| Sky Blue | `#56b4e9` | Unchanged |
| Pink | `#cc79a7` | Unchanged |

## Continuous data: colormaps

For heatmaps, density plots, geospatial fields — anywhere colour represents a
continuous value.

- **Never use rainbow / jet.** Rainbow colormaps create false boundaries in
  smooth data and hide real ones (Crameri et al. 2020). This is a correctness
  issue, not a style preference. Never use red–green for continuous data.
- **Do not build colormaps from brand colours.** Use established perceptually
  uniform, CVD-safe colormaps.

| Data type | Approach | Examples |
|-----------|----------|----------|
| Sequential (zero → max) | Perceptually uniform sequential | `viridis`, `cividis`, `batlow` |
| Diverging (meaningful midpoint) | Perceptually uniform diverging | `vik`, `roma`, `RdBu` |
| Cyclic (phase / angle / time-of-day) | Cyclic | `twilight`, `romaO` |

- **Always show a colour bar** with units; state if the scale is clipped or
  log-transformed.
- **Greyscale check.** If the figure may be printed in greyscale, verify the
  colormap is monotonic in lightness. `viridis`, `cividis`, `batlow` are;
  rainbow is not.

## How these palettes were verified

- **≥ 3:1 contrast check** — every categorical colour has ≥ 3:1 contrast against
  white (WCAG 2.1 SC 1.4.11 for graphical objects).
- **CVD** — simulated for protanopia, deuteranopia, tritanopia (Machado et al.
  2009 matrices).
- **ΔLAB** — minimum pairwise difference checked in CIELAB. Tightest pair is
  Green vs Orange under deuteranopia.

Re-run checks after any palette change: `python3 scripts/verify_chart_palettes.py`
(no dependencies). Interactive tools:
[viz-palette](https://projects.susielu.com/viz-palette) ·
[Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/).
