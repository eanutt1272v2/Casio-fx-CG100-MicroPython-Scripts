from matplotlib.pyplot import axis, grid, plot, show, text

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def collatz(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    start = int(input("Starting integer: "))
    seq = collatz(start)
    print("Steps:", len(seq) - 1)
    print("Max value:", max(seq))

    xs = list(range(len(seq)))
    plot(xs, seq, "blue")
    axis("auto")
    grid("on")
    text(
        0, max(seq) - max(seq) // 10, "n=" + str(start) + " steps=" + str(len(seq) - 1)
    )
    show()
    wait_for_exit()


main()
