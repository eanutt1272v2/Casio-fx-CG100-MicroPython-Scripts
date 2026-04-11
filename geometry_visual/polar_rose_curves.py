from matplotlib.pyplot import axis, grid, plot, show, text
import math

k = float(input("k (e.g. 3 or 2.5): "))
N = 600
step = 2 * math.pi / N if int(k) == k else 4 * math.pi / N

ts = [step * i for i in range(N+1)]
xs = [math.cos(k*t) * math.cos(t) for t in ts]
ys = [math.cos(k*t) * math.sin(t) for t in ts]

plot(xs, ys, "red")
axis([-1.2, 1.2, -1.2, 1.2])
grid("on")
text(-1.1, 1.1, "r=cos(" + str(k) + "*theta)")
show()

input("\nPress any key to exit: ")

