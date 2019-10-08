import turtle

turtle.setup(600,400,0,0)
turtle.bgcolor("red")
turtle.fillcolor("yellow")
turtle.color("yellow")
turtle.speed(10)

arr = [
	{"goto":{"left":-260,"right":105},"heading":0,"forward":120,"left":216},
	{"goto":{"left":-100,"right":180},"heading":300,"forward":40,"left":144},
	{"goto":{"left":-50,"right":95},"heading":60,"forward":40,"left":144},
	{"goto":{"left":-25,"right":60},"heading":180,"forward":40,"left":144},
	{"goto":{"left":-100,"right":10},"heading":300,"forward":40,"left":144}
]

for i in range(len(arr)):
	data = arr[i]
	turtle.begin_fill()
	turtle.up()
	turtle.goto(data["goto"]["left"],data["goto"]["right"])
	turtle.setheading(data["heading"])
	turtle.down()
	for j in range(5):
		turtle.forward(data["forward"])
		turtle.left(data["left"])
	turtle.end_fill()

turtle.hideturtle()
turtle.done()