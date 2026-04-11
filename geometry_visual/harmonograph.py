from matplotlib.pyplot import axis, plot, show, text
import math

f1 = float(input("Freq 1 (e.g. 2.01): "))
f2 = float(input("Freq 2 (e.g. 3.0): "))
d = float(input("Damping (e.g. 0.002): "))
p = float(input("Phase diff (degrees): "))
p = p * math.pi / 180

N = 800
T = 50.0
ts = [T*i/N for i in range(N+1)]

xs = [math.exp(-d*t)*math.sin(2*math.pi*f1*t) for t in ts]
ys = [math.exp(-d*t)*math.sin(2*math.pi*f2*t + p) for t in ts]

plot(xs, ys, "blue")
axis([-1.1, 1.1, -1.1, 1.1])
text(-1.0, 1.0, "Harmonograph")
show()

# input("\nPress any key to exit: ")

