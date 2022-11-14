import pygame
from sys import exit
from maze import Maze
from pacman import PacMan

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((550, 550))
        self.maze = Maze(self.window)
        self.p = PacMan(1, 1, self.maze, self.window)
        self.p2 = PacMan(1, 9, self.maze, self.window)

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    
    def draw(self):
        self.maze.draw()
        self.p.draw()
        self.p2.draw()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(100)
            self.checkEvents()
            self.window.fill((0, 0, 0))
            if self.p.getScore() + self.p2.getScore() == 55:
                self.p.reset(1, 1)
                self.p2.reset(1, 9)
                self.maze.resetMaze()
            self.p.move()
            self.p2.move()
            self.draw()
            pygame.display.update()

if __name__ == '__main__':
    g = Game()
    g.run()
