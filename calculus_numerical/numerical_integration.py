from math import sin

def f(x):
    return sin(x)

def simpson(a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        coeff = 4 if i % 2 == 1 else 2
        total += coeff * f(a + i * h)
    return total * h / 3

a = float(input("Lower limit a: "))
b = float(input("Upper limit b: "))
n = int(input("Subintervals (even, e.g. 100): "))

result = simpson(a, b, n)
print("Integral =", result)

input("\nPress any key to exit: ")

