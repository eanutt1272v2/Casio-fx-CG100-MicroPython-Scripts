from casioplot import clear_screen, draw_string, set_pixel, show_screen
from math import pi

from psi_fx_lib import (
    SCR_H,
    PY,
    SAMP,
    LEG_X,
    LEG_W,
    LEG_H,
    LEG_LABEL_X,
    EPSILON,
    AMU_TO_KG,
    BASIS_MAP,
    PLANE_MAP,
    UNIT_LABELS,
    CMAP_REGISTRY,
    read_int,
    read_float,
    read_text,
    wait_for_exit,
    HydrogenicWavefunction,
    get_unit_map,
    get_R,
    get_peak_density,
    generate_colour_lut,
    fmt_density,
    format_hdr,
)

n = read_int("n (default=4): ", min_value=1, default=4)
l = read_int("l (0..n-1, default=1): ", min_value=0, max_value=n - 1, default=1)
m = read_int("m (-l..l, default=0): ", min_value=-l, max_value=l, default=0)
Z = read_float("Z (default=1.0): ", min_value=0.1, default=1.0)

use_mu = read_text("Reduced mass? (y/n, default=y): ", default="y").lower() == "y"
M_kg = (read_float("Nucleus Mass [amu] (default=%s): " % (2.0 * Z), default=2.0 * Z) * AMU_TO_KG) if (use_mu and Z > 1.0) else None

print("Spherical Harmonic Basis:")
for k in range(1, len(BASIS_MAP) + 1):
    print("%s: %s" % (k, BASIS_MAP[k]))
basis_choice = read_int("Basis (1-2, default=2): ", min_value=1, max_value=2, default=2)
basis_str = BASIS_MAP[basis_choice]

print("Slice Plane:")
for k in range(1, len(PLANE_MAP) + 1):
    print("%s: %s" % (k, PLANE_MAP[k]))
plane_choice = read_int("Plane (1-3, default=1): ", min_value=1, max_value=3, default=1)
plane_str = PLANE_MAP[plane_choice]

offset = read_float("offset [a0] (default=0.0): ", default=0.0)
phi_deg = read_float("phi_deg (default=0.0): ", default=0.0)
phi_slice = phi_deg * pi / 180.0

R = read_float("R [a0] (0=auto, default=0.0): ", min_value=0.0, default=0.0)
k_scale = read_float("k_scale (default=1.5): ", min_value=1.0, max_value=3.0, default=1.5)
gamma = read_float("gamma (default=0.5): ", min_value=0.01, max_value=2.0, default=0.5)

print("Prob. Density Units:")
for k in range(1, len(UNIT_LABELS) + 1):
    print("%s: %s" % (k, UNIT_LABELS[k]))
unit_choice = read_int("Units (1-2, default=1): ", min_value=1, max_value=2, default=1)

print("Colour Maps:")
for idx in range(1, len(CMAP_REGISTRY) + 1):
    if idx in CMAP_REGISTRY:
        entry = CMAP_REGISTRY[idx]
        print("%s: %s" % (idx, entry[0]))
cm_choice = read_int("Map (1-8, default=6): ", min_value=1, max_value=8, default=6)
cm_str = CMAP_REGISTRY[cm_choice][0]

if R <= 0.0:
    R = get_R(n, l, Z, offset, k_scale)

wf = HydrogenicWavefunction(n, l, m, Z, M_kg, use_mu, phi_slice, plane_choice, offset, is_real=(basis_choice == 1))
unit_scale, unit_str = get_unit_map(wf)[unit_choice]
step = 2.0 * R / (SCR_H - PY - 1)
peak = get_peak_density(n, l, m, Z, wf.density_3d)

def main():
    clear_screen()

    hdr = format_hdr(n, l, m, Z, basis_str, plane_str, offset, cm_str, R, k_scale, phi_deg)
    draw_string(0, 0, hdr, (0, 0, 160), "small")

    sp, ss = set_pixel, show_screen
    get_coords, dens = wf.get_coords, wf.density_3d
    colour_lut, _ = generate_colour_lut(cm_choice, CMAP_REGISTRY)
    vmax, vmin = peak, 0.0

    for sy in range(SAMP):
        v = R - step * sy
        for sx in range(SAMP):
            u = -R + step * sx
            x3, y3, z3 = get_coords(u, v)
            d = dens(x3, y3, z3)
            ratio = max(0.0, min(1.0, (d - vmin) / (vmax - vmin))) if (vmax - vmin) > 0 else 0.0
            sp(sx, PY + sy, colour_lut[int((ratio**gamma) * 255.0)])
        ss()

    leg_den = LEG_H - 1 if LEG_H > 1 else 1
    for py in range(LEG_H):
        col = colour_lut[int((1.0 - py / leg_den) * 255.0)]
        for dx in range(LEG_W):
            sp(LEG_X + dx, PY + py, col)
        if py in (0, LEG_H - 1):
            for dx in range(LEG_W):
                sp(LEG_X + dx, PY + py, (0, 0, 0))
        sp(LEG_X, PY + py, (0, 0, 0))
        sp(LEG_X + LEG_W - 1, PY + py, (0, 0, 0))
        ss()

    for i in range(5):
        t = i / 4.0
        ty = PY + int((1.0 - t) * leg_den)
        for dx in range(3):
            sp(LEG_X + LEG_W + dx, ty, (0, 0, 0))
        t_row = 1.0 - (ty - PY) / leg_den
        norm_tick = t_row ** (1.0 / gamma + EPSILON) if t_row > 0.0 else 0.0
        d_tick = (vmin + norm_tick * (vmax - vmin)) / unit_scale
        draw_string(LEG_LABEL_X, max(PY, min(PY + LEG_H - 8, ty - 4)), "%s %s" % (fmt_density(d_tick), unit_str), (0, 0, 0), "small")
        ss()

    wait_for_exit()


main()
