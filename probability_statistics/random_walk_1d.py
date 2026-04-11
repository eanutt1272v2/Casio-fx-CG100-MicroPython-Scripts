from matplotlib.pyplot import axis, plot, show, text
import random

N = int(input("Steps N: "))
pos = 0
positions = [0]

for _ in range(N):
    pos += 1 if random.random() > 0.5 else -1
    positions.append(pos)

import math
rms = math.sqrt(N)
xs = list(range(N+1))
plot(xs, positions, "blue")
plot([0, N], [rms, rms], "red")
plot([0, N], [-rms, -rms], "red")
axis([0, N, -rms*2, rms*2])
text(0, rms+0.5, "+sqrt(N)")
text(0, -rms-2, "-sqrt(N)")
show()

input("\nPress any key to exit: ")

