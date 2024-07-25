from turtle import Turtle, Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# create a snake body
# move the snake
# create snake food
# detect collision with food
# create a scoreboard
# detect collision with wall
# detect collision with tail

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# keyboard input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# start game
move_snake = True
while move_snake:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        move_snake = False

    # Detect collision with tail.
    for segment in snake.snake_blocks[1:len(snake.snake_blocks)]:
    # if head collides with any segment in the tail
        # trigger game_over
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            move_snake = False
            scoreboard.game_over()


screen.exitonclick()
