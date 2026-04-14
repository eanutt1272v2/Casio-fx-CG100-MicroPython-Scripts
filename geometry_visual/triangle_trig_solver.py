# Solve triangles with trigonometric relationships.

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


def deg(r):
    return r * 180 / math.pi


def rad(d):
    return d * math.pi / 180


def solve_triangle(a, b, c, A, B, C):

    known = sum(1 for x in [a, b, c] if x is not None)
    known_a = sum(1 for x in [A, B, C] if x is not None)

    if a is None and b and c and A:
        a = math.sqrt(b * b + c * c - 2 * b * c * math.cos(rad(A)))
    elif b is None and a and c and B:
        b = math.sqrt(a * a + c * c - 2 * a * c * math.cos(rad(B)))
    elif c is None and a and b and C:
        c = math.sqrt(a * a + b * b - 2 * a * b * math.cos(rad(C)))
    elif A is None and a and b and c:
        A = deg(math.acos((b * b + c * c - a * a) / (2 * b * c)))
    elif B is None and a and b and c:
        B = deg(math.acos((a * a + c * c - b * b) / (2 * a * c)))
    elif C is None and a and b and c:
        C = deg(math.acos((a * a + b * b - c * c) / (2 * a * b)))

    if A and B and not C:
        C = 180 - A - B
    if A and C and not B:
        B = 180 - A - C
    if B and C and not A:
        A = 180 - B - C

    if a and A:
        k = a / math.sin(rad(A))
        if b is None and B:
            b = k * math.sin(rad(B))
        if c is None and C:
            c = k * math.sin(rad(C))
        if B is None and b:
            B = deg(math.asin(min(1, b / k)))
        if C is None and c:
            C = deg(math.asin(min(1, c / k)))
    return a, b, c, A, B, C


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    print("Enter known values (0 if unknown):")
    print("Sides: a (opp A), b (opp B), c (opp C)")
    a = read_float("a (0=unknown): ") or None
    b = read_float("b (0=unknown): ") or None
    c = read_float("c (0=unknown): ") or None
    A = read_float("A degrees (0=unknown): ") or None
    B = read_float("B degrees (0=unknown): ") or None
    C = read_float("C degrees (0=unknown): ") or None

    a, b, c, A, B, C = solve_triangle(a, b, c, A, B, C)
    a, b, c, A, B, C = solve_triangle(a, b, c, A, B, C)

    print("--- Solution ---")
    print("a=", round(a, 5) if a else "?")
    print("b=", round(b, 5) if b else "?")
    print("c=", round(c, 5) if c else "?")
    print("A=", round(A, 4), "deg" if A else "?")
    print("B=", round(B, 4), "deg" if B else "?")
    print("C=", round(C, 4), "deg" if C else "?")
    if a and b and c:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        R_circ = a * b * c / (4 * area)
        r_in = area / s
        print("Area=", round(area, 5))
        print("Circumradius R=", round(R_circ, 5))
        print("Inradius r=", round(r_in, 5))
        print("Perimeter=", round(a + b + c, 5))
    wait_for_exit()


main()
