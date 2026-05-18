from turtle import Turtle, Screen
import random
redtur = Turtle(shape="turtle")
orangetur = Turtle(shape="turtle")
yellowtur = Turtle(shape="turtle")
greentur = Turtle(shape="turtle")
bluetur = Turtle(shape="turtle")
purpletur = Turtle(shape="turtle")

# def move_forward():
#     tur.forward(20)
# def move_backward():
#     tur.backward(20)
# def turn_left():
#     tur.left(20)
# def turn_right():
#     tur.right(20)
# def clear_screen():
#     tur.clear()
#     tur.up()
#     tur.home()
#     tur.down()
#screen.listen()
#screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear_screen, "c")

screen = Screen()
screen.setup(width=600, height=600)

user_input = screen.textinput(title="Make your bet", prompt="choose")
is_race_on = False
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = (redtur, orangetur, yellowtur, greentur, bluetur, purpletur)
c=0
def positions():
    c=0
    x = -300
    y = -300
    for turtle in turtles:
        turtle.color(colours[c])
        c=c+1
        turtle.penup()
        turtle.goto(x, y)
        y=y+100

positions()

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>300:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You win!, The {winning_color} turtle wins!")
            else:
                print(f"You lose!, The {winning_color} turtle wins!")


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)













screen.exitonclick()
