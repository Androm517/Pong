import numpy as np


class Box:
    """
    Den här klassen innehåller attribut och metoder för att kunna flytta runt
    objekt på pong brädet. Alla objekt som ärver den här klassen kan flyttasrunt
    på pong brädet.
    """
    def __init__(self):
        self.position = np.array([0, 0])
        self.velocity = np.array([1, 1])
        self.dimensions = np.array([1, 1])

    def move(self, dt):
        self.position += self.velocity * dt


class Ball(Box):
    """
    Boll till pong brädet.
    """
    def __init__(self):
        super(Ball, self).__init__()


class Paddle(Box):
    """
    Paddel till pong brädet.
    """
    def __init__(self):
        super(Ball, self).__init__()


class PongBoard:
    """
    Pong brädet. Innehåller metoder för studsar av objekt på brädet och ser till
    att objekten håller sig på brädet.
    :attribut Objekt som ärver klassen Box:
    :metoder kolla om objekt studsar mot varandra eller åker utanför brädet:
    """
    pass