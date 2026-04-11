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


def parallel(*resistors):
    return 1.0 / sum(1.0 / r for r in resistors)


def series(*resistors):
    return sum(resistors)


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    print("--- Ohm's Law Solver ---")
    mode = read_text("s=series, p=parallel, o=basic: ")

    if mode == "o":
        V = read_float("V (volts, 0 to skip): ", default=0)
        I = read_float("I (amps, 0 to skip): ", default=0)
        R = read_float("R (ohms, 0 to skip): ", default=0)
        if R == 0 and V and I:
            print("R =", V / I, "ohms")
        elif I == 0 and V and R:
            print("I =", V / R, "amps")
        elif V == 0 and I and R:
            print("V =", I * R, "volts")

    elif mode == "s":
        n = read_int("How many resistors? ")
        rs = [read_float("R" + str(i + 1) + ": ") for i in range(n)]
        Rtot = series(*rs)
        V = read_float("Total voltage V: ")
        I = V / Rtot
        print("Total R:", round(Rtot, 4), "ohms")
        print("Current:", round(I, 4), "A")
        for i in range(len(rs)):
            r = rs[i]
            print("V" + str(i + 1) + ":", round(I * r, 4), "V")

    elif mode == "p":
        n = read_int("How many resistors? ")
        rs = [read_float("R" + str(i + 1) + ": ") for i in range(n)]
        Rtot = parallel(*rs)
        V = read_float("Voltage across parallel: ")
        print("Total R:", round(Rtot, 4), "ohms")
        for i in range(len(rs)):
            r = rs[i]
            print("I" + str(i + 1) + ":", round(V / r, 4), "A")
    wait_for_exit()


main()
