import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_speed = MOVE_INCREMENT

    def create_car(self):
        random_dice =random.randint(1, 6)
        if random_dice ==1:
            tur = Turtle("square")
            tur.color(random.choice(COLORS))
            tur.penup()
            tur.setheading(180)
            tur.turtlesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(tur)
            random_y = random.randint(-230, 230)
            tur.goto(300, random_y)


    def move_cars(self):
        for cars in self.all_cars:
            cars.forward(self.move_speed)

    def speedy_cars(self):
        self.move_speed *= 1.2







