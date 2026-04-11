try:
    from casioplot import getkey
except ImportError:
    getkey = None


def f(x):
    return x**3 - 2 * x - 5


def df(x):
    return 3 * x**2 - 2


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    x0 = float(input("Initial guess x0: "))
    tol = 1e-10
    max_iter = 50

    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-15:
            print("Derivative near zero. Stopping.")
            break
        x_new = x - fx / dfx
        print("Iter", i + 1, ": x =", x_new, "  f(x) =", f(x_new))
        if abs(x_new - x) < tol:
            print("Converged after", i + 1, "iterations.")
            break
        x = x_new

    print("Root ~", x)
    wait_for_exit()


main()
