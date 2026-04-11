from matplotlib.pyplot import axis, grid, plot, show, text
import math

g = 9.81
Ls = [0.05 + 0.05*i for i in range(40)]
Ts_exact = [2*math.pi*math.sqrt(L/g) for L in Ls]
Ts_approx = Ts_exact

theta = float(input("Initial angle (degrees): "))
theta_r = theta * math.pi / 180
Ts_large = [2*math.pi*math.sqrt(L/g)*(1 + theta_r**2/16) for L in Ls]

plot(Ls, Ts_exact, "blue")
plot(Ls, Ts_large, "red")
axis([0, max(Ls)*1.1, 0, max(Ts_large)*1.1])
grid("on")
text(0, max(Ts_large)*0.95, "blue: small-angle  red: large-angle corr")
show()

input("\nPress any key to exit: ")

