from matplotlib.pyplot import axis, plot, show, text
import random

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():

    N = int(input("Samples N (e.g. 200): "))
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
