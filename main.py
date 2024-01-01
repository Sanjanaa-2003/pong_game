from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()   #displays the screen
screen.bgcolor("black")     #background color is black
screen.setup(width=800, height=600)     #window of size 800 by 600
screen.title("Pong")    #sets title
screen.tracer(0)        #turns off animation;doesnt show the paddle moving from (0,0) to (350,0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()     #listens to keystrokes
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update() #once the animation is turned off using tracer method and the paddle is created in the baxkground the update method is called to refresh the screen
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #ball is 20 pixels therefoew 300-20=280 is where the ball crosses the border
    #if distance of collision with wall is set to 300 the ball would have crossed the wall

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        #ball(20) + paddle(20)+diatance to br maintained between ball and paddle to avoid collision(10)=50
        #if the distance is less than the required distance to be mainrained(50)

    #Detect R paddle misses
    if ball.xcor() > 380:   #if ball hits right wall left score increases
        ball.reset_position()
        scoreboard.l_point()    #increments score by 1

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()    #increments right score by 1

screen.exitonclick()