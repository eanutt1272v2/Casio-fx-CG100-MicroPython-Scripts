# Visualise hydrogenic wavefunctions on Casio fx-CG100.

from casioplot import clear_screen, draw_string, set_pixel, show_screen
from math import sqrt, log, exp, pi, cos, sin

from psi_pico_support import CMAPS, cmap, fmt_density, lgamma, read_float, read_int, wait_for_exit

try:
    from casioplot import getkey
except ImportError:
    getkey = None


n = read_int("n (1..k): ", min_value=1)
l = read_int("l (0..n-1): ", min_value=0, max_value=n - 1)
m = read_int("m (-l..l): ", min_value=-l, max_value=l)
phi_deg = read_float("phi_deg (real Ylm, default=33): ", default=33.0)
phi_slice = phi_deg * pi / 180.0
Z = read_float("Z (1=H): ")
R = read_float("R [a0] (0=auto): ")
exposure = read_float("exposure (0=natural): ")

print("CMAPS:")
for i in range(len(CMAPS)):
    print(str(i + 1) + " " + CMAPS[i][0])
cm_idx = read_int("Select (1-" + str(len(CMAPS)) + "): ") - 1
if cm_idx < 0 or cm_idx >= len(CMAPS):
    cm_idx = 0
cm_name, RC, GC, BC = CMAPS[cm_idx]

if Z <= 0.0:
    Z = 1.0

if R <= 0.0:
    r_exp = (3.0 * n * n - l * (l + 1)) / (2.0 * Z)
    if r_exp <= 0.0:
        r_exp = 3.0 * n * n / Z
    R = 1.75 * r_exp
else:
    R = R

SCR_H = 190
PY = 10
SZ = SCR_H - PY
SAMP = SZ
LEG_X = SZ + 4
LEG_W = 10
LEG_LABEL_X = LEG_X + LEG_W + 2
LEG_H = SZ

a0 = 1.0
EPS = 1e-30
A0_M = 5.29177210903e-11
A0_3 = A0_M * A0_M * A0_M

p_rad = n - l - 1
alpha_l = 2 * l + 1
rho_k = 2.0 * Z / (n * a0)
log_norm_r = 0.5 * (3 * log(rho_k) + lgamma(n - l) - log(2.0 * n) - lgamma(n + l + 1))
log_norm_y = 0.5 * (log((2 * l + 1) / (4 * pi)) + lgamma(l - m + 1) - lgamma(l + m + 1))
if m != 0:
    log_norm_y += 0.5 * log(2.0)
y_norm = exp(log_norm_y)


def al(ll, mm, x):
    pmm = 1.0
    if mm > 0:
        xx = 1.0 - x * x
        if xx < 0.0:
            xx = 0.0
        s = sqrt(xx)
        fact = 1.0
        for i in range(1, mm + 1):
            pmm *= -fact * s
            fact += 2.0
    if ll == mm:
        return pmm
    pmmp1 = x * (2 * mm + 1) * pmm
    if ll == mm + 1:
        return pmmp1
    for lll in range(mm + 2, ll + 1):
        pll = (x * (2 * lll - 1) * pmmp1 - (lll + mm - 1) * pmm) / (lll - mm)
        pmm = pmmp1
        pmmp1 = pll
    return pmmp1


def al_signed(ll, mm, x):
    if mm >= 0:
        return al(ll, mm, x)
    mp = -mm
    sign = -1.0 if (mp % 2) else 1.0
    scale = sign * exp(lgamma(ll - mp + 1) - lgamma(ll + mp + 1))
    return scale * al(ll, mp, x)


def lag(p, alp, x):
    if p < 0:
        return 0.0
    L0 = 1.0
    if p == 0:
        return L0
    L1 = 1.0 + alp - x
    if p == 1:
        return L1
    for k in range(1, p):
        L2 = ((2 * k + 1 + alp - x) * L1 - (k + alp) * L0) / (k + 1)
        L0, L1 = L1, L2
    return L1


def density(x_c, z_c):
    r2 = x_c * x_c + z_c * z_c
    if r2 <= 1e-24:
        if l != 0:
            return 0.0
        rv = exp(log_norm_r) * lag(p_rad, alpha_l, 0.0)
        yv = y_norm * al_signed(l, m, 1.0)
        d = rv * yv
        return d * d
    r = sqrt(r2)
    rho = rho_k * r
    ea = -0.5 * rho + (l * log(rho) if l > 0 else 0.0)
    if ea < -700.0:
        return 0.0
    rv = exp(log_norm_r + ea) * lag(p_rad, alpha_l, rho)
    ct = z_c / r
    if ct < -1.0:
        ct = -1.0
    elif ct > 1.0:
        ct = 1.0

    p = al_signed(l, m, ct)
    if m == 0:
        yv = y_norm * p
    else:
        phi_loc = phi_slice if x_c >= 0.0 else phi_slice + pi
        if m > 0:
            yv = y_norm * p * cos(m * phi_loc)
        else:
            yv = y_norm * p * sin((-m) * phi_loc)

    d = rv * yv
    return d * d


step = 2.0 * R / (SAMP - 1)
peak = EPS
for sy in range(SAMP):
    z_c = R - step * sy
    for sx in range(SAMP):
        x_c = -R + step * sx
        d = density(x_c, z_c)
        if d > peak:
            peak = d

if exposure >= -0.99:
    gamma = 1.0 / (1.0 + exposure)
else:
    gamma = 100.0


def main():
    clear_screen()

    Zs = str(int(Z)) if Z == int(Z) else str(Z)
    hdr = (
        "Psi | n="
        + str(n)
        + " l="
        + str(l)
        + " m="
        + str(m)
        + " Z="
        + Zs
        + " cmap="
        + cm_name
        + " R="
        + str(R)
        + " [a0] exposure="
        + str(exposure)
        + " phi="
        + str(phi_deg)
        + "deg"
    )
    draw_string(0, 0, hdr, (0, 0, 160), "small")

    sp = set_pixel
    ss = show_screen

    for sy in range(SAMP):
        z_c = R - step * sy
        py = PY + sy
        for sx in range(SAMP):
            x_c = -R + step * sx
            d = density(x_c, z_c)
            norm = d / peak
            if norm < 0.0:
                norm = 0.0
            elif norm > 1.0:
                norm = 1.0
            val = norm**gamma
            sp(sx, py, cmap(val, RC, GC, BC))
        ss()

    leg_den = LEG_H - 1 if LEG_H > 1 else 1
    for py in range(LEG_H):
        t = 1.0 - py / leg_den
        col = cmap(t, RC, GC, BC)
        for dx in range(LEG_W):
            sp(LEG_X + dx, PY + py, col)

    for i in range(5):
        t = i / 4.0
        ty = PY + int((1.0 - t) * leg_den)
        sp(LEG_X + LEG_W, ty, (0, 0, 0))
        sp(LEG_X + LEG_W + 1, ty, (0, 0, 0))
        t_row = 1.0 - (ty - PY) / leg_den
        if t_row <= 0.0:
            d_tick = 0.0
        else:
            d_tick = peak * (t_row ** (1.0 / gamma)) / A0_3
        label = fmt_density(d_tick) + " [m^-3]"
        ly = ty - 4
        if ly < PY:
            ly = PY
        if ly > PY + LEG_H - 8:
            ly = PY + LEG_H - 8
        draw_string(LEG_LABEL_X, ly, label, (0, 0, 0), "small")

    ss()
    wait_for_exit(getkey)


main()
