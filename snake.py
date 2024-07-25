from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake():

    def __init__(self):
        self.snake_blocks = []
        self.snake_starting_positions = []
        self.create_snake()
        self.head = self.snake_blocks[0]

    def create_snake(self):
        # snake_length = 3
        # for snake_index in range(0, snake_length):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle()
        snake.shape('square')
        snake.color("white")
        snake.penup()
        snake.goto(position)

        self.snake_blocks.append(snake)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.snake_blocks[-1].position())
        # [-1] finds the last segment

    def move(self):
        for block in range(len(self.snake_blocks) - 1, 0, -1):
            new_x = self.snake_blocks[block - 1].xcor()
            new_y = self.snake_blocks[block - 1].ycor()
            self.snake_blocks[block].goto(new_x, new_y)

        self.snake_blocks[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)