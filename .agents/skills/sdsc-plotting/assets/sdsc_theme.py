"""SDSC matplotlib theme.

Apply the SDSC chart palette and decluttering defaults to matplotlib globally.

Usage:
    import sdsc_theme          # applies on import
    # ...or explicitly:
    from sdsc_theme import apply
    apply()

The categorical cycle is CVD-safe and ordered most-distinguishable-first.
Keep to <= 5 series; for continuous fields the default colormap is viridis
(perceptually uniform, greyscale-safe). Never hard-code these hex values in a
plot -- reference SDSC_CATEGORICAL instead.
"""

import matplotlib as mpl

# Ordered most-distinguishable-first. Max 5 categories.
SDSC_CATEGORICAL = ["#26235c", "#73a235", "#b34a00", "#56b4e9", "#cc79a7"]

# Lightened variants for dark backgrounds (prefer <= 4 series in dark mode).
SDSC_CATEGORICAL_DARK = ["#8a94c9", "#90ca42", "#e07b39", "#56b4e9", "#cc79a7"]

SDSC_MUTED = "#b8b8b8"   # context series in focus/highlight charts
SDSC_GRID = "#e5e5e5"


def apply(dark: bool = False) -> None:
    """Update matplotlib rcParams with the SDSC theme.

    Args:
        dark: use the lightened dark-mode categorical cycle.
    """
    palette = SDSC_CATEGORICAL_DARK if dark else SDSC_CATEGORICAL
    mpl.rcParams.update({
        "axes.prop_cycle": mpl.cycler(color=palette),
        "image.cmap": "viridis",
        "axes.grid": True,
        "axes.grid.axis": "y",          # horizontal gridlines only
        "grid.color": SDSC_GRID,
        "axes.edgecolor": "#848484",
        "axes.spines.top": False,       # no top/right spines
        "axes.spines.right": False,
        "font.size": 12,                # 12px minimum chart text
        "figure.dpi": 150,
    })


# Apply on import for the common case.
apply()
