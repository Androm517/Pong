from unittest import TestCase
from source.game import Ball

class TestBall(TestCase):
    def test_move(self):
        b = Ball()
        b.move(1)
        assert b.position[0] == 1 and b.position[1] == 1

