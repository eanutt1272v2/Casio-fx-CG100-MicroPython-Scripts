from matplotlib.pyplot import axis, grid, plot, show, text
import math

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
    v0 = read_float("Initial speed v0 (m/s): ")
    angle = read_float("Angle (degrees): ")
    g = 9.81

    theta = angle * math.pi / 180
    T = 2 * v0 * math.sin(theta) / g
    R = v0**2 * math.sin(2 * theta) / g
    H = (v0 * math.sin(theta)) ** 2 / (2 * g)

    print("Flight time:", round(T, 3), "s")
    print("Range:", round(R, 3), "m")
    print("Max height:", round(H, 3), "m")

    N = 200
    ts = [T * i / N for i in range(N + 1)]
    xs = [v0 * math.cos(theta) * t for t in ts]
    ys = [v0 * math.sin(theta) * t - 0.5 * g * t**2 for t in ts]

    plot(xs, ys, "blue")
    axis([0, R * 1.1, 0, H * 1.2])
    grid("on")
    text(0, H, "v=" + str(v0) + " ang=" + str(angle))
    show()
    wait_for_exit()


main()
