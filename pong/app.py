import pyxel
import pong.config as config
import pong.objects as objects

class App:
    """ Main application class, defines the window and draws objects """
    def __init__(self):
        """ Initialise the window and run the update and draw methods """
        pyxel.init(config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
        self.ball = objects.Ball(20, 20, 2, 2) # initialise the ball instance
        self.bats = [objects.Bat(10, 10), objects.Bat(config.SCREEN_WIDTH - 10, 10)] # initialise two bats 
        pyxel.run(self.update, self.draw)

    def update(self):
        """ Update the application every frame """
        self.ball.update() # call the ball's update method
        for bat in self.bats:
            bat.update()
            if (bat.hitBox.x1 < self.ball.position.x < bat.hitBox.x2
            and bat.hitBox.y1 < self.ball.position.y < bat.hitBox.y2):
                self.ball.velocity.x = -self.ball.velocity.x
        if pyxel.btnp(pyxel.KEY_Q):
            """ If Q is pressed, quit the application """
            pyxel.quit()
    def draw(self):
        """ Clear the screen and redraw objects """
        pyxel.cls(0) # 0 is black in the 16 colour pallete
        # below: draw the ball, 2 is the radius and 7 is the colour
        pyxel.circ(
            self.ball.position.x, # x starting point
            self.ball.position.y, # y starting point
            config.BALL_SIZE, # size of the ball
            9 # color of the ball
        )
        # below: draw the bats
        for bat in self.bats:
            pyxel.rect(
                bat.hitBox.x1,
                bat.hitBox.y1,
                bat.hitBox.x2,
                bat.hitBox.y2,
                12
            )