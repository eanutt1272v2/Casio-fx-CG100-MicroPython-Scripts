# Visualise sorting algorithms step-by-step.

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


def shuffle_in_place(values):
    for i in range(len(values) - 1, 0, -1):
        j = int(random.random() * (i + 1))
        values[i], values[j] = values[j], values[i]


N = read_int("Array size N (e.g. 40): ", min_value=1)
print("1=Bubble  2=Selection  3=Insertion  4=Quicksort  5=Merge  6=Bogo  7=Radix  8=Counting  9=Heap")
alg = read_text("> ")
while alg not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
    print("Choose 1..9")
    alg = read_text("> ")

arr = list(range(1, N + 1))
shuffle_in_place(arr)
W = 384
H = 192
MAX_BOGO_SHUFFLES = 20000


def draw_bars(arr, hi1=-1, hi2=-1):
    clear_screen()
    max_v = max(arr)
    bar_w = max(1, W // len(arr))
    for i in range(len(arr)):
        v = arr[i]
        h = int(v / max_v * H)
        x = i * bar_w
        col = (200, 0, 0) if i == hi1 else (0, 180, 0) if i == hi2 else (0, 0, 180)
        for dx in range(bar_w - 1):
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
    bogo_shuffles = 0
    bogo_limit_hit = False

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
    elif alg == "5":
        temp = [0] * len(arr)

        def merge_sort(lo, hi):
            if hi - lo <= 1:
                return
            mid = (lo + hi) // 2
            merge_sort(lo, mid)
            merge_sort(mid, hi)

            i, j, k = lo, mid, lo
            while i < mid and j < hi:
                comps[0] += 1
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1
            while i < mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j < hi:
                temp[k] = arr[j]
                j += 1
                k += 1

            for k in range(lo, hi):
                arr[k] = temp[k]

            draw_bars(arr, lo, hi - 1)

        merge_sort(0, len(arr))
    elif alg == "6":
        if len(arr) > 8:
            print("Bogosort is too slow for large N; using first 8 items.")
            arr[:] = arr[:8]

        def is_sorted(values):
            for i in range(len(values) - 1):
                comps[0] += 1
                if values[i] > values[i + 1]:
                    return False
            return True

        while not is_sorted(arr):
            if bogo_shuffles >= MAX_BOGO_SHUFFLES:
                bogo_limit_hit = True
                break
            shuffle_in_place(arr)
            bogo_shuffles += 1
            draw_bars(arr)
    elif alg == "7":
        max_val = max(arr)
        exp = 1
        out = [0] * len(arr)

        while max_val // exp > 0:
            count = [0] * 10

            for v in arr:
                digit = (v // exp) % 10
                count[digit] += 1
                comps[0] += 1

            for i in range(1, 10):
                count[i] += count[i - 1]

            for i in range(len(arr) - 1, -1, -1):
                digit = (arr[i] // exp) % 10
                count[digit] -= 1
                out[count[digit]] = arr[i]

            for i in range(len(arr)):
                arr[i] = out[i]
                draw_bars(arr, i)

            exp *= 10
    elif alg == "8":
        lo = min(arr)
        hi = max(arr)
        counts = [0] * (hi - lo + 1)

        for v in arr:
            counts[v - lo] += 1
            comps[0] += 1

        idx = 0
        for offset, cnt in enumerate(counts):
            while cnt > 0:
                arr[idx] = offset + lo
                comps[0] += 1
                draw_bars(arr, idx)
                idx += 1
                cnt -= 1
    elif alg == "9":
        n = len(arr)

        def sift_down(start, end):
            root = start
            while True:
                child = 2 * root + 1
                if child > end:
                    return

                swap_idx = root
                comps[0] += 1
                if arr[swap_idx] < arr[child]:
                    swap_idx = child

                if child + 1 <= end:
                    comps[0] += 1
                    if arr[swap_idx] < arr[child + 1]:
                        swap_idx = child + 1

                if swap_idx == root:
                    return

                arr[root], arr[swap_idx] = arr[swap_idx], arr[root]
                draw_bars(arr, root, swap_idx)
                root = swap_idx

        for start in range((n - 2) // 2, -1, -1):
            sift_down(start, n - 1)

        for end in range(n - 1, 0, -1):
            arr[end], arr[0] = arr[0], arr[end]
            draw_bars(arr, 0, end)
            sift_down(0, end - 1)

    draw_bars(arr)
    summary = "Done comps=" + str(comps[0])
    if alg == "6":
        summary = summary + " shuf=" + str(bogo_shuffles)
    draw_string(0, 0, summary, (0, 0, 0), "small")
    if bogo_limit_hit:
        draw_string(0, 10, "Bogo stopped at safety limit", (180, 0, 0), "small")
    show_screen()

    wait_for_exit()


main()
