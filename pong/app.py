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
        self.score = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        """ Update the application every frame """
        self.ball.update() # call the ball's update method
        for bat in self.bats:
            bat.update()
            if (bat.hitBox.x1 < self.ball.position.x < bat.hitBox.x2
            and bat.hitBox.y1 < self.ball.position.y < bat.hitBox.y2):
                self.ball.velocity.x = -self.ball.velocity.x
                self.score += 1 # if the bat is hit, update the score
            # lose conditions
            if self.ball.position.x >= config.SCREEN_WIDTH - config.BALL_SIZE:
                self.score = 0
            if self.ball.position.x <= config.BALL_SIZE:
                self.score = 0
        if pyxel.btnp(pyxel.KEY_Q):
            """ If Q is pressed, quit the application """
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_R):
            """ Restart if R is pressed """
            self.ball.position.x = config.SCREEN_WIDTH / 2
            self.ball.position.y = 20
            self.score = 0
    def draw(self):
        """ Clear the screen and redraw objects """
        pyxel.cls(0) # 0 is black in the 16 colour pallete
        # below: draw the ball
        pyxel.circ(
            self.ball.position.x,   # x starting point
            self.ball.position.y,   # y starting point
            config.BALL_SIZE,       # size of the ball
            9                       # color of the ball
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
        pyxel.text(
            config.SCREEN_WIDTH / 2,   # x-position of the text
            config.SCREEN_HEIGHT / 12, # y position of the text
            str(self.score),    # displayed text as string
            7                   # text color
        )
        pyxel.text(
            config.SCREEN_WIDTH / 2,
            config.SCREEN_HEIGHT - 10,
            str("q = Quit, r = Restart"),
            7
        )