from mover import Mover
from random import choice
import pygame


class PacMan(Mover):
    def __init__(self, row, col, maze, window) -> None:
        super().__init__(row, col, pygame.transform.scale(pygame.image.load('images/right.png'), (50, 50)), maze, window)
        self.score = 0
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.available = []
        self.dir = None

    def getDir(self):
        d = {}
        pos = choice(self.directions)
        d[str(pos)] = True
        while self.isWall(pos) and len(d) < 4:
            pos = choice(self.directions)
            d[str(pos)] =  True
        return pos
    
    def getAllDirs(self):
        dirs = []
        for dir in self.directions:
            if self.isWall(dir):
                continue
            dirs.append(dir)
        return dirs

    def move(self):
        if dir is None:
            self.dir = self.getDir()
            self.available = self.getAllDirs()
        else:
            av = self.getAllDirs()
            if self.dir not in av:
                self.dir = choice(av)
            if len(av) > len(self.available):
                new_dir = choice(av)
                while new_dir[0] == self.dir[0] or new_dir[1] == self.dir[1]:
                    if new_dir[0] == self.dir[0] and new_dir[1] == self.dir[1]:
                        break
                    new_dir = choice(av)

                self.dir = new_dir
            self.available = av
        if self.isDot(self.dir) and not self.isEaten(self.dir):
            self.score += 1
            self.setDotEaten(self.dir)
        self.entity.move(self.dir)

    def win(self):
        return self.score == 55
    
    def reset(self, row, col):
        self.score = 0
        self.available = []
        self.dir = None
        self.entity.setPosition(row, col)


    def draw(self):
        self.entity.draw()