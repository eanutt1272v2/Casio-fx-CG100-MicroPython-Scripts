# Solve congruence systems with the Chinese Remainder Theorem.

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


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y


def crt(remainders, moduli):
    M = 1
    for m in moduli:
        M *= m
    x = 0
    for idx in range(len(remainders)):
        r = remainders[idx]
        m = moduli[idx]
        Mi = M // m
        _, inv, _ = ext_gcd(Mi, m)
        inv %= m
        x += r * Mi * inv
    return x % M


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    n = read_int("Number of congruences: ")
    rs = []
    ms = []
    for i in range(n):
        r = read_int("r" + str(i + 1) + " (remainder): ")
        m = read_int("m" + str(i + 1) + " (modulus): ")
        rs.append(r)
        ms.append(m)

    ok = True
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(ms[i], ms[j]) != 1:
                print("Moduli not pairwise coprime!")
                ok = False

    if ok:
        x = crt(rs, ms)
        print("Solution: x =", x)
        M = 1
        for m in ms:
            M *= m
        print("(unique mod", M, ")")
    wait_for_exit()


main()
