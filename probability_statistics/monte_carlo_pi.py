import random
from matplotlib.pyplot import axis, scatter, show, text

N = int(input("Samples N (e.g. 500): "))
inside = 0
xs_in, ys_in = [], []
xs_out, ys_out = [], []

for _ in range(N):
    x = random.random()
    y = random.random()
    if x*x + y*y <= 1:
        inside += 1
        xs_in.append(x)
        ys_in.append(y)
    else:
        xs_out.append(x)
        ys_out.append(y)

pi_est = 4 * inside / N
print("pi estimate:", pi_est)
print("Error:", abs(pi_est - 3.14159265))

scatter(xs_in, ys_in)
scatter(xs_out, ys_out)
axis([0, 1, 0, 1])
text(0, 0.95, "pi~" + str(round(pi_est, 4)))
show()

input("\nPress any key to exit: ")

