import turtle
win=turtle.Screen()

#square
crush=turtle.Turtle()
crush.color("red")
crush.forward(50)
crush.left(90)
crush.forward(50)
crush.left(90)
crush.forward(50)
crush.left(90)
crush.forward(50)
crush.left(90)
#triangle
turtle2=turtle.Turtle()
turtle2.color("green")
turtle2.penup()
turtle2.goto(-50,-50)
turtle2.pendown()
turtle2.forward(60)
turtle2.left(120)
turtle2.forward(60)
turtle2.left(120)
turtle2.forward(60)
turtle2.left(120)

win.exitonclick()
win.mainloop()