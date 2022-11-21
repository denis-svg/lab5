from entity import Entity

class Mover:
    def __init__(self, row, col, maze) -> None:
        self.entity = Entity(row, col)
        self.maze = maze

    def isWall(self, pos):
        row = self.entity.location.getRow() + pos[0]
        col = self.entity.location.getCol() + pos[1]
        if self.maze.isWall(row, col):
            return True
        return False
    
    def isDot(self, pos):
        row = self.entity.location.getRow() + pos[0]
        col = self.entity.location.getCol() + pos[1]
        if self.maze.isDot(row, col):
            return True
        return False
    
    def setDotEaten(self, pos):
        row = self.entity.location.getRow() + pos[0]
        col = self.entity.location.getCol() + pos[1]
        self.maze.dots[str(row) + ";" + str(col)].setEaten()
    
    def isEaten(self, pos):
        row = self.entity.location.getRow() + pos[0]
        col = self.entity.location.getCol() + pos[1]
        return self.maze.dots[str(row) + ";" + str(col)].isEaten()
