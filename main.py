from turtle import Screen
from Scripts.snake import Snake
from Scripts.food import Food
from Scripts.scoreboard import ScoreBoard
import time
import sys
import os

sys.path.append(os.path.join("./Scripts"))

screen = Screen()

screen.title("Welcom to Max Snake Game")
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision
    
    if snake.head.distance(food) < 20:
        score_board.increment_scoreboard()
        snake.extend_snake()
        food.refresh()
    
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score_board.gameover_board()
        game_is_on = False
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.gameover_board()
            game_is_on = False
    



screen.exitonclick()