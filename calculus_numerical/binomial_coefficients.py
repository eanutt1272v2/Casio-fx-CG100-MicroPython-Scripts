import matplotlib.pyplot as plt

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


def ask_int(prompt, default_value, minimum, maximum):
    return read_int(
        prompt + " [" + str(default_value) + "]: ",
        default=default_value,
        min_value=minimum,
        max_value=maximum,
    )


def pascal_row(n):
    row = [1]
    coeff = 1
    for k in range(1, n + 1):
        coeff = (coeff * (n - k + 1)) // k
        row.append(coeff)
    return row


def row_preview(row, shown_terms):
    if len(row) <= shown_terms:
        return str(row)
    left_count = shown_terms // 2
    right_count = shown_terms - left_count
    return str(row[:left_count]) + " ... " + str(row[-right_count:])


def compact_int(value):
    s = str(value)
    if len(s) <= 5:
        return s
    return s[0] + "." + s[1:3] + "e" + str(len(s) - 1)


def draw_screen(n, row, check_ok):
    max_value = max(row)

    xs = list(range(len(row)))
    heights = [float(v) for v in row]
    plt.bar(xs, heights)

    ticks = sorted(set([0, n // 4, n // 2, (3 * n) // 4, n]))
    plt.xticks(ticks)
    plt.xlim(-0.5, len(row) - 0.5)
    plt.grid(True)
    plt.xlabel("k")
    plt.ylabel("C(n, k)")

    status = "sum=OK" if check_ok else "sum=ERR"
    title = (
        "Pascal | n="
        + str(n)
        + " terms="
        + str(len(row))
        + " max="
        + compact_int(max_value)
        + " mode=linear "
        + status
    )
    plt.title(title)
    if hasattr(plt, "tight_layout"):
        plt.tight_layout()
    plt.show()


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    print("Pascal triangle row + histogram (matplotlib)")
    n = ask_int("Row n", 20, 0, 200)

    row = pascal_row(n)
    total = sum(row)
    power_of_two = 1 << n
    check_ok = total == power_of_two

    if n <= 35:
        print("Row:", row)
    else:
        print("Row preview:", row_preview(row, 12))
    print("Terms:", len(row))
    print("Sum:", total)
    print("2^n:", power_of_two)

    draw_screen(n, row, check_ok)
    wait_for_exit()


main()
