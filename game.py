import pygame
from sys import exit
from statistics import mean
import matplotlib.pyplot as plt
from maze import Maze
from pacman import PacMan
from ghost import Ghost


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((550, 550))
        self.maze = Maze(self.window)
        self.ghosts = []
        self.players = []
        self.setEntities()
        self.scores = []

    def setEntities(self):
        self.ghosts = [Ghost(5, 5, self.maze, self.window), ]#Ghost(5, 6, self.maze, self.window)]
        self.players = [PacMan(1, 1, self.maze, self.window), PacMan(1, 9, self.maze, self.window), PacMan(9, 1, self.maze, self.window)]

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plt.plot([i + 5 for i in range(len(self.scores))], self.scores, label="Average score ---> " + str(mean(self.scores)))
                plt.legend()
                plt.show()
                exit()
    
    def draw(self):
        self.maze.draw()
        for player in self.players:
            player.draw()
        for ghost in self.ghosts:
            ghost.draw()

    def checkDead(self):
        new_p = []
        for player in self.players:
            flag = True
            for ghost in self.ghosts:
                if player.getRow() == ghost.getRow() and player.getCol() == ghost.getCol():
                    flag = False
                    break
            if flag:
                new_p.append(player)
        self.players = new_p

    def getEatenDots(self):
        i = 0
        for key in self.maze.dots.keys():
            if self.maze.dots[key].isEaten():
                i += 1
        return i

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(0)
            self.checkEvents()
            self.window.fill((0, 0, 0))
            
            p_state = [(ghost.getRow(), ghost.getCol) for ghost in self.ghosts]

            for player in self.players:
                player.moveSmart(p_state)
                # player.moveRandom()
                
            self.draw()
            pygame.display.update()
            if sum([player.getScore() for player in self.players]) == 55:
                self.scores.append(55)
                self.setEntities()
                self.maze.resetMaze()
                continue

            self.checkDead()
            if len(self.players) == 0:
                self.scores.append(self.getEatenDots())
                self.setEntities()
                self.maze.resetMaze()
                continue

            if sum([player.getScore() for player in self.players]) == 55:
                self.scores.append(55)
                self.setEntities()
                self.maze.resetMaze()
                continue

            for ghost in self.ghosts:
                ghost.moveRandom()

            self.draw()
            pygame.display.update()
            self.checkDead()
            if len(self.players) == 0:
                self.scores.append(self.getEatenDots())
                self.setEntities()
                self.maze.resetMaze()
                continue
            sc = self.getEatenDots()
            if sc == 55:
                self.scores.append(55)
                self.setEntities()
                self.maze.resetMaze()
                continue

if __name__ == '__main__':
    g = Game()
    g.run()
