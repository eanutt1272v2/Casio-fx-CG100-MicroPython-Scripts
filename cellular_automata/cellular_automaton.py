from casioplot import clear_screen, set_pixel, show_screen

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
    rule_num = read_int("Rule (e.g. 30 or 110): ")
    rule = {}
    for i in range(8):
        rule[(i >> 2) & 1, (i >> 1) & 1, i & 1] = (rule_num >> i) & 1

    W = 192
    cells = [0] * W
    cells[W // 2] = 1

    clear_screen()
    for row in range(96):
        for x in range(W):
            if cells[x]:
                set_pixel(x * 2, row * 2, (0, 0, 180))
                set_pixel(x * 2 + 1, row * 2, (0, 0, 180))
        new = [0] * W
        for x in range(W):
            l = cells[(x - 1) % W]
            c = cells[x]
            r = cells[(x + 1) % W]
            new[x] = rule[l, c, r]
        cells = new

    show_screen()
    wait_for_exit()


main()
