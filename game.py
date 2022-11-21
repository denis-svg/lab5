import pygame
import datetime
from sys import exit
from statistics import mean
import matplotlib.pyplot as plt
from maze import Maze
from pacman import PacMan
from ghost import Ghost
from drawer import Drawer


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((550, 550))
        self.maze = Maze(self.window)
        self.ghosts = []
        self.players = []
        self.setEntities()
        self.scores = []
        self.times = []
        self.d = Drawer(self.window, self.maze)

    def setEntities(self):
        self.ghosts = [Ghost(5, 5, self.maze), Ghost(5, 6, self.maze), Ghost(5, 7, self.maze)]
        self.players = [PacMan(1, 9, self.maze), PacMan(9, 1, self.maze)]

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plt.plot([i + 5 for i in range(len(self.scores))], self.scores, label="Average score ---> " + str(mean(self.scores)))
                plt.legend()
                plt.show()
                plt.plot([i + 5 for i in range(len(self.times))], self.times, label="Average time ---> " + str(mean(self.times)))
                plt.legend()
                plt.show()
                exit()

    def draw(self):
        self.d.draw(self.players, self.ghosts)

    def checkDead(self):
        new_p = []
        for player in self.players:
            flag = True
            for ghost in self.ghosts:
                if player.getRow() == ghost.getRow() and player.getCol() == ghost.getCol():
                    player.health -= 1
                    if player.health == 0:
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

    def test(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(1)
            self.checkEvents()

            for player in self.players:
                player.moveRandom()
            self.d.draw(self.players, self.ghosts)

            self.checkDead()
            if len(self.players) == 0:
                self.setEntities()
                self.maze.resetMaze()
            self.d.draw(self.players, self.ghosts)
            
            if sum([player.getScore() for player in self.players]) == 55:
                self.d.draw(self.players, self.ghosts)
                self.setEntities()
                self.maze.resetMaze()
                continue

            for ghost in self.ghosts:
                ghost.moveRandom()
            self.checkDead()
            self.d.draw(self.players, self.ghosts)

            if len(self.players) == 0:
                self.setEntities()
                self.maze.resetMaze()

            self.d.draw(self.players, self.ghosts)

    def run(self):
        clock = pygame.time.Clock()
        start = datetime.datetime.now()
        while True:
            clock.tick(2)
            self.checkEvents()
            
            p_state = [(ghost.getRow(), ghost.getCol) for ghost in self.ghosts]

            for player in self.players:
                player.moveRandom()
                #player.moveRandom()

            self.draw()
            pygame.display.update()
            if sum([player.getScore() for player in self.players]) == 55:
                total  = (datetime.datetime.now() - start).total_seconds()
                start = datetime.datetime.now()
                self.times.append(total)
                self.scores.append(55)
                self.setEntities()
                self.maze.resetMaze()
                continue

            self.checkDead()
            if len(self.players) == 0:
                total  = (datetime.datetime.now() - start).total_seconds()
                start = datetime.datetime.now()
                self.times.append(total)
                self.scores.append(self.getEatenDots())
                self.setEntities()
                self.maze.resetMaze()
                continue

            if sum([player.getScore() for player in self.players]) == 55:
                total  = (datetime.datetime.now() - start).total_seconds()
                start = datetime.datetime.now()
                self.times.append(total)
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
                total  = (datetime.datetime.now() - start).total_seconds()
                start = datetime.datetime.now()
                self.times.append(total)
                self.scores.append(self.getEatenDots())
                self.setEntities()
                self.maze.resetMaze()
                continue
            sc = self.getEatenDots()
            if sc == 55:
                total  = (datetime.datetime.now() - start).total_seconds()
                start = datetime.datetime.now()
                self.times.append(total)
                self.scores.append(55)
                self.setEntities()
                self.maze.resetMaze()
                continue

if __name__ == '__main__':
    g = Game()
    g.test()
