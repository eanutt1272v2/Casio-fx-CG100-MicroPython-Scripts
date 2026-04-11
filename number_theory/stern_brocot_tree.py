from casioplot import clear_screen, draw_string, getkey, show_screen
def sb_navigate():
    lo_n, lo_d = 0, 1
    hi_n, hi_d = 1, 0
    mid_n = lo_n + hi_n
    mid_d = lo_d + hi_d

    clear_screen()
    draw_string(0, 0, "Stern-Brocot Navigator")
    draw_string(0, 15, "4=left 6=right 5=show EXE=quit")
    step = 0

    while True:
        mid_n = lo_n + hi_n
        mid_d = lo_d + hi_d
        msg = "Step " + str(step) + ": " + str(mid_n) + "/" + str(mid_d)
        clear_screen()
        draw_string(0, 0, "Stern-Brocot Navigator")
        draw_string(0, 20, msg)
        draw_string(0, 40, "Value~" + str(round(mid_n/mid_d, 5)))
        draw_string(0, 60, "4=left  6=right  EXE=quit")
        show_screen()
        k = getkey()
        if k == 95:
            break
        elif k == 73:
            lo_n, lo_d = mid_n, mid_d
        elif k == 71:
            hi_n, hi_d = mid_n, mid_d
        step += 1

sb_navigate()

# input("\nPress any key to exit: ")

