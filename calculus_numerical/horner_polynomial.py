def horner(coeffs, x):

    result = 0
    for c in coeffs:
        result = result * x + c
    return result


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    raw = read_text("Coefficients (highest to lowest, comma-sep): ")
    coeffs = [float(c) for c in raw.split(",")]
    x = read_float("Evaluate at x: ")
    result = horner(coeffs, x)
    print("p(x) =", result)

    from matplotlib.pyplot import axis, grid, plot, show, text

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

    a_val = read_float("Plot from x=: ")
    b_val = read_float("         to x=: ")
    xs = [a_val + (b_val - a_val) * i / 200 for i in range(201)]
    ys = [horner(coeffs, xi) for xi in xs]
    plot(xs, ys, "blue")
    axis("auto")
    grid("on")
    text(a_val, max(ys), "p(x)")
    show()
    wait_for_exit()


main()
