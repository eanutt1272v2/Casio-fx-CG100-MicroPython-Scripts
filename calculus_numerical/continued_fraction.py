# Evaluate and explore continued fractions.

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


def cont_frac(x, steps=12):
    coeffs = []
    for _ in range(steps):
        a = int(x)
        coeffs.append(a)
        frac = x - a
        if abs(frac) < 1e-9:
            break
        x = 1.0 / frac
    return coeffs


def convergents(coeffs):
    h_prev, h = 1, coeffs[0]
    k_prev, k = 0, 1
    print("n  coeff  h/k (convergent)")
    print(0, "    ", coeffs[0], "     ", h, "/", k)
    for i in range(1, len(coeffs)):
        h_prev, h = h, coeffs[i] * h + h_prev
        k_prev, k = k, coeffs[i] * k + k_prev
        print(i, "    ", coeffs[i], "     ", h, "/", k)


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    x = read_float("Def x (e.g. 3.14159..): ")
    cf = cont_frac(x, 10)
    print("CF:", cf)
    convergents(cf)
    wait_for_exit()


main()
