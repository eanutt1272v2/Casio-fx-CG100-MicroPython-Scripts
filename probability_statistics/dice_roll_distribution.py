from matplotlib.pyplot import axis, bar, grid, show, text
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

    M = int(input("Rolls M (e.g. 300): "))
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
