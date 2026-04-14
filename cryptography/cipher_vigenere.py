# Encrypt and decrypt text with a Vigenere cipher.

from matplotlib.pyplot import bar, axis, text, show, grid

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


def vigenere(text, key, decode=False):
    key = key.upper()
    result = ""
    ki = 0
    for ch in text.upper():
        if ch.isalpha():
            shift = ord(key[ki % len(key)]) - 65
            if decode:
                shift = -shift
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
            ki += 1
        else:
            result += ch
    return result


def freq_analysis(text):
    text = text.upper()
    counts = [text.count(chr(65 + i)) for i in range(26)]
    total = sum(counts)
    freqs = [c / total * 100 if total else 0 for c in counts]
    return freqs


def index_of_coincidence(text):
    text = "".join(c for c in text.upper() if c.isalpha())
    n = len(text)
    if n < 2:
        return 0
    counts = [text.count(chr(65 + i)) for i in range(26)]
    return sum(c * (c - 1) for c in counts) / (n * (n - 1))


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    while True:
        print("1=Encode  2=Decode  3=Freq analysis  4=Index of coincidence  0=quit")
        m = read_text("> ")
        if m == "0":
            break
        if m in ("1", "2"):
            txt = read_text("Text: ")
            key = read_text("Key: ")
            out = vigenere(txt, key, decode=(m == "2"))
            print("Result:", out)
        elif m == "3":
            txt = read_text("Ciphertext: ")
            freqs = freq_analysis(txt)
            letters = [chr(65 + i) for i in range(26)]
            xs = list(range(26))
            bar(xs, freqs, "blue")
            axis([-1, 26, 0, max(freqs) * 1.2])
            grid("on")
            text(0, max(freqs), "Letter frequencies (%)")
            show()

            pairs = []
            for idx in range(26):
                pairs.append((freqs[idx], letters[idx]))
            for a in range(len(pairs)):
                for b in range(a + 1, len(pairs)):
                    if pairs[b][0] > pairs[a][0]:
                        pairs[a], pairs[b] = pairs[b], pairs[a]
            top = pairs[:5]
            print("Top 5:", [(top[i][1], round(top[i][0], 1)) for i in range(5)])
            print("English IC~0.065. Random~0.038")
        elif m == "4":
            txt = read_text("Ciphertext: ")
            ic = index_of_coincidence(txt)
            print("IC =", round(ic, 5))
            print("English IC ~ 0.0650")
            print("Random IC  ~ 0.0385")
            print("Likely key length estimate:")

            for kl in range(1, 15):
                sub = "".join(txt[i] for i in range(0, len(txt), kl) if txt[i].isalpha())
                ic_sub = index_of_coincidence(sub)
                if ic_sub > 0.055:
                    print("  Key length", kl, "IC=", round(ic_sub, 4), "<-- likely")
                    break
        input("EXE")
    wait_for_exit()


main()
