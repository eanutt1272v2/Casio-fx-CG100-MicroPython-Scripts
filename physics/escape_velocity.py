import math

try:
    from casioplot import getkey
except ImportError:
    getkey = None


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():

    G = 6.674e-11

    bodies = {
        "Sun": (1.989e30, 6.957e8),
        "Mercury": (3.301e23, 2.440e6),
        "Venus": (4.867e24, 6.052e6),
        "Earth": (5.972e24, 6.371e6),
        "Moon": (7.342e22, 1.737e6),
        "Mars": (6.417e23, 3.390e6),
        "Ceres": (9.393e20, 4.697e5),
        "Jupiter": (1.898e27, 7.149e7),
        "Saturn": (5.683e26, 6.027e7),
        "Uranus": (8.681e25, 2.556e7),
        "Neptune": (1.024e26, 2.476e7),
        "Pluto": (1.303e22, 1.188e6),
        "Haumea": (4.006e21, 8.160e5),
        "Makemake": (3.100e21, 7.150e5),
        "Eris": (1.660e22, 1.163e6),
    }

    names = list(bodies.keys())

    print("--- Celestial Bodies ---")
    for i in range(len(names)):
        print(str(i + 1) + ": " + names[i])
    print(str(len(names) + 1) + ": Custom")

    choice = int(input("Choice: "))

    if choice <= len(names):
        name = names[choice - 1]
        M, R = bodies[name]
    else:
        name = "Custom"
        M = float(input("M (kg): "))
        R = float(input("R (m): "))

    ve = math.sqrt(2 * G * M / R)

    print("\n" + name + " Escape Velocity:")
    print(round(ve, 2), "m/s")
    print(round(ve / 1000, 2), "km/s")
    wait_for_exit()


main()
