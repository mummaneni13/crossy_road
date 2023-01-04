import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()

carmanager = CarManager()

screen.listen()
screen.onkey(timmy.move_forward, "Up")
screen.onkey(timmy.move_backward,"Down")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.car()
    carmanager.move_forward()

    for car in carmanager.cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            timmy.goto(0, -280)

    if timmy.ycor() > 200 :
        timmy.goto(0, -280)
        speed =0
        for car in carmanager.cars:
            speed +=5
            car.forward(speed)

screen.exitonclick()


