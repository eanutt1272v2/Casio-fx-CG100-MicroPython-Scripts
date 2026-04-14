# Draw polar rose curves.

from matplotlib.pyplot import axis, grid, plot, show, text
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
    k = read_float("k (e.g. 3 or 2.5): ")
    N = 600
    step = 2 * math.pi / N if int(k) == k else 4 * math.pi / N

    ts = [step * i for i in range(N + 1)]
    xs = [math.cos(k * t) * math.cos(t) for t in ts]
    ys = [math.cos(k * t) * math.sin(t) for t in ts]

    plot(xs, ys, "red")
    axis([-1.2, 1.2, -1.2, 1.2])
    grid("on")
    text(-1.1, 1.1, "r=cos(" + str(k) + "*theta)")
    show()
    wait_for_exit()


main()
