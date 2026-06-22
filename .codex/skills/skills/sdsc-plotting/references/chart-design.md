# SDSC Chart Design Rules

Principles governing chart-type selection, axes, decluttering, uncertainty, plot
typography, and accessibility.

## Choosing the chart

| Data relationship | Chart |
|-------------------|-------|
| Comparison | bars |
| Trend over time | lines |
| Distribution | histogram / density / boxen |
| Correlation | scatter |
| Part-of-whole | stacked bar (avoid pie beyond 2–3 slices) |
| More than ~5 series | small multiples with shared axes |

When unsure, consult the
[FT Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary).

## Axes & scales

- Bar charts must start at zero.
- No dual y-axes; use two stacked panels instead.
- Label axes with quantity and unit (metric; ISO-8601 dates).
- Avoid rotated x-labels — abbreviate, or swap to horizontal bars.
- Log scales: label ticks with actual values (1, 10, 100).

## Decluttering

- Light grey gridlines (`#e5e5e5`), horizontal only in most cases.
- No chart borders, no background fills, no 3D, no shadows.
- Direct-label lines at their right end instead of a legend.
- Order the legend to match the visual order of the series.
- Titles state the takeaway; subtitles state the measure.

## Visualizing uncertainty

Scientific plots without uncertainty overstate certainty (Padilla, Kay & Hullman
2021). Readers misread error bars as hard ranges ("within-bar" bias) — prefer
showing distributions over bare intervals.

**Always state what an interval is.** "Error bars" meaning SD, SEM, 95% CI, or a
prediction interval differ by large factors — name it in the caption or legend,
every time.

Options in rough order of preference:

1. **Gradient / fan plots** *(time series)* — interval fading out with
   probability; best for time-series forecasts.
2. **Quantile dotplots** *(static figures)* — the distribution as ~20–50 dots;
   the most accurately read static representation for lay and expert audiences.
3. **Half-eye / raincloud plots** *(group comparisons)* — density + interval +
   optional raw points; good default for comparing groups.
4. **Hypothetical outcome plots (HOPs)** *(interactive)* — animated draws from
   the distribution; effective in interactive dashboards.

- **Frequency framing for non-experts:** "1 in 20" outperforms "5%".
- **Uncertainty colour:** render in greys / transparency of the series colour,
  never as an extra categorical colour.

## Typography in plots

| Element | Font | Min size | Colour |
|---------|------|----------|--------|
| Chart title | Space Grotesk, 600 | 16 px | `#000000` |
| Subtitle / caption | Switzer, 400 | 12 px | `#848484` |
| Axis & data labels | Switzer, 400 | 12 px | `#404040` |
| Direct series labels | Switzer, 500 | 12 px | series colour ≥ 4.5:1 |

- **Caption contrast:** `#848484` is 3.7:1 on white — acceptable for large text
  only. Use `#6b6b6b` for small captions (below 18.66 px / 14 px bold).
- **Print / PDF export:** embed fonts or fall back to a standard sans
  (Helvetica/Arial) rather than letting the renderer substitute.

## Accessibility checklist for charts

Adapted from the UK Government Analysis Function 'accessible charts' checklist.
Verify all before shipping:

- [ ] Information is not conveyed by colour alone (labels, markers, patterns as backup)
- [ ] ≤ 5 colour-coded series (≤ 4 in dark mode); palette used in defined order
- [ ] All essential graphical elements ≥ 3:1 contrast against their background
- [ ] Text in / around the chart ≥ 12 px and ≥ 4.5:1 contrast
- [ ] Checked under CVD simulation (browser dev tools or Coblis)
- [ ] Title / alt text states the *message* of the chart, not just its topic
- [ ] Interactive charts: keyboard-reachable tooltips; underlying data downloadable or in a table
- [ ] Units, sources, and uncertainty definitions present
- [ ] Survives greyscale printing

### Key thresholds

| Threshold | Applies to |
|-----------|-----------|
| **4.5:1** | Text contrast minimum |
| **3:1** | Graphical object minimum |
| **12 px** | Minimum chart text size |
