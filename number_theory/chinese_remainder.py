def gcd(a, b):
    while b: a, b = b, a % b
    return a

def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y

def crt(remainders, moduli):
    M = 1
    for m in moduli: M *= m
    x = 0
    for idx in range(len(remainders)):
        r = remainders[idx]
        m = moduli[idx]
        Mi = M // m
        _, inv, _ = ext_gcd(Mi, m)
        inv %= m
        x += r * Mi * inv
    return x % M

n = int(input("Number of congruences: "))
rs = []
ms = []
for i in range(n):
    r = int(input("r" + str(i+1) + " (remainder): "))
    m = int(input("m" + str(i+1) + " (modulus): "))
    rs.append(r)
    ms.append(m)


ok = True
for i in range(n):
    for j in range(i+1, n):
        if gcd(ms[i], ms[j]) != 1:
            print("Moduli not pairwise coprime!")
            ok = False

if ok:
    x = crt(rs, ms)
    print("Solution: x =", x)
    M = 1
    for m in ms: M *= m
    print("(unique mod", M, ")")

# input("\nPress any key to exit: ")

