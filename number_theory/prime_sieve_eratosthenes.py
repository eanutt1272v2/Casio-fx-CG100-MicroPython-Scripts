from matplotlib.pyplot import axis, bar, grid, show, text
import math

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
    return [i for i in range(2, n + 1) if is_p[i]]


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    N = 200
    primes = sieve(N)
    print("Count:", len(primes))
    print("Largest:", primes[-1])

    xs = list(range(len(primes)))
    bar(xs, primes, "blue")
    axis([0, len(primes), 0, N])
    grid("on", "grey")
    text(0, N - 15, "Primes up to " + str(N))
    show()
    wait_for_exit()


main()
