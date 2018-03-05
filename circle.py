import turtle

def draw_circle():
	window = turtle.Screen()
	window.bgcolor("blue")
	
	#create the turtle angie -Draw a circle
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("red")
	angie.circle(100)
	
	window.exitonclick()

draw_circle()
	
