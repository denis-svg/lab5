import pygame
from wall import Wall
from dot import Dot
from sys import exit
import json

pygame.init()
win = pygame.display.set_mode((550, 550))
wall_image = pygame.image.load('images/wall.png')
wall_image = pygame.transform.scale(wall_image, (50, 50))
dots = []
walls = []
dot_im = [pygame.transform.scale(pygame.image.load('images/coin.png'), (50, 50)), pygame.transform.scale(pygame.image.load('images/no_coin.png'), (50, 50))]

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            ds = {}
            for dot in dots:
                ds[str(dot.location.getRow()) + ";" + str(dot.location.getCol())] = True
            ws = {}
            for wall in walls:
                ws[str(wall.location.getRow()) + ";" + str(wall.location.getCol())] = True
            with open("dots.json", "w") as outfile:
                json.dump(ds, outfile)
            with open("walls.json", "w") as outfile:
                json.dump(ws, outfile)
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if event.button == 1:
                col = pos[0] // 50
                row = pos[1] // 50
                flag = False
                for wall in walls:
                    if wall.location.getRow() == row and wall.location.getCol() == col:
                        flag = True
                        break

                if not flag:
                    walls.append(Wall(row, col, wall_image, win))
                    print("added wall")
            if event.button == 3:
                col = pos[0] // 50
                row = pos[1] // 50
                flag = False
                for wall in dots:
                    if wall.location.getRow() == row and wall.location.getCol() == col:
                        flag = True
                        break

                if not flag:
                    dots.append(Dot(row, col, dot_im, win))
                    print("added dot")
            if event.button == 2:
                col = pos[0] // 50
                row = pos[1] // 50
                index = None
                for i in range(len(dots)):
                    if dots[i].location.getRow() == row and dots[i].location.getCol() == col:
                        index = i
                        break
                print(index)
                if index is not None:
                    win.fill((0, 0, 0))
                    dots.pop(i)
                else:
                    for i in range(len(walls)):
                        if walls[i].location.getRow() == row and walls[i].location.getCol() == col:
                            index = i
                            break
                    if index is not None:
                        win.fill((0, 0, 0))
                        walls.pop(i)
                

        for wall in walls:
            wall.draw()
        for dot in dots:
            dot.draw()
    pygame.display.update()