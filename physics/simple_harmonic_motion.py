# Model simple harmonic motion.

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
    A = read_float("Amplitude A: ")
    omega = read_float("Angular freq omega: ")
    phi = read_float("Phase phi (degrees): ")
    phi = phi * math.pi / 180

    T = 2 * math.pi / omega
    N = 300
    ts = [3 * T * i / N for i in range(N + 1)]

    xs = [A * math.cos(omega * t + phi) for t in ts]
    vs = [-A * omega * math.sin(omega * t + phi) for t in ts]
    accs = [-A * omega**2 * math.cos(omega * t + phi) for t in ts]

    plot(ts, xs, "blue")
    plot(ts, vs, "red")
    plot(ts, accs, "green")
    axis("auto")
    grid("on")
    text(0, A, "x(t) blue, v(t) red, a(t) green")
    show()
    wait_for_exit()


main()
