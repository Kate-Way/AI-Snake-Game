from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time
import pygame

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('#9CAF88')
screen.title('Snake Game')
screen.tracer(0)
clock = pygame.time.Clock()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.move_up, key='Up')
screen.onkey(snake.move_down, key='Down')
screen.onkey(snake.turn_left, key='Left')
screen.onkey(snake.turn_right, key='Right')

game_is_on = True

while game_is_on:
    screen.update()
    # for smooth transition of moving elements
    clock.tick(5)
    # screen update time
    time.sleep(0.05)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.keep_score()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail (check all elements except 0 (the head))
    for new_turtle in snake.new_turtles[1:]:
        if snake.head.distance(new_turtle) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
