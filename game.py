import pygame
from sys import exit
from copy import deepcopy
from maze import Maze
from pacman import PacMan
from ghost import Ghost

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((550, 550))
        self.maze = Maze(self.window)
        self.ghosts = [Ghost(5, 5, self.maze, self.window), Ghost(5, 6, self.maze, self.window)]
        self.players = [PacMan(1, 1, self.maze, self.window), PacMan(1, 9, self.maze, self.window), PacMan(1, 2, self.maze, self.window)]

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(1000)
            self.checkEvents()
            self.window.fill((0, 0, 0))
            
            self.checkDead()

            if len(self.players) == 0:
                print('lose')
                self.players = [PacMan(1, 1, self.maze, self.window), PacMan(1, 9, self.maze, self.window)]
                self.ghosts = [Ghost(5, 5, self.maze, self.window), Ghost(5, 6, self.maze, self.window)]
                self.maze.resetMaze()

            if sum([player.getScore() for player in self.players]) == 55:
                print('win')
                self.players = [PacMan(1, 1, self.maze, self.window), PacMan(1, 9, self.maze, self.window)]
                self.ghosts = [Ghost(5, 5, self.maze, self.window), Ghost(5, 6, self.maze, self.window)]
                self.maze.resetMaze()

            for ghost in self.ghosts:
                ghost.move()

            for player in self.players:
                player.move(self.ghosts)

            self.draw()
            pygame.display.update()

if __name__ == '__main__':
    g = Game()
    g.run()
