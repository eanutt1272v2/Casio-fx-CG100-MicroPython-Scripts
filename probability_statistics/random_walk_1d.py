# Simulate a one-dimensional random walk.

from matplotlib.pyplot import axis, plot, show, text
import math
import random

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
    N = read_int("Steps N: ", min_value=1)
    pos = 0
    positions = [0]

    for _ in range(N):
        pos += 1 if random.random() > 0.5 else -1
        positions.append(pos)

    rms = math.sqrt(N)
    xs = list(range(N + 1))
    plot(xs, positions, "blue")
    plot([0, N], [rms, rms], "red")
    plot([0, N], [-rms, -rms], "red")
    axis([0, N, -rms * 2, rms * 2])
    text(0, rms + 0.5, "+sqrt(N)")
    text(0, -rms - 4, "-sqrt(N)")
    show()
    wait_for_exit()


main()
