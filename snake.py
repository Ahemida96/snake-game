from turtle import Turtle

MOV_DIS = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
INITIAL_PARTS = 5


def increase_speed():
    global MOV_DIS
    MOV_DIS += 2


class Snake:

    def __init__(self):
        self.snake = []
        self.x_cor = 0
        self.y_cor = 0
        self.create_snake()
        self.head = self.snake[0]
        self.head.shape("circle")

    def create_snake(self):
        for _ in range(INITIAL_PARTS):
            self.add_segment(self.x_cor, self.y_cor)
            self.x_cor -= 20

    def add_segment(self, x_position, y_position):
        part_of_snake = Turtle(shape="square")
        part_of_snake.pu()
        part_of_snake.color("gray90")
        part_of_snake.setposition(x_position, y_position)
        self.snake.append(part_of_snake)

    def extend_snake(self):
        self.add_segment(self.snake[-1].xcor(), self.snake[-1].ycor())

    def move(self):
        for part in range(len(self.snake) - 1, 0, -1):
            previous_part_pos = self.snake[part - 1].position()
            self.snake[part].goto(previous_part_pos)
            self.snake[-1].shape("arrow")
            self.snake[-2].shape("square")
        self.snake[0].forward(MOV_DIS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


''' HOW TO MAKE ALL PART MOVE TOGETHER
FOR THE LAST PART TO THE HEAD
    GET THE ONE'S POS BEFORE THE CURRENT PART
    MAKE THE CURRENT PART POS EQUAL TO IT
HERE MAKE THE HEAD TO MOVE
'''