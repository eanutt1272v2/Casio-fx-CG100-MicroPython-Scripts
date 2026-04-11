def powmod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = result * base % mod
        exp >>= 1
        base = base * base % mod
    return result

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i*i <= n:
        if n % i == 0: return False
        i += 2
    return True

a = int(input("a: "))
p = int(input("p (odd prime): "))

if not is_prime(p) or p == 2:
    print("p must be an odd prime.")
else:
    val = powmod(a, (p-1)//2, p)
    if val == 0:
        sym = 0
    elif val == 1:
        sym = 1
    else:
        sym = -1
    print("Legendre (" + str(a) + "/" + str(p) + ") =", sym)
    if sym == 1:
        print(str(a) + " is a quadratic residue mod " + str(p))
    elif sym == -1:
        print(str(a) + " is a non-residue mod " + str(p))

# input("\nPress any key to exit: ")

