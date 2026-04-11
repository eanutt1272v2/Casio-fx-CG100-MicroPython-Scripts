def cont_frac(x, steps=12):
    coeffs = []
    for _ in range(steps):
        a = int(x)
        coeffs.append(a)
        frac = x - a
        if abs(frac) < 1e-9:
            break
        x = 1.0 / frac
    return coeffs


def convergents(coeffs):
    h_prev, h = 1, coeffs[0]
    k_prev, k = 0, 1
    print("n  coeff  h/k (convergent)")
    print(0, "    ", coeffs[0], "     ", h, "/", k)
    for i in range(1, len(coeffs)):
        h_prev, h = h, coeffs[i] * h + h_prev
        k_prev, k = k, coeffs[i] * k + k_prev
        print(i, "    ", coeffs[i], "     ", h, "/", k)


x = float(input("x (e.g. 3.14159): "))
cf = cont_frac(x, 10)
print("CF:", cf)
convergents(cf)

input("\nPress any key to exit: ")

