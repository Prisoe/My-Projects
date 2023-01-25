import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move()

    # Detect Turtle colliding with cars
    for car in cars.car:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    # Detect Turtle reaching Finishing Line
    if player.ycor() > 280:
        player.reset_turtle()
        cars.level_up()
        score.update_level()

screen.exitonclick()
