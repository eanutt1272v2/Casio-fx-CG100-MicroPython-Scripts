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
    f1 = read_float("Freq 1 (e.g. 5): ")
    f2 = read_float("Freq 2 (e.g. 5.5): ")
    A1 = read_float("Amplitude 1: ")
    A2 = read_float("Amplitude 2: ")

    N = 400
    T_end = 4.0 / min(f1, f2)
    ts = [T_end * i / N for i in range(N + 1)]

    y1 = [A1 * math.sin(2 * math.pi * f1 * t) for t in ts]
    y2 = [A2 * math.sin(2 * math.pi * f2 * t) for t in ts]
    ytot = [y1[i] + y2[i] for i in range(len(ts))]

    plot(ts, ytot, "blue")
    plot(ts, y1, "grey")
    plot(ts, y2, "grey")
    axis("auto")
    grid("on")
    text(0, max(ytot), "f1=" + str(f1) + " f2=" + str(f2))
    show()
    wait_for_exit()


main()
