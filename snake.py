from turtle import Turtle,Screen
import time

START_POSTIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 0
RIGHT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSTIONS:
            self.add_segement(position)
    def add_segement(self,position):
        num_square = Turtle("square")
        num_square.color("white") 
        num_square.penup()
        num_square.goto(position)
        self.segments.append(num_square)

    def extend_snake(self):
        self.add_segement(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            self.head.setheading(DOWN)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def left(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)