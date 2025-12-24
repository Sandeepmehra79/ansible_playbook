from turtle import Turtle , Screen
import random
from player import Player
from car import Car
screen = Screen()
screen.setup(800,800)
screen.listen()
screen.bgcolor("black")
tim = Player()

screen.onkeypress(tim.move_left, "a")
screen.onkeypress(tim.move_right, "d")
screen.onkeypress(tim.move_up, "w")
screen.onkeypress(tim.move_down, "s")

vehicles = []

for i in range(10):
    start_y = -120
    tim = Car()
    tim.sety((i*30)+start_y)
    vehicles.append(tim)

while True:
    random_int = random.randint(0, len(vehicles)-1)
    random_vehicle = vehicles[random_int]
    random_vehicle.forward(10)
    if random_vehicle.xcor() > 400:
        random_vehicle.hideturtle()
        random_vehicle.setx(-400)
        random_vehicle.showturtle()

screen.exitonclick()