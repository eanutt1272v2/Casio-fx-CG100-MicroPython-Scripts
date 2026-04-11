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

    f1 = float(input("Freq 1 (e.g. 5): "))
    f2 = float(input("Freq 2 (e.g. 5.5): "))
    A1 = float(input("Amplitude 1: "))
    A2 = float(input("Amplitude 2: "))

    N = 400
    T_end = 4.0 / min(f1, f2)
    ts = [T_end * i / N for i in range(N + 1)]

    y1 = [A1 * math.sin(2 * math.pi * f1 * t) for t in ts]
    y2 = [A2 * math.sin(2 * math.pi * f2 * t) for t in ts]
    ytot = [y1[i] + y2[i] for i in range(len(ts))]

    plot(ts, ytot, "blue")
    plot(ts, y1, "grey")
    plot(ts, y2, "grey")
    axis("auto")
    grid("on")
    text(0, max(ytot), "f1=" + str(f1) + " f2=" + str(f2))
    show()
    wait_for_exit()


main()
