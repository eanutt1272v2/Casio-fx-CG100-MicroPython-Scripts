# Calculate pendulum period from system parameters.

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
    g = 9.81
    Ls = [0.05 + 0.05 * i for i in range(40)]
    Ts_exact = [2 * math.pi * math.sqrt(L / g) for L in Ls]
    Ts_approx = Ts_exact

    theta = read_float("Initial angle (degrees): ")
    theta_r = theta * math.pi / 180
    Ts_large = [2 * math.pi * math.sqrt(L / g) * (1 + theta_r**2 / 16) for L in Ls]

    plot(Ls, Ts_exact, "blue")
    plot(Ls, Ts_large, "red")
    axis([0, max(Ls) * 1.1, 0, max(Ts_large) * 1.1])
    grid("on")
    text(0, max(Ts_large) * 0.95, "blue: small-angle  red: large-angle corr")
    show()
    wait_for_exit()


main()
