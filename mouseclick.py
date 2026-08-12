import turtle

screen = turtle.Screen()
screen.title("Draw Shapes with Mouse Click")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Function to draw a circle
def draw_circle(x, y):
    pen.penup()
    pen.goto(x, y - 30)
    pen.pendown()
    pen.circle(30)

# Function to draw a square
def draw_square(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    for _ in range(4):
        pen.forward(60)
        pen.right(90)

# Function to draw a triangle
def draw_triangle(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    for _ in range(3):
        pen.forward(70)
        pen.left(120)

# Left click → Circle
screen.onclick(draw_circle, btn=1)

# Middle click → Square
screen.onclick(draw_square, btn=2)

# Right click → Triangle
screen.onclick(draw_triangle, btn=3)

screen.mainloop()