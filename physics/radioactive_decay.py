# Model exponential radioactive decay.

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
    N0 = read_float("Initial amount N0: ")
    half_life = read_float("Half-life T_1/2: ")
    lam = math.log(2) / half_life
    T_end = 5 * half_life

    N = 300
    ts = [T_end * i / N for i in range(N + 1)]
    Ns = [N0 * math.exp(-lam * t) for t in ts]

    plot(ts, Ns, "blue")

    plot([half_life, half_life], [0, N0 / 2], "red")
    plot([0, half_life], [N0 / 2, N0 / 2], "red")
    axis([0, T_end, 0, N0 * 1.05])
    grid("on")
    text(0, N0, "N0=" + str(N0) + " T1/2=" + str(half_life))
    text(half_life, N0 * 0.1, "T_1/2")
    show()
    wait_for_exit()


main()
