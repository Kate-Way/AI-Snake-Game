from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.new_turtles = []
        # create all moving pieces of snake
        self.create_snake()
        self.head = self.new_turtles[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(shape='square')
        new_turtle.color('black')
        new_turtle.penup()
        new_turtle.goto(position)
        # new_turtle.direction = "Stop"
        self.new_turtles.append(new_turtle)

    def extend(self):
        """Add a new segment to the snake at the last segment of the list."""
        # .position() is a Turtle class method
        self.add_segment(self.new_turtles[-1].position())


    def move(self):
        # move snake starting from the last piece heading towards the head
        # start at the position of the last piece (len-1), move to start position 0, with step -1
        for turt_num in range(len(self.new_turtles) - 1, 0, -1):
            new_x = self.new_turtles[turt_num - 1].xcor()
            new_y = self.new_turtles[turt_num - 1].ycor()
            self.new_turtles[turt_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        # to make dead snake disappear send it far off the screen
        for turt in self.new_turtles:
            turt.goto(1000, 1000)
        self.new_turtles.clear()
        self.create_snake()
        self.head = self.new_turtles[0]

    def move_up(self):
        # if already goes down can't go up
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)


