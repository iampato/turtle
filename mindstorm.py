#pythoneer: Patrick
#date: Saturday Mar - 03 - 2018

import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    #create the turtle Brad -Draw a square
    wanja = turtle.Turtle()
    wanja.shape("turtle")
    wanja.color("yellow")
    wanja.speed(2)
    draw_square(wanja)
    for i in range(1,37):
		draw_square(wanja)
		wanja.right(10)

    window.exitonclick()


draw_art()
