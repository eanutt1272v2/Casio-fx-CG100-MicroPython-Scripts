from matplotlib.pyplot import plot, axis, grid, text, show
from math import sin, cos, exp, log, atan

try:
    from casioplot import getkey
except ImportError:
    getkey = None


print("1=sin(x)  2=cos(x)  3=e^x  4=ln(1+x)  5=arctan(x)")
choice = input("> ")
N = int(input("Max terms N (e.g. 8): "))
a_str = input("x range: a to ")
a = float(a_str)
b = float(input("b: "))

pts = 200
xs = [a + (b - a) * i / pts for i in range(pts + 1)]


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


def maclaurin(x, n, choice):
    s = 0.0
    if choice == "1":
        for k in range(n):
            s += (-1) ** k * x ** (2 * k + 1) / factorial(2 * k + 1)
    elif choice == "2":
        for k in range(n):
            s += (-1) ** k * x ** (2 * k) / factorial(2 * k)
    elif choice == "3":
        for k in range(n):
            s += x**k / factorial(k)
    elif choice == "4":
        for k in range(1, n + 1):
            s += (-1) ** (k + 1) * x**k / k
    elif choice == "5":
        for k in range(n):
            s += (-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
    return s


def _true_fn(choice, x):
    if choice == "1":
        return sin(x)
    if choice == "2":
        return cos(x)
    if choice == "3":
        return exp(x)
    if choice == "4":
        return log(1 + x) if x > -1 else 0.0
    if choice == "5":
        return atan(x)
    return sin(x)


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    ys_true = [_true_fn(choice, x) for x in xs]
    ys_approx = [maclaurin(x, N, choice) for x in xs]
    ys_half = [maclaurin(x, max(1, N // 2), choice) for x in xs]

    ymin = min(min(ys_true), min(ys_approx)) - 0.5
    ymax = max(max(ys_true), max(ys_approx)) + 0.5
    ymin = max(ymin, -5)
    ymax = min(ymax, 5)

    plot(xs, ys_true, "blue")
    plot(xs, ys_approx, "red")
    plot(xs, ys_half, "grey")
    axis([a, b, ymin, ymax])
    grid("on")
    fnames = {"1": "sin", "2": "cos", "3": "e^x", "4": "ln(1+x)", "5": "arctan"}
    text(a, ymax - 0.4, fnames.get(choice, "f") + " (blue=true red=N=" + str(N) + ")")
    show()
    wait_for_exit()


main()
