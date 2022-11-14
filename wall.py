from block import Block

class Wall(Block):
    def __init__(self, row, col, image, window):
        super().__init__(row, col, image, window)