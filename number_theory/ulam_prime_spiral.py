from casioplot import clear_screen, set_pixel, show_screen
def sieve(n):
    is_p = [True]*(n+1)
    is_p[0]=is_p[1]=False
    i=2
    while i*i<=n:
        if is_p[i]:
            for j in range(i*i,n+1,i):
                is_p[j]=False
        i+=1
    return is_p

N = 383*191
N = min(N, 15000)
is_p = sieve(N)


cx, cy = 192, 96
x, y = cx, cy
dx, dy = 1, 0
seg_len = 1
n = 1
steps_in_seg = 0
segs_done = 0

clear_screen()
while n <= N:
    px, py = x, y
    if 0<=px<384 and 0<=py<192:
        col = (220,0,0) if is_p[n] else (220,220,220)
        set_pixel(px, py, col)
    n += 1
    x += dx; y += dy
    steps_in_seg += 1
    if steps_in_seg == seg_len:
        steps_in_seg = 0
        segs_done += 1
        dx, dy = -dy, dx
        if segs_done % 2 == 0:
            seg_len += 1

show_screen()

# input("\nPress any key to exit: ")

