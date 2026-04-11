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
    a = read_float("a (e.g. 3): ")
    b = read_float("b (e.g. 2): ")
    delta = read_float("delta in degrees (e.g. 90): ")
    delta = delta * math.pi / 180

    N = 500
    ts = [2 * math.pi * i / N for i in range(N + 1)]
    xs = [math.sin(a * t + delta) for t in ts]
    ys = [math.sin(b * t) for t in ts]

    plot(xs, ys, "blue")
    axis([-1.2, 1.2, -1.2, 1.2])
    grid("on")
    text(
        -1.1,
        1.1,
        "a=" + str(a) + " b=" + str(b) + " d=" + str(int(delta * 180 / math.pi)),
    )
    show()
    wait_for_exit()


main()
