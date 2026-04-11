try:
    from casioplot import getkey
except ImportError:
    getkey = None


def caesar(text, shift, decode=False):
    if decode:
        shift = -shift
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    mode = input("e=encode, d=decode: ")
    text = input("Text: ")
    shift = int(input("Shift: "))
    out = caesar(text, shift, decode=(mode == "d"))
    print("Result:", out)
    wait_for_exit()


main()
