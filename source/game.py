import numpy as np


class Box:
    def __init__(self):
        self.position = np.array([0, 0])
        self.velocity = np.array([1, 1])
        self.dimensions = np.array([1, 1])

    def move(self, dt):
        self.position += self.velocity * dt

class Ball(Box):
    def __init__(self):
        super(Ball, self).__init__()


class Board:
    pass