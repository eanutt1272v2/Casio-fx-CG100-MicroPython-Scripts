# Generate harmonograph-style drawings.

from matplotlib.pyplot import axis, plot, show, text
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
    f1 = read_float("Freq 1 (e.g. 2.01): ")
    f2 = read_float("Freq 2 (e.g. 3.0): ")
    d = read_float("Damping (e.g. 0.002): ")
    p = read_float("Phase diff (degrees): ")
    p = p * math.pi / 180

    N = 800
    T = 50.0
    ts = [T * i / N for i in range(N + 1)]

    xs = [math.exp(-d * t) * math.sin(2 * math.pi * f1 * t) for t in ts]
    ys = [math.exp(-d * t) * math.sin(2 * math.pi * f2 * t + p) for t in ts]

    plot(xs, ys, "blue")
    axis([-1.1, 1.1, -1.1, 1.1])
    text(-1.0, 1.0, "Harmonograph")
    show()
    wait_for_exit()


main()
