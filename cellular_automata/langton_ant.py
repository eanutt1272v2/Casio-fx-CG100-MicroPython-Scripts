from casioplot import clear_screen, set_pixel, show_screen

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():

    W, H = 384, 192
    grid = {}
    ax, ay = W // 2, H // 2

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    direction = 0
    steps = int(input("Steps (e.g. 5000): "))

    clear_screen()
    for _ in range(steps):
        cell = grid.get((ax, ay), 0)
        if cell == 0:
            direction = (direction + 1) % 4
            grid[(ax, ay)] = 1
            set_pixel(ax, ay, (0, 0, 0))
        else:
            direction = (direction - 1) % 4
            grid[(ax, ay)] = 0
            set_pixel(ax, ay, (255, 255, 255))
        ax = (ax + dx[direction]) % W
        ay = (ay + dy[direction]) % H

    show_screen()
    wait_for_exit()


main()
