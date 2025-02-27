from turtle import Turtle,Screen
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()
        
    def refresh(self):
        rand_x_axis = random.randint(-280,280)
        rand_y_axis = random.randint(-280,280)
        self.goto(rand_x_axis,rand_y_axis)

