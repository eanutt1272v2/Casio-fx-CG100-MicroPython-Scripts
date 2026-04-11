def horner(coeffs, x):

    result = 0
    for c in coeffs:
        result = result * x + c
    return result

raw = input("Coefficients (highest to lowest, comma-sep): ")
coeffs = [float(c) for c in raw.split(",")]
x = float(input("Evaluate at x: "))
result = horner(coeffs, x)
print("p(x) =", result)


from matplotlib.pyplot import axis, grid, plot, show, text

a_val = float(input("Plot from x=: "))
b_val = float(input("         to x=: "))
xs = [a_val + (b_val - a_val) * i / 200 for i in range(201)]
ys = [horner(coeffs, xi) for xi in xs]
plot(xs, ys, "blue")
axis("auto")
grid("on")
text(a_val, max(ys), "p(x)")
show()

input("\nPress any key to exit: ")

