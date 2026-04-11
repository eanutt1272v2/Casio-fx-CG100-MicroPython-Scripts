try:
    from casioplot import clear_screen, draw_string, getkey, set_pixel, show_screen
except ImportError:
    from casioplot import clear_screen, draw_string, set_pixel, show_screen

    getkey = None

SCREEN_W = 384
SCREEN_H = 192
CHAR_W = 7.5
TEXT_H = 10
TOP_TEXT_Y = 0
TOP_MARGIN = TEXT_H + 4
LEFT_MARGIN_MIN = 24
RIGHT_MARGIN = 4
BOTTOM_MARGIN = TEXT_H + 8
AXIS_LABEL_GAP = 4

PLOT_LEFT = LEFT_MARGIN_MIN
PLOT_TOP = TOP_MARGIN
PLOT_RIGHT = SCREEN_W - RIGHT_MARGIN
PLOT_BOTTOM = SCREEN_H - BOTTOM_MARGIN
PLOT_W = PLOT_RIGHT - PLOT_LEFT
PLOT_H = PLOT_BOTTOM - PLOT_TOP

CHAR_WIDTHS = {
    "0": 8,
    "1": 8,
    "2": 8,
    "3": 8,
    "4": 8,
    "5": 8,
    "6": 8,
    "7": 8,
    "8": 8,
    "9": 8,
    ".": 4,
    "e": 6,
}


def text_width_px(text):
    total = 0.0
    for ch in text:
        total += CHAR_WIDTHS.get(ch, CHAR_W)
    return int(total + 0.5)


"""
def clip_text_px(text, max_width):
    if text_width_px(text) <= max_width:
        return text

    acc = 0.0
    out = []
    for ch in text:
        w = CHAR_WIDTHS.get(ch, CHAR_W)
        if acc + w > max_width:
            break
        out.append(ch)
        acc += w
    return "".join(out)
"""


def ask_int(prompt, default_value, minimum, maximum):
    while True:
        raw = input(prompt + " [" + str(default_value) + "]: ").strip()
        if raw == "":
            return default_value
        try:
            value = int(raw)
        except ValueError:
            print("Please enter an integer.")
            continue
        if value < minimum or value > maximum:
            print("Enter a value in " + str(minimum) + ".." + str(maximum) + ".")
            continue
        return value


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


def draw_axes():
    axis_col = (0, 0, 0)
    grid_col = (210, 210, 210)

    for gy in range(1, 4):
        y = PLOT_BOTTOM - (gy * PLOT_H) // 4
        for x in range(PLOT_LEFT + 1, PLOT_RIGHT + 1, 2):
            set_pixel(x, y, grid_col)

    for gx in range(1, 4):
        x = PLOT_LEFT + (gx * PLOT_W) // 4
        for y in range(PLOT_TOP, PLOT_BOTTOM, 2):
            set_pixel(x, y, grid_col)

    for x in range(PLOT_LEFT, PLOT_RIGHT + 1):
        set_pixel(x, PLOT_BOTTOM, axis_col)
    for y in range(PLOT_TOP, PLOT_BOTTOM + 1):
        set_pixel(PLOT_LEFT, y, axis_col)

    for tx in range(5):
        x = PLOT_LEFT + (tx * PLOT_W) // 4
        for dy in range(1, 4):
            y_tick = PLOT_BOTTOM + dy
            if y_tick < SCREEN_H:
                set_pixel(x, y_tick, axis_col)

    for ty in range(5):
        y = PLOT_BOTTOM - (ty * PLOT_H) // 4
        for dx in range(1, 4):
            x_tick = PLOT_LEFT - dx
            if x_tick >= 0:
                set_pixel(x_tick, y, axis_col)


def compact_int(value):
    s = str(value)
    if len(s) <= 5:
        return s
    return s[0] + "." + s[1:3] + "e" + str(len(s) - 1)


def update_plot_layout(max_value):
    global PLOT_LEFT, PLOT_TOP, PLOT_RIGHT, PLOT_BOTTOM, PLOT_W, PLOT_H

    max_y_label_w = 1
    for i in range(5):
        label_w = text_width_px(compact_int((i * max_value) // 4))
        if label_w > max_y_label_w:
            max_y_label_w = label_w

    left_f = max(LEFT_MARGIN_MIN, 8 + max_y_label_w + AXIS_LABEL_GAP)
    PLOT_LEFT = int(left_f + 0.5)
    PLOT_TOP = int(TOP_MARGIN)
    PLOT_RIGHT = int(SCREEN_W - RIGHT_MARGIN)
    PLOT_BOTTOM = int(SCREEN_H - BOTTOM_MARGIN)
    PLOT_W = int(PLOT_RIGHT - PLOT_LEFT)
    PLOT_H = int(PLOT_BOTTOM - PLOT_TOP)


def draw_tick_labels(n, max_value):
    label_col = (0, 0, 0)
    x_label_y = int(PLOT_BOTTOM + 6)
    y_label_right = int(PLOT_LEFT - AXIS_LABEL_GAP)

    for i in range(5):
        x = PLOT_LEFT + (i * PLOT_W) // 4
        kval = (i * n) // 4
        x_label = str(kval)
        x_label_w = text_width_px(x_label)
        x_label_x = int(x - (x_label_w // 2))
        draw_string(x_label_x, x_label_y, x_label, label_col, "small")

    for i in range(5):
        y = PLOT_BOTTOM - (i * PLOT_H) // 4
        yval = (i * max_value) // 4
        y_label = compact_int(yval)
        y_label_y = int(y - (TEXT_H // 2) + 1)
        y_label_x = int(y_label_right - text_width_px(y_label))
        draw_string(y_label_x, y_label_y, y_label, label_col, "small")


def bar_height(value, max_value, usable_h):
    if value <= 0:
        return 0

    height = (value * usable_h) // max_value
    if height < 1:
        return 1
    return height


def draw_histogram(row):
    max_value = max(row)
    if max_value <= 0:
        return

    if PLOT_W <= 1 or PLOT_H <= 2:
        return

    columns = PLOT_W - 1
    row_len = len(row)
    usable_h = PLOT_H - 2

    for x in range(columns):
        start_i = (x * row_len) // columns
        end_i = ((x + 1) * row_len) // columns
        if end_i <= start_i:
            end_i = start_i + 1

        chunk_peak = 0
        for i in range(start_i, end_i):
            value = row[i]
            if value > chunk_peak:
                chunk_peak = value

        height = bar_height(chunk_peak, max_value, usable_h)

        px = PLOT_LEFT + 1 + x
        r = 35 + (90 * height) // usable_h
        g = 90 + (45 * height) // usable_h
        colour = (r, g, 220)
        for dy in range(height):
            set_pixel(px, PLOT_BOTTOM - 1 - dy, colour)

        if height > 0:
            set_pixel(px, PLOT_BOTTOM - height, (220, 235, 255))


def draw_screen(n, row, check_ok):
    max_value = max(row)
    update_plot_layout(max_value)

    clear_screen()
    draw_histogram(row)
    draw_axes()
    draw_tick_labels(n, max_value)

    status = "sum=OK" if check_ok else "sum=ERR"
    top_text = (
        "Pascal | n="
        + str(n)
        + " terms="
        + str(len(row))
        + " max="
        + compact_int(max_value)
        + " mode=linear "
        + status
    )
    # top_text = clip_text_px(top_text, SCREEN_W)
    draw_string(0, TOP_TEXT_Y, top_text, (0, 0, 0), "small")

    show_screen()


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    print("Pascal triangle row + histogram (fx-CG100)")
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
