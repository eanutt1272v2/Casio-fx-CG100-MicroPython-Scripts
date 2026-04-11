try:
    from casioplot import getkey
except ImportError:
    getkey = None


def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    n = int(input("n: "))
    print("Happy:", is_happy(n))

    print("\nHappy numbers 1-100:")
    happy = [n for n in range(1, 101) if is_happy(n)]
    print(happy)
    wait_for_exit()


main()
