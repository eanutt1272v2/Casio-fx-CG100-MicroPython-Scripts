from matplotlib.pyplot import axis, plot, show, text
import math

R = float(input("R (large circle): "))
r = float(input("r (small circle): "))
mode = input("Type: e=epi, h=hypo: ")

N = 800
ts = [2 * math.pi * i / N for i in range(N+1)]

if mode == "e":
    xs = [(R+r)*math.cos(t) - r*math.cos((R+r)*t/r) for t in ts]
    ys = [(R+r)*math.sin(t) - r*math.sin((R+r)*t/r) for t in ts]
    title = "Epicycloid R=" + str(R) + " r=" + str(r)
else:
    xs = [(R-r)*math.cos(t) + r*math.cos((R-r)*t/r) for t in ts]
    ys = [(R-r)*math.sin(t) - r*math.sin((R-r)*t/r) for t in ts]
    title = "Hypocycloid R=" + str(R) + " r=" + str(r)

plot(xs, ys, "purple")
axis("auto")
text(min(xs), max(ys), title)
show()

input("\nPress any key to exit: ")

