from matplotlib.pyplot import plot, axis, grid, text, show
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

    N = int(input("Harmonics N (e.g. 10): "))
    print("1=Square  2=Sawtooth  3=Triangle  4=Custom")
    choice = input("> ")

    L = math.pi
    pts = 300
    xs = [2 * math.pi * i / pts - math.pi for i in range(pts + 1)]

    if choice == "1":

        ys = [
            sum(
                4 / math.pi * math.sin((2 * k - 1) * x) / (2 * k - 1)
                for k in range(1, N + 1)
            )
            for x in xs
        ]
        lbl = "Square wave N=" + str(N)
    elif choice == "2":

        ys = [
            sum(
                2 / math.pi * ((-1) ** (k + 1)) * math.sin(k * x) / k
                for k in range(1, N + 1)
            )
            for x in xs
        ]
        lbl = "Sawtooth N=" + str(N)
    elif choice == "3":

        ys = [
            sum(
                8
                / math.pi**2
                * ((-1) ** k)
                * math.sin((2 * k + 1) * x)
                / (2 * k + 1) ** 2
                for k in range(N)
            )
            for x in xs
        ]
        lbl = "Triangle N=" + str(N)
    else:

        print("Enter a0,a1..aN (cos coeffs) then b1..bN (sin coeffs)")
        a0 = float(input("a0: "))
        acoeffs = [float(input("a" + str(k) + ": ")) for k in range(1, N + 1)]
        bcoeffs = [float(input("b" + str(k) + ": ")) for k in range(1, N + 1)]
        ys = [
            a0 / 2
            + sum(
                acoeffs[k - 1] * math.cos(k * x) + bcoeffs[k - 1] * math.sin(k * x)
                for k in range(1, N + 1)
            )
            for x in xs
        ]
        lbl = "Custom Fourier N=" + str(N)

    ys_half = (
        [
            sum(
                4 / math.pi * math.sin((2 * k - 1) * x) / (2 * k - 1)
                for k in range(1, N // 2 + 1)
            )
            for x in xs
        ]
        if choice == "1"
        else ys
    )

    plot(xs, ys, "blue")
    axis([-math.pi, math.pi, min(ys) * 1.2, max(ys) * 1.2])
    grid("on")
    text(-math.pi + 0.1, max(ys) * 0.9, lbl)
    text(-math.pi + 0.1, max(ys) * 0.75, "Gibbs phenomenon visible at discontinuities")
    show()
    wait_for_exit()


main()
