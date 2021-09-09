import turtle

def line(t,x,y,color,len):
  t.goto(x,y)
  t.color(color)
  t.forward(len)
wn = turtle.Screen()
crush = turtle.Turtle()
line(crush,10,10,"red",50)
crush.right(35)
line(crush,50,-10,"green",40)
wn.exitonclick()
wn.mainloop()