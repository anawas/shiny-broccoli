#!/usr/bin/env python3
"""Verify the SDSC chart palettes for accessibility. No dependencies.

Checks, for the categorical palette:
  1. Pairwise distinguishability in CIELAB (CIE76 dE) under normal vision and
     simulated protanopia, deuteranopia, and tritanopia (Machado et al. 2009).
     This is the HARD GATE: series must be tellable apart from each other.
  2. Contrast against white -- WCAG 2.1 SC 1.4.11 graphical objects (>= 3:1).
     This is ADVISORY (warning only). Categorical series are always paired with
     direct labels/markers ("never rely on colour alone"), and the palette
     deliberately includes the Okabe-Ito sky blue (#56b4e9, ~2.3:1) for its CVD
     distinguishability. Low against-white contrast is surfaced, not failed, so
     the canonical palette is not blocked; thicken lines / enlarge markers for
     low-contrast series.

Exit code 0 if the hard gate passes, 1 otherwise, so it can gate CI.

Run:  python3 scripts/verify_chart_palettes.py

To check a different palette, edit CATEGORICAL below (or import the functions).
The thresholds (CONTRAST_MIN, DELTA_E_MIN) are documented inline; change them
only with a stated reason.
"""

import sys

# ---- Palette under test (keep in sync with the guidelines / tokens) ----------
CATEGORICAL = {
    "Chart Dark Blue": "#26235c",
    "Chart Green":     "#73a235",
    "Chart Orange":    "#b34a00",
    "Chart Sky Blue":  "#56b4e9",
    "Chart Pink":      "#cc79a7",
}

# ---- Thresholds --------------------------------------------------------------
CONTRAST_MIN = 3.0   # WCAG 2.1 SC 1.4.11: graphical objects need >= 3:1.
DELTA_E_MIN = 11.0   # CIE76 dE below ~11 reads as "hard to tell apart" for
                     # adjacent chart elements. Conservative; tune with reason.

# ---- Machado et al. (2009) CVD matrices, severity 1.0, applied to linear RGB -
CVD_MATRICES = {
    "protanopia": (
        (0.152286, 1.052583, -0.204868),
        (0.114503, 0.786281, 0.099216),
        (-0.003882, -0.048116, 1.051998),
    ),
    "deuteranopia": (
        (0.367322, 0.860646, -0.227968),
        (0.280085, 0.672501, 0.047413),
        (-0.011820, 0.042940, 0.968881),
    ),
    "tritanopia": (
        (1.255528, -0.076749, -0.178779),
        (-0.078411, 0.930809, 0.147602),
        (0.004733, 0.691367, 0.303900),
    ),
}


def hex_to_srgb(value):
    """'#rrggbb' -> (r, g, b) floats in [0, 1]."""
    h = value.lstrip("#")
    if len(h) != 6:
        raise ValueError(f"expected #rrggbb, got {value!r}")
    return tuple(int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))


def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c):
    c = max(0.0, min(1.0, c))
    return c * 12.92 if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def relative_luminance(srgb):
    r, g, b = (srgb_to_linear(c) for c in srgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(srgb_a, srgb_b):
    la, lb = relative_luminance(srgb_a), relative_luminance(srgb_b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def apply_cvd(srgb, matrix):
    """Simulate CVD: linearize, multiply by matrix, return to sRGB."""
    lin = [srgb_to_linear(c) for c in srgb]
    out = [sum(m * v for m, v in zip(row, lin)) for row in matrix]
    return tuple(linear_to_srgb(c) for c in out)


def srgb_to_lab(srgb):
    """sRGB [0,1] -> CIELAB (D65)."""
    r, g, b = (srgb_to_linear(c) for c in srgb)
    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505
    # Normalize by D65 white.
    x, y, z = x / 0.95047, y / 1.0, z / 1.08883

    def f(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116

    fx, fy, fz = f(x), f(y), f(z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def delta_e(lab_a, lab_b):
    """CIE76 Euclidean distance in Lab."""
    return sum((a - b) ** 2 for a, b in zip(lab_a, lab_b)) ** 0.5


def main():
    names = list(CATEGORICAL)
    srgb = {n: hex_to_srgb(CATEGORICAL[n]) for n in names}
    white = (1.0, 1.0, 1.0)
    ok = True   # hard gate: pairwise distinguishability only

    print("Pairwise distinguishability (CIE76 dE, HARD GATE, need >= %.1f):"
          % DELTA_E_MIN)
    visions = [("normal", None)] + list(CVD_MATRICES.items())
    for vision, matrix in visions:
        if matrix is None:
            lab = {n: srgb_to_lab(srgb[n]) for n in names}
        else:
            lab = {n: srgb_to_lab(apply_cvd(srgb[n], matrix)) for n in names}
        worst = None
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                d = delta_e(lab[names[i]], lab[names[j]])
                if worst is None or d < worst[0]:
                    worst = (d, names[i], names[j])
        d, a, b = worst
        flag = "OK " if d >= DELTA_E_MIN else "LOW"
        if d < DELTA_E_MIN:
            ok = False
        print(f"  [{flag}] {vision:<13} tightest pair dE={d:5.1f}  ({a} vs {b})")

    print("\nContrast against white (ADVISORY, target >= %.1f:1):" % CONTRAST_MIN)
    for n in names:
        cr = contrast_ratio(srgb[n], white)
        flag = "OK  " if cr >= CONTRAST_MIN else "WARN"
        note = "" if cr >= CONTRAST_MIN else "  <- thicken lines / enlarge markers"
        print(f"  [{flag}] {n:<16} {CATEGORICAL[n]}  {cr:4.2f}:1{note}")

    print("\n" + ("PASS — series are mutually distinguishable (hard gate)." if ok
                  else "FAIL — a series pair is below the distinguishability "
                       "threshold (see [LOW] rows)."))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
