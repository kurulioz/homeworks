from turtle import *
shape("turtle")

speed(15)

width(7)

color("purple")



forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)

color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(180,120)
pendown()

color("blue")
begin_fill()
left(120)
right(180)
forward(20)
right(90)
forward(50)
right(90)
forward(20)
right(90)
forward(50)
end_fill()


penup()
goto(20,120)
pendown()

color("blue")
begin_fill()
right(180)
forward(50)
right(90)
forward(20)
right(90)
forward(50)
right(90)
forward(20)
end_fill()


exitonclick()
