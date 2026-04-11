from matplotlib.pyplot import axis, plot, show, text
import math

R = float(input("Outer radius R: "))
r = float(input("Inner radius r: "))
d = float(input("Pen distance d: "))

N = 1000
lcm_val = R * r // math.gcd(int(R), int(r))
ts = [2 * math.pi * i / N * (lcm_val / r) for i in range(N+1)]

xs = [(R-r)*math.cos(t) + d*math.cos((R-r)*t/r) for t in ts]
ys = [(R-r)*math.sin(t) - d*math.sin((R-r)*t/r) for t in ts]

plot(xs, ys, "magenta")
axis("auto")
text(min(xs), max(ys), "Spirograph")
show()

input("\nPress any key to exit: ")

