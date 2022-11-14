from point import Point


class Block:
    def __init__(self, row, col, image, window):
        self.window = window
        self.image = image
        self.location = Point(row, col)
    
    def draw(self):
        self.window.blit(self.image, (self.location.getCol() * 50, self.location.getRow() * 50) )

    def setPosition(self, row, col):
        self.location.setRow(row)
        self.location.setCol(col)
