def powmod(b, e, m):
    r = 1; b %= m
    while e > 0:
        if e & 1: r = r*b % m
        e >>= 1; b = b*b % m
    return r

def prime_factors(n):
    factors = set()
    d = 2
    while d*d <= n:
        while n % d == 0:
            factors.add(d); n //= d
        d += 1
    if n > 1: factors.add(n)
    return factors

def is_prim_root(g, p):
    phi = p - 1
    pfs = prime_factors(phi)
    for q in pfs:
        if powmod(g, phi // q, p) == 1:
            return False
    return True

p = int(input("Prime p: "))
print("Primitive roots mod", p, ":")
count = 0
for g in range(2, p):
    if is_prim_root(g, p):
        print(g, end="  ")
        count += 1
        if count >= 10:
            print("...")
            break

# input("\nPress any key to exit: ")

