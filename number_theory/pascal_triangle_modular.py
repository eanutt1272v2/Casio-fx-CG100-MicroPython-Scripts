from casioplot import clear_screen, set_pixel, show_screen
def pascal_row(prev):
    row = [1]
    for i in range(len(prev) - 1):
        row.append(prev[i] + prev[i+1])
    row.append(1)
    return row

k = int(input("Modulus k (e.g. 2 or 3): "))
rows = 20
row = [1]
clear_screen()
colours = [
    (220,0,0),(0,180,0),(0,0,220),(180,120,0),
    (0,160,160),(160,0,160),(80,80,80),(0,0,0)
]

for r in range(rows):
    for c in range(len(row)):
        val = row[c]
        mod_val = val % k
        col = colours[mod_val % len(colours)]
        px = 192 + (c - r // 2) * 9
        py = 5 + r * 9
        for dx in range(7):
            for dy in range(7):
                set_pixel(px + dx, py + dy, col)
    row = pascal_row(row)

show_screen()

input("\nPress any key to exit: ")

