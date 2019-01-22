import pong.config as config
import math

class Vec2:
    """ 2D positioning on the window x and y axis """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vec2norm:
    """ A normalized version of the vector class to allow us to change the ball speed """
    def __init__(self, x, y):
        self.magnitude = math.sqrt(x * x + y * y) # this is how you get the magnitude (length) of a vector
        self.x = x / self.magnitude * config.BALL_SPEED
        self.y = y / self.magnitude * config.BALL_SPEED