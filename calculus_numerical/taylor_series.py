# Approximate functions with Taylor series expansions.

from matplotlib.pyplot import plot, axis, grid, text, show
from math import sin, cos, exp, log, atan

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


print("1=sin(x)  2=cos(x)  3=e^x  4=ln(1+x)  5=arctan(x)")
choice = read_text("> ")
N = read_int("Max terms N (e.g. 8): ")
a_str = read_text("x range: a to ")
a = float(a_str)
b = read_float("b: ")

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
