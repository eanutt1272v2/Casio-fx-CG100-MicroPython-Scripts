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


RAM = {
    "H": 1.008,
    "He": 4.003,
    "Li": 6.941,
    "Be": 9.012,
    "B": 10.81,
    "C": 12.01,
    "N": 14.01,
    "O": 16.00,
    "F": 19.00,
    "Ne": 20.18,
    "Na": 22.99,
    "Mg": 24.31,
    "Al": 26.98,
    "Si": 28.09,
    "P": 30.97,
    "S": 32.07,
    "Cl": 35.45,
    "Ar": 39.95,
    "K": 39.10,
    "Ca": 40.08,
    "Fe": 55.85,
    "Cu": 63.55,
    "Zn": 65.38,
    "Br": 79.90,
    "Ag": 107.9,
    "I": 126.9,
    "Ba": 137.3,
    "Pb": 207.2,
}


def molar_mass(formula):
    import re

    def expand(f):
        while "(" in f:
            m = re.search(r"\(([^()]+)\)(\d*)", f)
            if not m:
                break
            inner = m.group(1)
            mult = int(m.group(2)) if m.group(2) else 1
            expanded = ""
            i2 = 0
            while i2 < len(inner):
                if inner[i2].isupper():
                    sym = inner[i2]
                    i2 += 1
                    if i2 < len(inner) and inner[i2].islower():
                        sym += inner[i2]
                        i2 += 1
                    num = ""
                    while i2 < len(inner) and inner[i2].isdigit():
                        num += inner[i2]
                        i2 += 1
                    cnt2 = int(num) if num else 1
                    expanded += sym + str(cnt2 * mult)
                else:
                    i2 += 1
            f = f[: m.start()] + expanded + f[m.end() :]
        return f

    formula = expand(formula)
    total = 0.0
    import re as _re

    for tok in _re.findall(r"([A-Z][a-z]?)(\d*)", formula):
        sym = tok[0]
        cnt = int(tok[1]) if tok[1] else 1
        total += RAM.get(sym, 0) * cnt
    return total


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    while True:
        print("1=Molar mass  2=Moles/mass/Mr  3=Concentration")
        print("4=Ideal gas PV=nRT  5=Titration  6=% composition  0=quit")
        m = read_text("> ")
        if m == "0":
            break
        if m == "1":
            f = read_text("Formula (e.g. H2SO4): ")
            Mr = molar_mass(f)
            print("Mr(" + f + ") =", round(Mr, 3), "g/mol")
        elif m == "2":
            print("n=mass/Mr. Enter 0 for unknown.")
            mass = read_float("Mass (g, 0=?): ", default=0)
            Mr = read_float("Mr (0=?): ", default=0)
            n = read_float("Moles n (0=?): ", default=0)
            if not mass:
                mass = n * Mr
            if not Mr and n:
                Mr = mass / n
            if not n and Mr:
                n = mass / Mr
            print(
                "Mass=",
                round(mass, 4),
                "g  Mr=",
                round(Mr, 4),
                "  n=",
                round(n, 6),
                "mol",
            )
        elif m == "3":
            print("c=n/V. Enter 0 for unknown.")
            c = read_float("Conc c (mol/dm3, 0=?): ", default=0)
            n = read_float("Moles n (0=?): ", default=0)
            V = read_float("Volume V (dm3, 0=?): ", default=0)
            if not c and n and V:
                c = n / V
            if not n and c and V:
                n = c * V
            if not V and c and n:
                V = n / c
            print(
                "c=",
                round(c, 5),
                "mol/dm3  n=",
                round(n, 5),
                "mol  V=",
                round(V, 5),
                "dm3",
            )
        elif m == "4":
            R = 8.314
            print("PV=nRT. R=8.314 J/(mol K). 0=unknown.")
            P = read_float("P (Pa, 0=?): ", default=0)
            V = read_float("V (m3, 0=?): ", default=0)
            n = read_float("n (mol, 0=?): ", default=0)
            T = read_float("T (K, 0=?): ", default=0)
            if not P:
                P = n * R * T / V
            if not V:
                V = n * R * T / P
            if not n:
                n = P * V / (R * T)
            if not T:
                T = P * V / (n * R)
            print(
                "P=",
                round(P, 2),
                "Pa  V=",
                round(V, 6),
                "m3  n=",
                round(n, 6),
                "mol  T=",
                round(T, 3),
                "K",
            )
        elif m == "5":
            print("Titration: c1V1 = c2V2")
            c1 = read_float("c1 (0=?): ", default=0)
            V1 = read_float("V1 cm3 (0=?): ", default=0)
            c2 = read_float("c2 (0=?): ", default=0)
            V2 = read_float("V2 cm3 (0=?): ", default=0)
            if not c1:
                c1 = c2 * V2 / V1
            if not V1:
                V1 = c2 * V2 / c1
            if not c2:
                c2 = c1 * V1 / V2
            if not V2:
                V2 = c1 * V1 / c2
            print(
                "c1=",
                round(c1, 5),
                "  V1=",
                round(V1, 4),
                "cm3  c2=",
                round(c2, 5),
                "  V2=",
                round(V2, 4),
                "cm3",
            )
        elif m == "6":
            f = read_text("Formula: ")
            Mr = molar_mass(f)
            el = read_text("Element (e.g. O): ")
            cnt = read_int("Count of " + el + " in formula: ")
            pct = RAM.get(el, 0) * cnt / Mr * 100 if Mr else 0
            print("% " + el + " in " + f + " =", round(pct, 3), "%")
        input("EXE")
    wait_for_exit()


main()
