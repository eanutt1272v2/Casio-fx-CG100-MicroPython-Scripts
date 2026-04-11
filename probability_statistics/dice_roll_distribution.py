from matplotlib.pyplot import axis, bar, grid, show, text
import random

M = int(input("Rolls M (e.g. 300): "))
counts = [0] * 13

for _ in range(M):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    counts[d1 + d2] += 1

xs = list(range(2, 13))
ys = counts[2:]
bar(xs, ys, "blue")
axis([1, 13, 0, max(ys)*1.2])
grid("on")
text(2, max(ys), "2d6 rolls: " + str(M))
show()

# input("\nPress any key to exit: ")

