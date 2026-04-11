from matplotlib.pyplot import axis, grid, plot, show, text
import math

a = float(input("a (e.g. 3): "))
b = float(input("b (e.g. 2): "))
delta = float(input("delta in degrees (e.g. 90): "))
delta = delta * math.pi / 180

N = 500
ts = [2 * math.pi * i / N for i in range(N+1)]
xs = [math.sin(a * t + delta) for t in ts]
ys = [math.sin(b * t) for t in ts]

plot(xs, ys, "blue")
axis([-1.2, 1.2, -1.2, 1.2])
grid("on")
text(-1.1, 1.1, "a=" + str(a) + " b=" + str(b) + " d=" + str(int(delta*180/math.pi)))
show()

input("\nPress any key to exit: ")

