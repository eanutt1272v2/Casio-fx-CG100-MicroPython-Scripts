import math

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def factorise(n):
    factors = {}
    if n < 2:
        return factors
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    i = 3
    while i <= int(math.sqrt(n)) + 1:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    n = int(input("Factorise n: "))
    f = factorise(n)
    result = ""
    for p in sorted(f.keys()):
        result += str(p) + "^" + str(f[p]) + " * "
    print(result[:-3] if result else str(n) + " is 1")
    wait_for_exit()


main()
