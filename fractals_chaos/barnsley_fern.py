from casioplot import clear_screen, set_pixel, show_screen
import random

def ifs(x, y):
    r = random.random()
    if r < 0.01:
        return 0, 0.16*y
    elif r < 0.86:
        return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6
    elif r < 0.93:
        return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6
    else:
        return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

clear_screen()
x, y = 0.0, 0.0
N = int(input("Points (e.g. 5000): "))

for _ in range(N):
    x, y = ifs(x, y)
    px = int((x + 2.5) / 5.0 * 383)
    py = int((1 - y / 10.0) * 191)
    if 0 <= px <= 383 and 0 <= py <= 191:
        set_pixel(px, py, (0,150,0))

show_screen()

# input("\nPress any key to exit: ")

