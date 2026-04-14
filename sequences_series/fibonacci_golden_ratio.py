# Explore Fibonacci growth and the golden ratio.

from matplotlib.pyplot import axis, grid, plot, show, text
import math

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

    phi = (1 + math.sqrt(5)) / 2
    print("phi =", phi)

    a, b = 1, 1
    ratios = []
    fibs = [1, 1]
    for i in range(28):
        a, b = b, a + b
        fibs.append(b)
        ratios.append(b / a)

    xs = list(range(len(ratios)))
    phis = [phi] * len(ratios)

    plot(xs, ratios, "blue")
    plot(xs, phis, "red")
    axis([0, len(ratios), 1.5, 1.75])
    grid("on")
    text(0, 1.73, "F(n+1)/F(n) -> phi")
    text(0, phi + 0.005, "phi=1.618...")
    show()
    wait_for_exit()


main()
