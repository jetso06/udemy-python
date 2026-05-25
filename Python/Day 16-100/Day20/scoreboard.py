from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

with open("Scoreboard.txt", "r") as file:
    highest_score = file.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(highest_score)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,290)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {int(self.high_score)}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)

        with open(f"Scoreboard.txt", "w") as file:
            file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        #self.clear()
        self.score = self.score + 1
        self.update_scoreboard()



