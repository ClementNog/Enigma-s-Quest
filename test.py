import random
import pygame
import time

def genObstacle():
    # generate and return
    #1. pygame surface for top and bottom rects
    #2. initial position for top rect and bottom rect
    topHeight = random.randint(10, 200) # height for bottom obstacle
    botHeight = random.randint(10, 200) # height for top obstacle
    top = pygame.Surface((10, topHeight)).convert()
    bot = pygame.Surface((10, botHeight)).convert()
    # return: top rect, bottom rect, top rect's position, bottom rect's position

    return [top, bot, [800, 0], [800, 500-botHeight]]

pygame.init()

obstacles = []
start = time.time()
win = pygame.display.set_mode((1000, 500))
pygame.display.flip()
while True:
    #other code
    now = time.time()
    if now - start > 3:
        obstacles.append(genObstacle())
        start = now
    print(genObstacle())
    for i in range(len(obstacles)):
        # remember, third item in list is position for top and
        # fourth item is the position for bottom
        
        # draw the obstacles
        win.blit(obstacles[i][0], (obstacles[i][2][0], obstacles[i][3][1]))
        win.blit(obstacles[i][1], (obstacles[i][2][0], obstacles[i][3][1]))

        # change the x values for it to move to the right
        obstacles[i][2][0] -= 1
        obstacles[i][2][0] -= 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
