import random
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

timmy.color("Purple")

"""Draw a square"""
# for _ in range(4):
#     timmy.forward(150)
#     timmy.right(90)


"""Draw a dashed Line"""

# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


"""Draw different Shapes"""

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

#
# def draw_shape(n):
#     angle = 360 / n
#     for _ in range(n):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for number_of_sides in range(3, 11):
#     timmy.color(random.choice(colours))
#     draw_shape(number_of_sides)


"""Random Walk"""

direction = [0, 90, 180, 270]
for _ in range(500):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))
    timmy.pensize(5)
    timmy.speed("fastest")


screen = Screen()
screen.exitonclick()