def kaprekar_step(n):
    digits = sorted([int(d) for d in str(n).zfill(4)])
    asc  = int("".join(map(str, digits)))
    desc = int("".join([str(x) for x in digits[::-1]]))
    return desc - asc

n = int(input("4-digit number: "))
if len(set(str(n).zfill(4))) == 1:
    print("All same digits - invalid.")
else:
    step = 0
    while n != 6174 and step < 10:
        n = kaprekar_step(n)
        step += 1
        print("Step", step, ":", n)
    if n == 6174:
        print("Reached Kaprekar constant in", step, "steps!")

# input("\nPress any key to exit: ")

