from turtle import Screen
from snake import Snake, increase_speed
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
sleep_time = 0.1
game_is_on = False
game_mode = screen.numinput("Select Game Mode", "1:Walls Collision , 2: Without Walls collision",
                            default=1, minval=1, maxval=2)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

if game_mode:
    game_is_on = True
speed_list = [500, 1000, 1500, 2000, 2500]
while game_is_on:
    if scoreboard.score in speed_list:
        increase_speed()
        speed_list.remove(scoreboard.score)

    screen.update()
    time.sleep(sleep_time)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        sleep_time -= 0.001
        scoreboard.increase_score()

    if game_mode == 1 and (snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285):
        game_is_on = False
        scoreboard.game_over()

    if game_mode == 2:
        if snake.head.xcor() > 285 or snake.head.xcor() < -285:
            snake.head.setx(0 - snake.head.xcor())
        if snake.head.ycor() > 285 or snake.head.ycor() < -285:
            snake.head.sety(0 - snake.head.ycor())

    for part in snake.snake[1:]:
        if snake.head.distance(part) < 8:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
