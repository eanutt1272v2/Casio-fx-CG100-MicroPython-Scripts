# Demonstrate the law of large numbers.

from matplotlib.pyplot import axis, plot, show, text
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
    N = read_int("Samples N (e.g. 200): ")
    total = 0
    avgs = []

    for i in range(1, N + 1):
        total += random.random()
        avgs.append(total / i)

    xs = list(range(1, N + 1))
    means = [0.5] * N

    plot(xs, avgs, "blue")
    plot(xs, means, "red")
    axis([1, N, 0.2, 0.8])
    text(1, 0.78, "Running mean -> 0.5")
    show()
    wait_for_exit()


main()
