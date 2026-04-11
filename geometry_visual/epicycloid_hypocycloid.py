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
    R = read_float("R (large circle): ")
    r = read_float("r (small circle): ")
    mode = read_text("Type: e=epi, h=hypo: ")

    N = 800
    ts = [2 * math.pi * i / N for i in range(N + 1)]

    if mode == "e":
        xs = [(R + r) * math.cos(t) - r * math.cos((R + r) * t / r) for t in ts]
        ys = [(R + r) * math.sin(t) - r * math.sin((R + r) * t / r) for t in ts]
        title = "Epicycloid R=" + str(R) + " r=" + str(r)
    else:
        xs = [(R - r) * math.cos(t) + r * math.cos((R - r) * t / r) for t in ts]
        ys = [(R - r) * math.sin(t) - r * math.sin((R - r) * t / r) for t in ts]
        title = "Hypocycloid R=" + str(R) + " r=" + str(r)

    plot(xs, ys, "purple")
    axis("auto")
    text(min(xs), max(ys), title)
    show()
    wait_for_exit()


main()
