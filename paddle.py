from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")    #shape of paddle
        self.color("white")     #colour of paddle
        self.shapesize(stretch_wid=5, stretch_len=1)    #size of paddle
        self.penup()    #doesn't draw while moving
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20    #moves up by 20
        self.goto(self.xcor(), new_y)   #goes up

    def go_down(self):
        new_y = self.ycor() - 20    #moves down by 20
        self.goto(self.xcor(), new_y)   #goes down
