import turtle
win=turtle.Screen()
crush = turtle.Turtle()

for f in range(3):
  crush.forward(60)
  crush.left(120)

crush.penup()
crush.goto(-50,0)
crush.color("Blue")
crush.pendown()
for l in range(4):
  crush.forward(40)
  crush.left(90)

crush.penup()
crush.goto(70,0)
crush.color("green")
crush.pendown()
for w in range(6):
  crush.forward(50)
  crush.left(60)
print("I made a change and it will be sent to github")

win.exitonclick()
win.mainloop()

