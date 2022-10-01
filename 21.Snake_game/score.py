from turtle import Turtle


class scoreboard(Turtle):
    
    def __init__(self):
        # creation
        super().__init__()
        self.color('red')
        self.penup()
        self.goto(0,275)
        # score 
        self.score = 0
        self.write(arg=f'Your Score : {self.score}',align='center', font=('arial',16))
        # hide symbol
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Your Score : {self.score}',align='center', font=('arial',16))

    def game_over(self):
        self.goto(0,0)
        self.write(arg='--GAME OVER--', align='center',font=('arial',18))