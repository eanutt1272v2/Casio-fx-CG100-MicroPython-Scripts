from matplotlib.pyplot import axis, grid, scatter, show, text

def phi(n):
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result

N = 100
ns = list(range(1, N+1))
phis = [phi(n) for n in ns]

scatter(ns, phis)
axis([0, N, 0, N])
grid("on")
text(1, N-8, "Euler totient phi(n)")
show()

# input("\nPress any key to exit: ")

