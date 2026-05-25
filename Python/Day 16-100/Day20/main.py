from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295 or snake.head.ycor() > 295:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segments in snake.segments[1:]:
        if segments.distance(snake.head) < 10:
            scoreboard.reset()

screen.exitonclick()