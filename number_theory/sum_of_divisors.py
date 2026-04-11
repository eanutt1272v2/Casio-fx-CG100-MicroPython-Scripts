try:
    from casioplot import getkey
except ImportError:
    getkey = None


def sigma(n):
    total = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total


def classify(n):
    s = sigma(n)
    if s == 2 * n:
        return "PERFECT"
    elif s > 2 * n:
        return "Abundant"
    else:
        return "Deficient"


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    n = int(input("n: "))
    s = sigma(n)
    print("sigma(n) =", s)
    print("2n =", 2 * n)
    print("Classification:", classify(n))

    print("\nChecking 1-1000 for perfect:")
    for k in range(2, 1001):
        if sigma(k) == 2 * k:
            print(k, end=" ")
    wait_for_exit()


main()
