import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)
		
def draw():
	window = turtle.Screen()
	window.bgcolor("brown")
	
	pato = turtle.Turtle()
	pato.shape("turtle")
	pato.color("white")
	pato.speed(2)
	draw_square(pato)
	
	
	window.exitonclick()

draw()
