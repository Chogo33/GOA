from turtle import*
speed(20)

width(7)

color("blue")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square 

#door
forward(200)
left(180)
forward(70)
color("grey")
begin_fill()
right(90)
forward(120)
left(90)
forward(70)
left(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()
color("green")
begin_fill()
right(150)
forward(195)
left(118)
forward(197)
end_fill()
#end of roof

#1 window
penup()
goto(30,170)
pendown()
color("yellow")
begin_fill()
left(32)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

#2 window
penup()
goto(170,170)
pendown()
begin_fill()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()






exitonclick()


