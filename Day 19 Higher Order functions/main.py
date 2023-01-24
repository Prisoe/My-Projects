import random
from turtle import Turtle, Screen

# timmy = Turtle(shape="turtle")
# screen = Screen()

# screen.listen()
#
# """Etch a sketch app"""
#
#
# def move_forward():
#     timmy.forward(50)
#
#
# def move_backward():
#     timmy.back(50)
#
#
# def counter_clockwise():
#     timmy.left(90)
#     timmy.forward(10)
#
#
# def clockwise():
#     timmy.right(90)
#     timmy.forward(10)
#
#
# def u_turn():
#     timmy.right(90)
#     timmy.right(90)
#     timmy.forward(50)
#
#
# def clear_drawing():
#     timmy.reset()
#
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=counter_clockwise)
# screen.onkey(key="d", fun=clockwise)
# screen.onkey(key="space", fun=u_turn)
# screen.onkey(key="c", fun=clear_drawing)

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ["red", "blue", "yellow", "green", "orange", "indigo"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtle = []

for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fast")
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_position[turtle])
    new_turtle.color(colours[turtle])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
