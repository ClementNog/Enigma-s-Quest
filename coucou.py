import pygame
import spritesheet
import random
import time
import map1

pygame.init()


DEFAULT_SCREENSIZE = [700, 700] #16 X 14 grid with 32px X 32px cell

screen = pygame.display.set_mode(DEFAULT_SCREENSIZE)
pygame.display.set_caption("test")

sprite_sheet_image = pygame.image.load('TAP.png').convert_alpha()
spritesheet = spritesheet.SpriteSheet(sprite_sheet_image)
BACKGROUND = (243, 211, 124)
animation_list=[]
animation_step=9
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0
step_counter = 0
for i in range(4):
    temp_anim_list=[]
    for a in range(animation_step):
        temp_anim_list.append(spritesheet.get_image(a, i, 63, 65, 1, BACKGROUND))
        step_counter +=1
    animation_list.append(temp_anim_list)
MAP=map1.init_map()


run = True
x=25
y=25
lastkey=[0,1]    
updated = False
going = True
getmouse=[25,25]
wall_position=[]

while run:
    now=time.time()
    screen.fill(BACKGROUND)
    current_time = pygame.time.get_ticks()
    
    for b in range(len(MAP)):
        for c in range(len(MAP[b])):
            MAP[b][c] = MAP[b][c].get_object(c,b)
            for i in MAP[b][c].get_wall():
                    wall=pygame.Rect(i)
                    wall_position.append(wall)
            screen.blit(MAP[b][c].image, MAP[b][c].location)


            

    move_ticker = 0
    a=screen.blit(animation_list[action][frame], (x, y))



    xmouse = int(pygame.mouse.get_pos()[0] / 100) * 100
    ymouse = int(pygame.mouse.get_pos()[1] / 100) * 100
    xrect=[]
    yrect=[]
    for m in range(len(MAP)):
        for i in MAP[m]:
            xrect.append(i.location[0])
            yrect.append(i.location[1])
    if pygame.mouse.get_pressed()[0]:
        
        xdep=min((abs(xmouse-xi), xi) for xi in xrect)[1]
        ydep=min((abs(ymouse-xi), xi) for xi in yrect)[1]
        getmouse=[xdep+25,ydep+25] 
    if a.collidelist(wall_position) != -1:
        xwall = wall_position[a.collidelist(wall_position)][0]
        ywall = wall_position[a.collidelist(wall_position)][1]
        
        if xwall == xdep:
            getmouse=[x,y]
        elif ywall == ydep:
            getmouse=[x,y] 
    if x < getmouse[0]:
        x+=0.5
        if current_time - last_update >= animation_cooldown:
            frame+=1
            last_update=current_time
            if frame>=len(animation_list[action]):
                frame=0
        action = 3
        if move_ticker == 0:   
            move_ticker = 5
    if x > getmouse[0]:
        x-=0.5
        if current_time - last_update >= animation_cooldown:
            frame+=1
            last_update=current_time
            if frame>=len(animation_list[action]):
                frame=0
        action = 1
        if move_ticker == 0:   
            move_ticker = 5
    if x == getmouse[0]:
        if y < getmouse[1]:
            y+=0.5
            if current_time - last_update >= animation_cooldown:
                frame+=1
                last_update=current_time
                if frame>=len(animation_list[action]):
                    frame=0
            action = 2
            if move_ticker == 0:   
                move_ticker = 5
        if y > getmouse[1]:
            y-=0.5
            if current_time - last_update >= animation_cooldown:
                frame+=1
                last_update=current_time
                if frame>=len(animation_list[action]):
                    frame=0
            action = 0
            if move_ticker == 0:   
                move_ticker = 5
        if y == getmouse[1]:
            frame = 0

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run = False
            going = False

    pygame.display.update()
pygame.quit()
