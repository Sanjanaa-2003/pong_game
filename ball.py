from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1   #set the ball speed to stg less or normal initially

    def move(self):
        new_x = self.xcor() + self.x_move   #adds few steps for the ball to move in x coord
        new_y = self.ycor() + self.y_move   #adds few steps for the ball to move in y coord
        self.goto(new_x, new_y)             #goes to new x and y

    def bounce_y(self):
        self.y_move *= -1                   #moves backwards by defined move distance in y dir

    def bounce_x(self):
        self.x_move *= -1                   ##moves backwards by defined move distance in x dir
        self.move_speed *= 0.9              #descreases the speed everytime it gets hit and has to bounce

    def reset_position(self):
        self.goto(0, 0)     #goes back to original position
        self.move_speed = 0.1     #sets back the initial speed
        self.bounce_x()
