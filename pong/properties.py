class HitBox:
    """ Class used to draw hitboxes around objects """
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1 # x-coordinate of top left corner
        self.y1 = y1 # y-coordinate of top left corner
        self.x2 = x2 # x-coordinate of bottom right corner
        self.y2 = y2 # y-coordinate of bottom right corner