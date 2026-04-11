from matplotlib.pyplot import axis, grid, plot, show, text
import math

v0 = float(input("Initial speed v0 (m/s): "))
angle = float(input("Angle (degrees): "))
g = 9.81

theta = angle * math.pi / 180
T = 2 * v0 * math.sin(theta) / g
R = v0**2 * math.sin(2*theta) / g
H = (v0 * math.sin(theta))**2 / (2*g)

print("Flight time:", round(T, 3), "s")
print("Range:", round(R, 3), "m")
print("Max height:", round(H, 3), "m")

N = 200
ts = [T * i / N for i in range(N+1)]
xs = [v0 * math.cos(theta) * t for t in ts]
ys = [v0 * math.sin(theta) * t - 0.5 * g * t**2 for t in ts]

plot(xs, ys, "blue")
axis([0, R*1.1, 0, H*1.2])
grid("on")
text(0, H, "v=" + str(v0) + " ang=" + str(angle))
show()

input("\nPress any key to exit: ")

