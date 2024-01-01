from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0    #initializes left and right score to 0
        self.r_score = 0
        self.update_scoreboard()    #updates the score board

    def update_scoreboard(self):
        self.clear()    #clears previous scores
        self.goto(-100, 200)    #goes to left score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))    #Font format
        self.goto(100, 200)     #goes to right score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))    #Font format

    def l_point(self):
        self.l_score += 1   #increments left score
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1   #increments right score
        self.update_scoreboard()