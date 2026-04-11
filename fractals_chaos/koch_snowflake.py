from turtle import forward, goto, hideturtle, left, pencolor, pendown, penup, right, speed

def koch(length, depth):
    if depth == 0:
        forward(length)
    else:
        koch(length/3, depth-1)
        left(60)
        koch(length/3, depth-1)
        right(120)
        koch(length/3, depth-1)
        left(60)
        koch(length/3, depth-1)

speed(0)
hideturtle()
penup()
goto(-90, 50)
pendown()
pencolor("blue")
depth = int(input("Depth (1-4): "))
side = 170

for _ in range(3):
    koch(side, depth)
    right(120)

# input("\nPress any key to exit: ")

