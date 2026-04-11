from matplotlib.pyplot import axis, grid, plot, show, text

def collatz(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

start = int(input("Starting integer: "))
seq = collatz(start)
print("Steps:", len(seq) - 1)
print("Max value:", max(seq))

xs = list(range(len(seq)))
plot(xs, seq, "blue")
axis("auto")
grid("on")
text(0, max(seq) - max(seq)//10,
     "n=" + str(start) + " steps=" + str(len(seq)-1))
show()

input("\nPress any key to exit: ")

