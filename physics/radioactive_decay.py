from matplotlib.pyplot import axis, grid, plot, show, text
import math

N0 = float(input("Initial amount N0: "))
half_life = float(input("Half-life T_1/2: "))
lam = math.log(2) / half_life
T_end = 5 * half_life

N = 300
ts = [T_end * i / N for i in range(N+1)]
Ns = [N0 * math.exp(-lam * t) for t in ts]

plot(ts, Ns, "blue")

plot([half_life, half_life], [0, N0/2], "red")
plot([0, half_life], [N0/2, N0/2], "red")
axis([0, T_end, 0, N0*1.05])
grid("on")
text(0, N0, "N0=" + str(N0) + " T1/2=" + str(half_life))
text(half_life, N0*0.1, "T_1/2")
show()

# input("\nPress any key to exit: ")

