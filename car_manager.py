from turtle import  Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars =[]



    def car(self):
        random_chance = random.randint(1,6)
        if random_chance ==1:
            new_car =Turtle()
            new_car.penup()
            y_cord = random.randint(-240,240)
            new_car.goto(300,y_cord)
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            self.cars.append(new_car)

    def move_forward(self):
        for car in self.cars :
            car.forward(STARTING_MOVE_DISTANCE)












