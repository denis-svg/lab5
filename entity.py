from block import Block

class Entity(Block):
    def __init__(self, row, col):
        super().__init__(row, col)
    
    def move(self, pos):
        self.location.setRow(self.location.getRow() + pos[0])
        self.location.setCol(self.location.getCol() + pos[1])
