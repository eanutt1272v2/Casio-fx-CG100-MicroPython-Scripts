def powmod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp //= 2
        base = (base * base) % mod
    return result

def fermat_test(n, trials=5):
    import random
    if n < 2:
        return False
    if n == 2:
        return True
    for _ in range(trials):
        a = random.randint(2, n - 1)
        if powmod(a, n - 1, n) != 1:
            return False
    return True

n = int(input("Test n for primality: "))
result = fermat_test(n)
print("Probably prime:", result)
print("(Fermat test, 5 witnesses)")

print("a^(n-1) mod n for a=2:", powmod(2, n-1, n))

# input("\nPress any key to exit: ")

