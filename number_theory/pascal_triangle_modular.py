# Visualise Pascal's triangle modulo n.

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


def pascal_row(prev):
    row = [1]
    for i in range(len(prev) - 1):
        row.append(prev[i] + prev[i + 1])
    row.append(1)
    return row


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    k = read_int("Modulus k (e.g. 2 or 3): ")
    rows = 20
    row = [1]
    clear_screen()
    colours = [(220, 0, 0), (0, 180, 0), (0, 0, 220), (180, 120, 0), (0, 160, 160), (160, 0, 160), (80, 80, 80), (0, 0, 0)]

    for r in range(rows):
        for c in range(len(row)):
            val = row[c]
            mod_val = val % k
            col = colours[mod_val % len(colours)]
            px = 192 + (c - r // 2) * 9
            py = 5 + r * 9
            for dx in range(7):
                for dy in range(7):
                    set_pixel(px + dx, py + dy, col)
        row = pascal_row(row)

    show_screen()
    wait_for_exit()


main()
