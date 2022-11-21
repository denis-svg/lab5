import pygame
import json
from wall import Wall
from dot import Dot


class Maze:
    def __init__(self, window) -> None:
        self.window = window
        self.walls = {}
        self.dots = {}
        self.resetMaze()
    
    def resetMaze(self):
        dots_loc = {}
        walls_loc = {}
        self.walls = {}
        self.dots = {}

        f = open('dots.json')
        dots_loc = json.load(f)
        f.close()

        f = open('walls.json')
        walls_loc = json.load(f)
        f.close()
        i = 0
        for key in dots_loc.keys():
            if key not in self.dots:
                row, col = key.split(";")
                i += 1
                self.dots[key] = Dot(int(row), int(col))
        
        for key in walls_loc.keys():
            if key not in self.walls:
                row, col = key.split(";")
                i += 1
                self.walls[key] = Wall(int(row), int(col))

    def isWall(self, row, col):
        key = str(row) + ';' + str(col)
        if key in self.walls:
            return True
        return False

    def isDot(self, row, col):
        key = str(row) + ';' + str(col)
        if key in self.dots:
            return True
        return False



        