# SDSC Plotting — Implementation

The palette **hex values in `references/palettes.md` are the source of truth** —
they apply to any charting library. Define them once for whatever stack you use
and reference that definition; never hard-code hex values inside individual
plots. Ready-made themes for three common stacks live in `assets/` (below); for
any other library (D3, Vega/Vega-Lite, ggplot2, Observable Plot, ECharts, …) set
the same hex values once in that library's theme, colour scale, or `scale_*`
definition.

## CSS / JS (`assets/tokens.css`)

Copy into the project's global stylesheet, then reference the variables from
chart code (D3, Chart.js, Observable Plot, etc.).

```css
:root {
  --chart-cat-1: #26235c;
  --chart-cat-2: #73a235;
  --chart-cat-3: #b34a00;
  --chart-cat-4: #56b4e9;
  --chart-cat-5: #cc79a7;
  --chart-muted: #b8b8b8;
  --chart-grid:  #e5e5e5;
}
.dark {
  --chart-cat-1: #8a94c9;
  --chart-cat-2: #90ca42;
  --chart-cat-3: #e07b39;
}
```

## Matplotlib — Python (`assets/sdsc_theme.py`)

Import the module once at the top of a script or notebook; it updates
`mpl.rcParams` globally.

```python
import matplotlib as mpl

SDSC_CATEGORICAL = ["#26235c", "#73a235", "#b34a00", "#56b4e9", "#cc79a7"]

mpl.rcParams.update({
    "axes.prop_cycle": mpl.cycler(color=SDSC_CATEGORICAL),
    "image.cmap": "viridis",
    "axes.grid": True, "axes.grid.axis": "y",
    "grid.color": "#e5e5e5", "axes.edgecolor": "#848484",
    "axes.spines.top": False, "axes.spines.right": False,
    "font.size": 12, "figure.dpi": 150,
})
```

## Plotly — Python / JS (`assets/sdsc_plotly_theme.py`)

Registers a template named `sdsc` and makes it the default.

```python
import plotly.io as pio
import plotly.graph_objects as go

pio.templates["sdsc"] = go.layout.Template(layout={
    "colorway": ["#26235c", "#73a235", "#b34a00", "#56b4e9", "#cc79a7"],
    "colorscale": {"sequential": "Viridis"},
    "font": {"size": 12},
    "xaxis": {"showgrid": False},
    "yaxis": {"gridcolor": "#e5e5e5"},
    "plot_bgcolor": "white",
})
pio.templates.default = "sdsc"
```

## Any other stack

Set the same five categorical hex values once in the library's theme/scale:

- **Vega / Vega-Lite** — a named `range` scheme, or `scale.range` /
  `config.range.category: ["#26235c", "#73a235", "#b34a00", "#56b4e9", "#cc79a7"]`.
- **D3** — `d3.scaleOrdinal().range([...])` with the categorical array.
- **ggplot2 (R)** — `scale_colour_manual(values = c(...))` /
  `scale_fill_manual(...)`; for continuous fills use `scico::scale_*_scico(palette = "batlow")`.
- **Observable Plot / ECharts / Vega-Lite themes** — set the categorical array
  as the colour range and a perceptually-uniform map (`viridis`/`batlow`) for
  continuous scales.

The rules (≤ 5 series, no rainbow, start bars at zero, label uncertainty) are
identical regardless of stack.

## Scientific colourmaps

For the full Scientific colour maps collection (`batlow`, `vik`, `roma`,
`romaO`, …):

- **Python:** `pip install cmcrameri`
- **R:** the `scico` package

## Verifying a palette change

After editing any palette, run the dependency-free checker:

```bash
python3 scripts/verify_chart_palettes.py
```

It reports per-colour contrast against white, pairwise CIELAB difference under
normal vision and the three CVD simulations, and flags any pair that falls below
the distinguishability threshold.
