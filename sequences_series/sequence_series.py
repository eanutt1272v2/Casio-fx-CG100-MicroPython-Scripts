# Work with general sequences and series.

from matplotlib.pyplot import plot, axis, grid, text, show

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

    while True:
        print("1=AP  2=GP  3=Recurrence  4=Series sums  0=quit")
        mode = read_text("> ")
        if mode == "0":
            break
        if mode == "1":
            a = read_float("First term a: ")
            d = read_float("Common diff d: ")
            n = read_int("Number of terms n: ")
            terms = [a + d * i for i in range(n)]
            Sn = n / 2 * (2 * a + (n - 1) * d)
            print("a_n =", round(terms[-1], 6))
            print("S_n =", round(Sn, 6))
            print("Formula: a +", d, "(n-1)")
            xs = list(range(1, n + 1))
            plot(xs, terms, "blue")
            axis([0, n + 1, min(terms) - 1, max(terms) + 1])
            text(1, terms[0], "AP a=" + str(a) + " d=" + str(d))
            grid("on")
            show()
        elif mode == "2":
            a = read_float("First term a: ")
            r = read_float("Common ratio r: ")
            n = read_int("Number of terms n: ")
            terms = [a * r**i for i in range(n)]
            if abs(r) != 1:
                Sn = a * (1 - r**n) / (1 - r)
            else:
                Sn = a * n
            print("a_n =", round(terms[-1], 8))
            print("S_n =", round(Sn, 8))
            if abs(r) < 1:
                print("S_inf =", round(a / (1 - r), 8))
            xs = list(range(1, n + 1))
            plot(xs, terms, "red")
            axis([0, n + 1, min(terms) - abs(min(terms)) * 0.1, max(terms) * 1.1])
            text(1, terms[0], "GP a=" + str(a) + " r=" + str(r))
            grid("on")
            show()
        elif mode == "3":
            print("Define u(n) in terms of u(n-1). e.g. Fibonacci")
            a0 = read_float("u(0): ")
            a1 = read_float("u(1): ")
            n = read_int("Terms to compute: ")

            coeff1 = read_float("coeff of u(n-1) (e.g.1 for Fib): ")
            coeff2 = read_float("coeff of u(n-2) (e.g.1 for Fib): ")
            const = read_float("constant term (0 for Fib): ")
            terms = [a0, a1]
            for i in range(2, n):
                terms.append(coeff1 * terms[-1] + coeff2 * terms[-2] + const)
            print("Last 5:", terms[-5:])
            xs = list(range(n))
            plot(xs, terms, "green")
            axis("auto")
            grid("on")
            text(0, terms[0], "Recurrence")
            show()
        elif mode == "4":
            print("Known series sums:")
            n = read_int("n: ")
            print("Sum 1..n =", n * (n + 1) // 2)
            print("Sum 1^2..n^2 =", n * (n + 1) * (2 * n + 1) // 6)
            print("Sum 1^3..n^3 =", (n * (n + 1) // 2) ** 2)
            print("Sum k*r^(k-1) geometric deriv:")
            r = read_float("r (for sum k*r^k): ")
            if abs(r) < 1:
                print("Sum k*r^k (inf) =", r / (1 - r) ** 2)
            s = sum(k * r**k for k in range(1, n + 1))
            print("Sum k*r^k to n =", round(s, 6))
        input("EXE")
    wait_for_exit()


main()
