from matplotlib.pyplot import plot, axis, grid, text, scatter, show
import math

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def cmod(re, im):
    return math.sqrt(re * re + im * im)


def carg(re, im):
    return math.atan2(im, re)


def cmul(a, b, c, d):
    return (a * c - b * d, a * d + b * c)


def cdiv(a, b, c, d):
    denom = c * c + d * d
    return ((a * c + b * d) / denom, (b * c - a * d) / denom)


def cpow(r, im, n):
    mod = cmod(r, im)
    arg = carg(r, im)
    return (mod**n * math.cos(n * arg), mod**n * math.sin(n * arg))


def fmt(x):
    return round(x, 5)


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    while True:
        print("1=Convert polar/rect  2=Multiply  3=Divide")
        print("4=De Moivre z^n  5=nth roots of unity  0=quit")
        m = input("> ")
        if m == "0":
            break
        if m == "1":
            raw = input("z = a+bi, enter a,b: ").split(",")
            a, b = float(raw[0]), float(raw[1])
            r = cmod(a, b)
            theta = carg(a, b)
            print("Mod=", fmt(r), "Arg=", fmt((theta) * 180 / math.pi), "deg")
            print(
                "Polar: "
                + str(fmt(r))
                + "(cos"
                + str(fmt((theta) * 180 / math.pi))
                + "+ i sin...)"
            )
            conj = (a, -b)
            print("Conjugate=", a, "-", abs(b), "i")
            plot([0, a], [0, b], "blue")
            scatter([a], [b])
            plot([-2, 2], [0, 0], "grey")
            plot([0, 0], [-2, 2], "grey")
            text(a, b, "z")
            axis([-r * 1.5, r * 1.5, -r * 1.5, r * 1.5])
            show()
        elif m == "2":
            raw = input("z1 = a,b: ").split(",")
            a, b = float(raw[0]), float(raw[1])
            raw = input("z2 = c,d: ").split(",")
            c, d = float(raw[0]), float(raw[1])
            re, im = cmul(a, b, c, d)
            print("z1*z2 =", fmt(re), "+", fmt(im), "i")
            print("Mod =", fmt(cmod(re, im)))
        elif m == "3":
            raw = input("z1 = a,b: ").split(",")
            a, b = float(raw[0]), float(raw[1])
            raw = input("z2 = c,d: ").split(",")
            c, d = float(raw[0]), float(raw[1])
            re, im = cdiv(a, b, c, d)
            print("z1/z2 =", fmt(re), "+", fmt(im), "i")
        elif m == "4":
            raw = input("z = a,b: ").split(",")
            a, b = float(raw[0]), float(raw[1])
            n = int(input("n: "))
            re, im = cpow(a, b, n)
            print("z^" + str(n) + " =", fmt(re), "+", fmt(im), "i")
            print(
                "De Moivre: |z|^n=",
                fmt(cmod(a, b) ** n),
                " arg*n=",
                fmt((carg(a, b) * 180 / math.pi * n)),
                "deg",
            )
        elif m == "5":
            n = int(input("n-th roots of unity: "))
            xs = [math.cos(2 * math.pi * k / n) for k in range(n)]
            ys = [math.sin(2 * math.pi * k / n) for k in range(n)]
            ts = [2 * math.pi * i / 100 for i in range(101)]
            plot([math.cos(t) for t in ts], [math.sin(t) for t in ts], "grey")
            scatter(xs, ys)
            for k in range(n):
                plot([0, xs[k]], [0, ys[k]], "blue")
                text(xs[k], ys[k], "w" + str(k))
            axis([-1.4, 1.4, -1.4, 1.4])
            grid("on")
            show()
        input("EXE")
    wait_for_exit()


main()
