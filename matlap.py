import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")
	
	brad = turtle.Turtle()
	brad.color("blue")
	for i in range(1,36):
		
		for i in range(1,5):
			brad.forward(100)
			brad.right(90)
		brad.right(10)
		
		
draw_square()
