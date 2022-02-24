from segment import Segment
import math

MOVE_DISTANCE = 20                       # Do not change!
RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270  # Do not change!
X_BORDER = 350                           # Do not change!
Y_BORDER = 250                           # Do not change!
STARTING_SIZE = 3                        # Changeable


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.heading = 0

    def create_snake(self):
        for i in range(STARTING_SIZE):
            segment = Segment()
            segment.setx(-i * MOVE_DISTANCE)
            self.segments.append(segment)

    def move(self):
        for i, segment in enumerate(self.segments[::-1][:-1]):
            segment.goto(self.segments[::-1][i+1].pos())
        if not self.is_opposite_direction():
            self.head.setheading(self.heading)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        self.heading = RIGHT

    def up(self):
        self.heading = UP

    def left(self):
        self.heading = LEFT

    def down(self):
        self.heading = DOWN

    def add_new_segment(self):
        segment = Segment()
        segment.goto(self.segments[-1].pos())
        self.segments.append(segment)

    def is_colliding(self):
        is_in_x_range = -X_BORDER < self.head.xcor() < X_BORDER
        is_in_y_range = -Y_BORDER < self.head.ycor() < Y_BORDER
        if not(is_in_x_range and is_in_y_range):
            return True
        if any(self.head.distance(segment) < 1 for segment in self.segments[::-1][:-1]):
            return True
        return False

    def is_opposite_direction(self):
        return math.fabs(self.heading - self.head.heading()) == 180
