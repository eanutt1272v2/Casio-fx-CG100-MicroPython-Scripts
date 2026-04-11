def sieve(n):
    is_p = [True]*(n+1)
    is_p[0] = is_p[1] = False
    i = 2
    while i*i <= n:
        if is_p[i]:
            for j in range(i*i, n+1, i):
                is_p[j] = False
        i += 1
    return is_p

N = int(input("Check even numbers up to N: "))
is_p = sieve(N)

for n in range(4, N+1, 2):
    found = False
    for p in range(2, n//2 + 1):
        if is_p[p] and is_p[n-p]:
            print(n, "=", p, "+", n-p)
            found = True
            break
    if not found:
        print("COUNTEREXAMPLE FOUND:", n)
        break
print("Done. Conjecture holds up to", N)

# input("\nPress any key to exit: ")

