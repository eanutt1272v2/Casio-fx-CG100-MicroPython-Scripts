from casioplot import clear_screen, draw_string, set_pixel, show_screen
import random

W = 48
H = 48
GENS = int(input("Generations (e.g. 500): "))
SEED = int(input("Seed (0=random): ") or "0")
ALIVE = (255, 255, 255)
DEAD = (0, 0, 0)

MASK = (1 << W) - 1

def hadd(a, b):
    return (a ^ b), (a & b)

def fadd(a, b, c):
    s1, c1 = hadd(a, b)
    s2, c2 = hadd(s1, c)
    return s2, (c1 | c2)

def step(grid):
    new = [0] * H
    for y in range(H):
        rp = grid[(y - 1) % H]
        rc = grid[y]
        rn = grid[(y + 1) % H]

        lp = ((rp >> 1) | ((rp & 1) << (W - 1))) & MASK
        xp = ((rp << 1) | (rp >> (W - 1))) & MASK
        lc = ((rc >> 1) | ((rc & 1) << (W - 1))) & MASK
        xc = ((rc << 1) | (rc >> (W - 1))) & MASK
        ln = ((rn >> 1) | ((rn & 1) << (W - 1))) & MASK
        xn = ((rn << 1) | (rn >> (W - 1))) & MASK

        s1, c1 = fadd(lp, rp, xp)
        s2, c2 = fadd(lc, xc, ln)
        s3, c3 = fadd(rn, xn, 0)
        s4, c4 = fadd(s1, s2, s3)
        sc, cr1 = fadd(c1, c2, c3)
        b1, cr2 = hadd(sc, c4)
        b0 = s4
        b2 = cr1 | cr2

        n3 = (~b2) & b1 & b0
        n2 = (~b2) & b1 & (~b0)
        new[y] = (n3 | (n2 & rc)) & MASK
    return new

def draw_diff(prev, curr):
    for y in range(H):
        changed = prev[y] ^ curr[y]
        if not changed:
            continue
        row = curr[y]
        py = y << 2
        for x in range(W):
            if changed & (1 << x):
                col = ALIVE if (row >> x) & 1 else DEAD
                px = x << 2
                set_pixel(px, py, col)
                set_pixel(px + 1, py, col)
                set_pixel(px + 2, py, col)
                set_pixel(px, py + 1, col)
                set_pixel(px + 1, py + 1, col)
                set_pixel(px + 2, py + 1, col)
                set_pixel(px, py + 2, col)
                set_pixel(px + 1, py + 2, col)
                set_pixel(px + 2, py + 2, col)

def draw_all(grid):
    for y in range(H):
        row = grid[y]
        py = y << 2
        for x in range(W):
            col = ALIVE if (row >> x) & 1 else DEAD
            px = x << 2
            for dy in range(3):
                for dx in range(3):
                    set_pixel(px + dx, py + dy, col)


if SEED:
    random.seed(SEED)
grid = []
for i in range(H):
    r = random.randint(0, 0x3FFFFFFF)
    r = r | (random.randint(0, 0x3FFFFFFF) << 30)
    r = r | (random.randint(0, 0x3FFFFFFF) << 60)
    grid.append(r & MASK)

clear_screen()
draw_all(grid)
show_screen()

for gen in range(1, GENS + 1):
    prev = grid
    grid = step(grid)
    draw_diff(prev, grid)
    for dy in range(10):
        for dx in range(72):
            set_pixel(dx, dy, (150, 150, 150))
    draw_string(0, 0, "Gen " + str(gen), (0, 0, 200), "small")
    show_screen()

# input("\nPress any key to exit: ")

