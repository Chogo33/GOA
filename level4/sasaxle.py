from turtle import*
speed(20)

#tower 1 (have to color later)
shape("turtle")
color("pink")
begin_fill()
forward(200)
left(90)
forward(200)
right(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(50)
left(90)
forward(30)
right(90)
forward(200)
right(90)
end_fill()
#end of tower1

#tower 2 (have to color this one later too)
color("pink")
begin_fill()
forward(500)
right(90)
forward(200)
left(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
left(90)
forward(200)
end_fill()
#end of tower 2

#door
left(90)
forward(160)
color("yellow")
begin_fill()
left(90)
forward(90)
right(90)
forward(95)
right(90)
forward(90)
penup()
goto(110,150)
pendown()
right(90)
forward(20)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)
left(90)
forward(10)
end_fill()

#drosha
color("red")
penup()
goto(-417,250)
pendown()
forward(3)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(25)
right(90)
forward(100)
penup()
goto(-400,275)
pendown()
write("G O A",font=("halvecita",15))

#marcxena mxaris gaperadeba
penup()
goto(-300,0)
color("light blue")
begin_fill()
pendown
right(90)
forward(150)
right(133)
forward(221)
end_fill()

#marjvcena mxaris gaperadeba
color("light blue")
penup()
goto(-40,0)
pendown()
begin_fill()
left(43)
forward(150)
left(90)
forward(150)
left(133)
forward(220)
end_fill()

#karebi
penup()
goto(-45,0)
pendown()
color("pink")
begin_fill()
setheading(0)
left(90)
forward(90)
left(90)
forward(94)
left(90)
forward(90)
end_fill()

#king and queen
#king
color("black")
penup()
goto(-140,-300)
pendown()
right(180)
forward(60)
left(130)
forward(60)
exitonclick()