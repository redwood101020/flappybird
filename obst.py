import turtle
import random
import time
wn = turtle.Screen()
pen = turtle.Turtle()
ran1 = 0
ran2 = 0
ran3 = 0
ran4 = 0
ran5 = 0
ran6 = 0

pl = turtle.Turtle()
def left(val):
	pen.left(val)
def right(val):
	pen.right(val)
def forward(val):
	pen.forward(val)
def backward(val):
	pen.backward(val)
def up():
	pen.up()
def down():
	pen.down()
def goto(val1, val2):
	pen.goto(val1, val2)
def begin_fill():
	pen.begin_fill()
def end_fill():
	pen.end_fill()
def rand(val1, val2):
	return(random.randint(val1, val2))
def color(val1):
	pen.color(val1)
	pen.fillcolor(val1)

pen.speed(0)
pl.up()
pl.goto(-290, 0)

def draw_map():
	global ran1
	global ran2
	global ran3
	global ran4
	global ran5
	global ran6
	up()
	goto(-300, -200)
	down()
	pen.fillcolor("#1AA7EC")
	begin_fill()
	for i in range(2):
		forward(600)
		left(90)
		forward(400)
		left(90)
	end_fill()
	for i in range(6):
		color("#009C41")
		up()
		goto(int(-200 + i * 85), 200)
		down()
		begin_fill()
		for j in range(2):
			right(90)
			forward(400)
			right(90)
			forward(25)
		end_fill()
		up()
		goto(int(-200 + i * 85), 200)
		right(90)
		if i == 0:
			ran1 = rand(2, 35)
			forward(ran1 * 10)
		elif i == 1:
			ran2 = rand(2, 35)
			forward(ran2 * 10)
		elif i == 2:
			ran3 = rand(2, 35)
			forward(ran3 * 10)
		elif i == 3:
			ran4 = rand(2, 35)
			forward(ran4 * 10)
		elif i == 4:
			ran5 = rand(2, 35)
			forward(ran5 * 10)
		elif i == 5:
			ran6 = rand(2, 35)
			forward(ran6 * 10)
		#forward(rand(2, 35) * 10)
		left(90)
		forward(3)
		begin_fill()
		for j in range(2):
			left(90)
			forward(6)
			left(90)
			forward(31)
		end_fill()
		backward(3)
		right(90)
		forward(31)
		left(90)
		forward(3)
		begin_fill()
		for j in range(2):
			left(90)
			forward(6)
			left(90)
			forward(31)
		end_fill()
		backward(3)
		right(90)
		backward(32)
		down()
		color("#1AA7EC")
		begin_fill()
		for j in range(2):
			forward(26)
			right(90)
			forward(25)
			right(90)
		end_fill()
		color("black")
		left(90)
	up()
	goto(270, 0)
	color("#80EF08")
	down()
	begin_fill()
	for i in range(2):
		right(90)
		forward(10)
		right(90)
		forward(17)
	end_fill()
	color("#818589")
	right(90)
	begin_fill()
	for i in range(2):
		forward(30)
		left(90)
		forward(3)
		left(90)
	end_fill()
	goto(270, 200)
	forward(400)

def countdown():
	up()
	color("#818589")
	goto(-10, 300)
	pen.write("3", font=('Arial', 20, 'normal'))
	time.sleep(1)
	goto(-10, 300)
	color("#ffffff")
	down()
	begin_fill()
	pen.setheading(0)
	for i in range(4):
		forward(50)
		left(90)
	end_fill()
	up()
	color("#818589")
	goto(-10, 300)
	pen.write("2", font=('Arial', 20, 'normal'))
	time.sleep(1)
	goto(-10, 300)
	color("#ffffff")
	down()
	begin_fill()
	pen.setheading(0)
	for i in range(4):
		forward(50)
		left(90)
	end_fill()
	up()
	color("#818589")
	goto(-10, 300)
	pen.write("1", font=('Arial', 20, 'normal'))
	time.sleep(1)
	goto(-10, 300)
	color("#ffffff")
	down()
	begin_fill()
	pen.setheading(0)
	for i in range(4):
		forward(50)
		left(90)
	end_fill()
	up()
def plup():
	'''if pl.ycor() < 200:
		pl.sety(pl.ycor()+15)
	else:
		pl.sety(200)'''
	if pl.ycor() + 15 >= 200:
		pl.sety(200)
	else:
		pl.sety(pl.ycor()+15)

def pldown():
	if pl.ycor() - 15 <= -200:
		pl.sety(-200)
	else:
		pl.sety(pl.ycor()-15)

def onpipe():
	if -200 > pl.xcor() and -225 < pl.xcor():
		return(1)
	elif -115 > pl.xcor() and -140 < pl.xcor():
		return(2)
	elif -30 > pl.xcor() and -55 < pl.xcor():
		return(3)
	elif 55 > pl.xcor() and 30 < pl.xcor():
		return(4)
	elif 140 > pl.xcor() and 115 < pl.xcor():
		return(5)
	elif 225 > pl.xcor() and 200 < pl.xcor():
		return(6)
	else:
		return(7)

def die():
	color("#818589")
	goto(-50, 300)
	pen.write("you died", font=('Arial', 20, 'normal'))

draw_map()
countdown()
turtle.listen()
turtle.onkeypress(plup,'Up')
turtle.onkeypress(pldown,'Down')
while(1):
	pl.setx(pl.xcor()+0.6)
	if pl.xcor() > 270:
		color("#818589")
		goto(-50, 300)
		pen.write("you win", font=('Arial', 20, 'normal'))
		break
	if onpipe() == 1:
		if ((ran1 - 20) * -10) - 25 > pl.ycor() or (ran1 - 20) * -10 < pl.ycor():
			break
	elif onpipe() == 2:
		if ((ran2 - 20) * -10) - 25 > pl.ycor() or (ran2 - 20) * -10 < pl.ycor():
			break
	elif onpipe() == 3:
		if ((ran3 - 20) * -10) - 25 > pl.ycor() or (ran3 - 20) * -10 < pl.ycor():
			break
	elif onpipe() == 4:
		if ((ran4 - 20) * -10) - 25 > pl.ycor() or (ran4 - 20) * -10 < pl.ycor():
			break
	elif onpipe() == 5:
		if ((ran5 - 20) * -10) - 25 > pl.ycor() or (ran5 - 20) * -10 < pl.ycor():
			break
	elif onpipe() == 6:
		if ((ran6 - 20) * -10) - 25 > pl.ycor() or (ran6 - 20) * -10 < pl.ycor():
			break

wn.exitonclick()
