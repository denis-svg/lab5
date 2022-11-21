import pygame


class Drawer:
    def __init__(self, window, maze) -> None:
        self.window = window
        self.coin_image = [pygame.transform.scale(pygame.image.load('images/coin.png'), (50, 50)), 
                                                pygame.transform.scale(pygame.image.load('images/no_coin.png'), (50, 50))]
        self.wall_image = pygame.transform.scale(pygame.image.load('images/wall.png'), (50, 50))
        self.pacman_image = pygame.transform.scale(pygame.image.load('images/right.png'), (50, 50))
        self.ghost_image = pygame.transform.scale(pygame.image.load('images/ghost.png'), (50, 50))
        
        self.maze = maze

    def drawMaze(self):
        self.window.fill((0, 0, 0))
        for key in self.maze.dots.keys():
            if self.maze.dots[key].isEaten():
                self.window.blit(self.coin_image[1], (self.maze.dots[key].location.getCol() * 50, self.maze.dots[key].location.getRow() * 50) )
            else:
                self.window.blit(self.coin_image[0], (self.maze.dots[key].location.getCol() * 50, self.maze.dots[key].location.getRow() * 50) )
        for key in self.maze.walls.keys():
            self.window.blit(self.wall_image, (self.maze.walls[key].location.getCol() * 50, self.maze.walls[key].location.getRow() * 50) )

    def drawEntities(self, pacmans, ghosts):
        for pacman in pacmans:
            self.window.blit(self.pacman_image, (pacman.entity.location.getCol() * 50, pacman.entity.location.getRow() * 50) )

        for ghost in ghosts:
            self.window.blit(self.ghost_image, (ghost.entity.location.getCol() * 50, ghost.entity.location.getRow() * 50))
    
    def draw(self, pacmans, ghosts):
        self.drawMaze()
        self.drawEntities(pacmans, ghosts)
        pygame.display.update()





        