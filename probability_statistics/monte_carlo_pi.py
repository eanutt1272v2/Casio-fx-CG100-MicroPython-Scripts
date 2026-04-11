import random
from matplotlib.pyplot import axis, scatter, show, text

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
    N = read_int("Samples N (e.g. 500): ")
    inside = 0
    xs_in, ys_in = [], []
    xs_out, ys_out = [], []

    for _ in range(N):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside += 1
            xs_in.append(x)
            ys_in.append(y)
        else:
            xs_out.append(x)
            ys_out.append(y)

    pi_est = 4 * inside / N
    print("pi estimate:", pi_est)
    print("Error:", abs(pi_est - 3.14159265))

    scatter(xs_in, ys_in)
    scatter(xs_out, ys_out)
    axis([0, 1, 0, 1])
    text(0, 0.95, "pi~" + str(round(pi_est, 4)))
    show()
    wait_for_exit()


main()
