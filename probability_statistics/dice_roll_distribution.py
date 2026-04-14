# Simulate and summarize dice-roll distributions.

from matplotlib.pyplot import axis, bar, grid, show, text
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
    M = read_int("Rolls M (e.g. 300): ")
    counts = [0] * 13

    for _ in range(M):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        counts[d1 + d2] += 1

    xs = list(range(2, 13))
    ys = counts[2:]
    bar(xs, ys, "blue")
    axis([1, 13, 0, max(ys) * 1.2])
    grid("on")
    text(2, max(ys), "2d6 rolls: " + str(M))
    show()
    wait_for_exit()


main()
