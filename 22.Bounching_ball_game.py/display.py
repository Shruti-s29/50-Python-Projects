from turtle import * 

class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.upper_line()
        

    def upper_line(self):
        self.penup()
        self.goto(-250,250)
        while self.xcor()<250:
            self.pendown()
            self.pencolor('white')
            self.forward(10)
        self.penup()
        self.goto(-250,-250)
        while self.xcor()<250:
            self.pendown()
            self.pencolor('white')
            self.forward(10)



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 30, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def reset_position(self):
        self.goto(0,0)
        self.update_scoreboard()