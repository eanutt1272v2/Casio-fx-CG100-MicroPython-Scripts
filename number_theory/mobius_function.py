# Compute values of the Mobius function.

from casioplot import clear_screen, draw_string, set_pixel, show_screen
import math

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def mobius(n):
    if n == 1:
        return 1
    factors = 0
    p = 2
    while p <= int(math.sqrt(n)) + 1:
        if n % p == 0:
            factors += 1
            n //= p
            if n % p == 0:
                return 0
        p += 1
    if n > 1:
        factors += 1
    return (-1) ** factors


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    clear_screen()
    draw_string(0, 0, "Mobius mu(n): green=1 red=-1 grey=0")
    for n in range(1, 151):
        m = mobius(n)
        col = (0, 180, 0) if m == 1 else (200, 0, 0) if m == -1 else (160, 160, 160)
        x = ((n - 1) % 50) * 7 + 2
        y = ((n - 1) // 50) * 20 + 18
        for dx in range(5):
            for dy in range(14):
                set_pixel(x + dx, y + dy, col)
        if n % 50 == 0 or n == 150:
            pass

    show_screen()
    wait_for_exit()


main()
