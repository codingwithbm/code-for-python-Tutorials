from turtle import *
color("black")
begin_fill()

#stripe1

for i in range(2):
	forward(200)
	left(90)
	forward(40)
	left(90)
end_fill()

#stripe2

begin_fill()

right(90)
forward(40)
left(90)
color("red")
for i in range(2):
	forward(200)
	left(90)
	forward(40)
	left(90)
end_fill()


#stripe3

begin_fill()

right(90)
forward(40)
left(90)
color("gold")
for i in range(2):
	forward(200)
	left(90)
	forward(40)
	left(90)
end_fill()






done()
