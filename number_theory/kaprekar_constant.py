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


def kaprekar_step(n):
    digits = sorted([int(d) for d in str(n).zfill(4)])
    asc = int("".join(map(str, digits)))
    desc = int("".join([str(x) for x in digits[::-1]]))
    return desc - asc


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    n = read_int("4-digit number: ")
    if len(set(str(n).zfill(4))) == 1:
        print("All same digits - invalid.")
    else:
        step = 0
        while n != 6174 and step < 10:
            n = kaprekar_step(n)
            step += 1
            print("Step", step, ":", n)
        if n == 6174:
            print("Reached Kaprekar constant in", step, "steps!")
    wait_for_exit()


main()
