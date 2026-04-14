# Synthesize signals with Fourier components.

from matplotlib.pyplot import plot, axis, grid, text, show
import math

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def read_text(prompt, default=None):
    while True:
        raw = input(prompt).strip()
        if raw:
            return raw
        if default is not None:
            return default
        print("Please enter a value.")


def read_int(prompt, default=None, min_value=None, max_value=None):
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            value = default
        else:
            try:
                value = int(raw)
            except ValueError:
                print("Invalid integer. Try again.")
                continue
        if min_value is not None and value < min_value:
            print("Value must be >= " + str(min_value))
            continue
        if max_value is not None and value > max_value:
            print("Value must be <= " + str(max_value))
            continue
        return value


def read_float(prompt, default=None, min_value=None, max_value=None):
    while True:
        raw = input(prompt).strip()
        if raw == "" and default is not None:
            value = default
        else:
            try:
                value = float(raw)
            except ValueError:
                print("Invalid number. Try again.")
                continue
        if min_value is not None and value < min_value:
            print("Value must be >= " + str(min_value))
            continue
        if max_value is not None and value > max_value:
            print("Value must be <= " + str(max_value))
            continue
        return value


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():

    N = read_int("Harmonics N (e.g. 10): ")
    print("1=Square  2=Sawtooth  3=Triangle  4=Custom")
    choice = read_text("> ")

    L = math.pi
    pts = 300
    xs = [2 * math.pi * i / pts - math.pi for i in range(pts + 1)]

    if choice == "1":

        ys = [sum(4 / math.pi * math.sin((2 * k - 1) * x) / (2 * k - 1) for k in range(1, N + 1)) for x in xs]
        lbl = "Square wave N=" + str(N)
    elif choice == "2":

        ys = [sum(2 / math.pi * ((-1) ** (k + 1)) * math.sin(k * x) / k for k in range(1, N + 1)) for x in xs]
        lbl = "Sawtooth N=" + str(N)
    elif choice == "3":

        ys = [sum(8 / math.pi**2 * ((-1) ** k) * math.sin((2 * k + 1) * x) / (2 * k + 1) ** 2 for k in range(N)) for x in xs]
        lbl = "Triangle N=" + str(N)
    else:

        print("Enter a0,a1..aN (cos coeffs) then b1..bN (sin coeffs)")
        a0 = read_float("a0: ")
        acoeffs = [read_float("a" + str(k) + ": ") for k in range(1, N + 1)]
        bcoeffs = [read_float("b" + str(k) + ": ") for k in range(1, N + 1)]
        ys = [a0 / 2 + sum(acoeffs[k - 1] * math.cos(k * x) + bcoeffs[k - 1] * math.sin(k * x) for k in range(1, N + 1)) for x in xs]
        lbl = "Custom Fourier N=" + str(N)

    ys_half = (
        [sum(4 / math.pi * math.sin((2 * k - 1) * x) / (2 * k - 1) for k in range(1, N // 2 + 1)) for x in xs] if choice == "1" else ys
    )

    plot(xs, ys, "blue")
    axis([-math.pi, math.pi, min(ys) * 1.2, max(ys) * 1.2])
    grid("on")
    text(-math.pi + 0.1, max(ys) * 0.9, lbl)
    text(-math.pi + 0.1, max(ys) * 0.75, "Gibbs phenomenon visible at discontinuities")
    show()
    wait_for_exit()


main()
