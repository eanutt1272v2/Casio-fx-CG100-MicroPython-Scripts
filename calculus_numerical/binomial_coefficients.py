from matplotlib.pyplot import axis, bar, show, text

def binom(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

n = int(input("Row n of Pascal's triangle: "))
row = [binom(n, k) for k in range(n+1)]
print("Row:", row)
print("Sum:", sum(row), "= 2^n =", 2**n)

xs = list(range(n+1))
bar(xs, row)
axis([-1, n+1, 0, max(row)*1.1])
text(0, max(row), "C("+str(n)+",k)")
show()

input("\nPress any key to exit: ")

