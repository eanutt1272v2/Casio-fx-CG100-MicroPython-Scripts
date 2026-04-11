from turtle import (
    forward,
    goto,
    hideturtle,
    left,
    pencolor,
    pendown,
    penup,
    right,
    speed,
)

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def dragon(seq, iters):
    for _ in range(iters):
        new = seq + "R"
        for idx in range(len(seq) - 1, -1, -1):
            c = seq[idx]
            if c == "R":
                new += "L"
            elif c == "L":
                new += "R"
            else:
                new += c
        seq = new
    return seq


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    iters = int(input("Iterations (8-12): "))
    seq = dragon("", iters)

    speed(0)
    hideturtle()
    pencolor("blue")
    penup()
    goto(-20, 10)
    pendown()
    step = max(1, 120 // (2 ** (iters // 2)))

    for c in seq:
        forward(step)
        if c == "R":
            right(90)
        elif c == "L":
            left(90)
    wait_for_exit()


main()
