from turtle import backward, forward, goto, hideturtle, left, pencolor, pendown, penup, right, speed

def sierpinski(length, depth):
    if depth == 0:
        for _ in range(3):
            forward(length)
            left(120)
    else:
        sierpinski(length/2, depth-1)
        forward(length/2)
        sierpinski(length/2, depth-1)
        backward(length/2)
        left(60)
        forward(length/2)
        right(60)
        sierpinski(length/2, depth-1)
        left(60)
        backward(length/2)
        right(60)

speed(0)
hideturtle()
penup()
goto(-80, -70)
pendown()
pencolor("green")
depth = int(input("Depth (1-5): "))
sierpinski(160, depth)

# input("\nPress any key to exit: ")

