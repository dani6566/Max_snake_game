from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT ,font= FONT)

    def increment_scoreboard(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def gameover_board(self):
        self.clear()
        self.goto(0,30)
        self.write(f"Score: {self.score}",align=ALIGNMENT ,font= FONT)
        self.goto(0,0)
        self.write(f"Game Over",align=ALIGNMENT ,font= FONT)