from turtle import Turtle
import random as rn


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.color(rn.choice(['PaleGreen4', 'OliveDrab', 'ForestGreen']))
        random_x = rn.randint(-280, 280)
        random_y = rn.randint(-280, 280)
        self.goto(random_x, random_y)
