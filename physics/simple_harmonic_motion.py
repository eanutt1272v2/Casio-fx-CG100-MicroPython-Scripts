from matplotlib.pyplot import axis, grid, plot, show, text
import math

A = float(input("Amplitude A: "))
omega = float(input("Angular freq omega: "))
phi = float(input("Phase phi (degrees): "))
phi = phi * math.pi / 180

T = 2 * math.pi / omega
N = 300
ts = [3*T*i/N for i in range(N+1)]

xs = [A * math.cos(omega*t + phi) for t in ts]
vs = [-A * omega * math.sin(omega*t + phi) for t in ts]
accs = [-A * omega**2 * math.cos(omega*t + phi) for t in ts]

plot(ts, xs, "blue")
plot(ts, vs, "red")
plot(ts, accs, "green")
axis("auto")
grid("on")
text(0, A, "x(t) blue, v(t) red, a(t) green")
show()

# input("\nPress any key to exit: ")

