from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("Black")
screen.tracer(0)
screen.listen()

# snake and other stuf settings

snake = Snake()
food1 = Food()
scoreboard = ScoreBoard()

# keys events
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down ")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.06)
    snake.move()

    # check collision with food.
    if snake.head.distance(food1) < 15:
        food1.change_place()
        scoreboard.add_score()
        snake.extend()
    # check collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # check collision with any tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
