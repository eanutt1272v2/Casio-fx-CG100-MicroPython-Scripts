def digit_sum(n):
    return sum(int(d) for d in str(n))

def digital_root(n):
    steps = 0
    while n >= 10:
        n = digit_sum(n)
        steps += 1
    return n, steps

n = int(input("n: "))
root, persist = digital_root(n)
print("Digital root:", root)
print("Additive persistence:", persist)

quick = 1 + (n - 1) % 9 if n > 0 else 0
print("Formula check:", quick)

input("\nPress any key to exit: ")

