from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("beige")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "W")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "S")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "A")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "D")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor()<-290 or snake.head.xcor()>290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
