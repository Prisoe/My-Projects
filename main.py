import turtle
from turtle import Turtle, Screen
import random

color_palette_rgb = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]

tim = Turtle()
my_screen = Screen()
my_screen.bgcolor("black")
turtle.colormode(255)
tim.penup()
tim.hideturtle()



tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
tim.speed("fastest")


for dots_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_palette_rgb))
    tim.forward(50)
    if dots_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



my_screen.exitonclick()