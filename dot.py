from block import Block

class Dot(Block):
    def __init__(self, row, col, images, window):
        super().__init__(row, col, images[0], window)
        # when the dot is eaten it will display image2
        self.is_eaten = False
        self.images = images

    def setEaten(self):
        self.is_eaten = True
        self.image = self.images[1]

    def isEaten(self):
        return self.is_eaten

    
    