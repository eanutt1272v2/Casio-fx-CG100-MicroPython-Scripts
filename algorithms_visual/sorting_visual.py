from casioplot import draw_string, show_screen, clear_screen, set_pixel
import random

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


def shuffle_in_place(values):
    for i in range(len(values) - 1, 0, -1):
        j = int(random.random() * (i + 1))
        values[i], values[j] = values[j], values[i]


N = read_int("Array size N (e.g. 40): ", min_value=1)
print("1=Bubble  2=Selection  3=Insertion  4=Quicksort")
alg = read_text("> ")

arr = list(range(1, N + 1))
shuffle_in_place(arr)
W = 384
H = 192
BAR_W = max(1, W // N)


def draw_bars(arr, hi1=-1, hi2=-1):
    clear_screen()
    max_v = max(arr)
    for i in range(len(arr)):
        v = arr[i]
        h = int(v / max_v * H)
        x = i * BAR_W
        col = (200, 0, 0) if i == hi1 else (0, 180, 0) if i == hi2 else (0, 0, 180)
        for dx in range(BAR_W - 1):
            for dy in range(h):
                set_pixel(x + dx, H - dy, col)
    show_screen()


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    comps = [0]

    if alg == "1":
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                comps[0] += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    draw_bars(arr, j, j + 1)
    elif alg == "2":
        n = len(arr)
        for i in range(n):
            mn = i
            for j in range(i + 1, n):
                comps[0] += 1
                if arr[j] < arr[mn]:
                    mn = j
            arr[i], arr[mn] = arr[mn], arr[i]
            draw_bars(arr, i, mn)
    elif alg == "3":
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                comps[0] += 1
                arr[j + 1] = arr[j]
                j -= 1
                draw_bars(arr, j + 1, i)
            arr[j + 1] = key
    elif alg == "4":

        def qs(a, lo, hi):
            if lo >= hi:
                return
            pivot = a[hi]
            i = lo - 1
            for j in range(lo, hi):
                comps[0] += 1
                if a[j] <= pivot:
                    i += 1
                    a[i], a[j] = a[j], a[i]
                    draw_bars(a, i, j)
            a[i + 1], a[hi] = a[hi], a[i + 1]
            draw_bars(a, i + 1, hi)
            qs(a, lo, i)
            qs(a, i + 2, hi)

        qs(arr, 0, len(arr) - 1)

    draw_bars(arr)
    draw_string(
        0, 0, "Exec Done! Total Comparisons=" + str(comps[0]), (0, 0, 0), "small"
    )
    show_screen()

    wait_for_exit()


main()
