from point import Point


class Block:
    def __init__(self, row, col):
        self.location = Point(row, col)
    
    def setPosition(self, row, col):
        self.location.setRow(row)
        self.location.setCol(col)
