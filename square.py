import turtle

sc=turtle.Screen()
sc.bgcolor("White")
sc.setup(500,499)
sc.title("Screen setup")
canvas=turtle.Turtle()
canvas.pensize(4)
canvas.pencolor("red")








for i in range(4):
    canvas.forward(90)
    canvas.right(90)


sc.exitonclick()