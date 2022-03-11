from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("LuX's Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Score()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.11)
    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extends()
        scoreboard.increasescore()

    #detect with collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on=False
        scoreboard.game_over()
    #detect a collison with tail
    #if head collides with any segment in the tail trigger game over
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    snake.move()





screen.exitonclick()