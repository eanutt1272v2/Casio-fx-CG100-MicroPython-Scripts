def parallel(*resistors):
    return 1.0 / sum(1.0/r for r in resistors)

def series(*resistors):
    return sum(resistors)

print("--- Ohm's Law Solver ---")
mode = input("s=series, p=parallel, o=basic: ")

if mode == "o":
    V = float(input("V (volts, 0 to skip): ") or 0)
    I = float(input("I (amps, 0 to skip): ") or 0)
    R = float(input("R (ohms, 0 to skip): ") or 0)
    if R == 0 and V and I:
        print("R =", V/I, "ohms")
    elif I == 0 and V and R:
        print("I =", V/R, "amps")
    elif V == 0 and I and R:
        print("V =", I*R, "volts")

elif mode == "s":
    n = int(input("How many resistors? "))
    rs = [float(input("R" + str(i+1) + ": ")) for i in range(n)]
    Rtot = series(*rs)
    V = float(input("Total voltage V: "))
    I = V / Rtot
    print("Total R:", round(Rtot,4), "ohms")
    print("Current:", round(I,4), "A")
    for i in range(len(rs)):
        r = rs[i]
        print("V" + str(i+1) + ":", round(I*r, 4), "V")

elif mode == "p":
    n = int(input("How many resistors? "))
    rs = [float(input("R" + str(i+1) + ": ")) for i in range(n)]
    Rtot = parallel(*rs)
    V = float(input("Voltage across parallel: "))
    print("Total R:", round(Rtot,4), "ohms")
    for i in range(len(rs)):
        r = rs[i]
        print("I" + str(i+1) + ":", round(V/r, 4), "A")

input("\nPress any key to exit: ")

