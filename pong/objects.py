import pyxel
import pong.config as config
import pong.properties as props
from pong.vectors import Vec2,Vec2norm

class Ball:
    """ The ball just has a position and velocity to tell it where to go """
    def __init__(self, px, py, vx, vy): 
        self.position = Vec2(px, py)
        self.velocity = Vec2norm(vx, vy)
    def update(self):
        """ update the position of the ball """
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

        # make sure the ball doesnt go outside the app window
        if self.position.y >= config.SCREEN_HEIGHT - config.BALL_SIZE: 
            self.velocity.y = -self.velocity.y
        if self.position.y <= config.BALL_SIZE:
            self.velocity.y = -self.velocity.y
        ##### Temporary code to allow bouncing off the sides #####
        # if self.position.x >= config.SCREEN_WIDTH - config.BALL_SIZE:
        #     self.velocity.x = -self.velocity.x
        # if self.position.x <= config.BALL_SIZE:
        #     self.velocity.x = -self.velocity.x
        ##### end of temporary code #####

class Bat:
    """ The bats to hit the ball around with """
    def __init__(self, px, py):
        self.position = Vec2(px, py)
        self.velocity = 0 # The bats only need to move on one axis and they are still when initialised
        self.hitBox = props.HitBox( # initialise the bat with a hitbox
            self.position.x - config.BAT_SIZE / 4, 
            self.position.y - config.BAT_SIZE, 
            self.position.x + config.BAT_SIZE / 4, 
            self.position.y + config.BAT_SIZE
        )
    def update(self):
        """ update the position of the bat """
        self.position.y += self.velocity

        # make sure that the hitbox updates every frame and moves with the drawing
        self.hitBox = props.HitBox(
            self.position.x - config.BAT_SIZE / 4, 
            self.position.y - config.BAT_SIZE, 
            self.position.x + config.BAT_SIZE / 4, 
            self.position.y + config.BAT_SIZE
        )

        if pyxel.btnp(pyxel.KEY_UP):
            self.velocity = -2 # move up
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.velocity = 2 # move down

        # make sure the bat doesnt go outside the app window
        if self.position.y - config.BAT_SIZE < 0:
            self.position.y = config.BAT_SIZE
            self.velocity = 0
        if self.position.y + config.BAT_SIZE > config.SCREEN_HEIGHT:
            self.position.y = config.SCREEN_HEIGHT - config.BAT_SIZE
            self.velocity = 0