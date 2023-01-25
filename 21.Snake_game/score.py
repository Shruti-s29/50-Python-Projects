from turtle import Turtle, position

class scoreboard(Turtle):
    
    def __init__(self):
        # creation
        super().__init__()
        self.color('red')
        self.penup()
        self.goto(0,260)
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

class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.line()
        self.hideturtle()

    def line(self):
        self.penup()
        # left margin
        self.goto(-290,291)           
        self.setheading(270)
        while self.ycor()>=-290:
            self.draw()
        #down margin
        self.setheading(0)
        while self.xcor()<=290:
            self.draw()

        # right margin 
        self.setheading(90)
        while self.ycor()<=290:
            self.draw()
        
        #upper margin
        self.setheading(180)
        while self.xcor()>-290:
            self.draw()

    def draw(self):
        self.pensize(15)
        self.pendown()
        self.pencolor('grey')
        self.forward(20)
        



        

