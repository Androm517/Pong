import numpy as np

class Ball:
    def __init__(self):
        self.position = np.array([0, 0])
        self.velocity = np.array([1, 1])
        self.radie = 1

    def move(self, dt):
        self.position += self.velocity * dt


class Board:
    pass