import turtle

screen = turtle.Screen()
pirate = turtle.Turtle()
angles = [160,-43,270,-97,-43,200,-940,17,-86]

for angle in angles:
  pirate.left(angle)
  pirate.forward(100)

screen.exitonclick()
screen.mainloop()