import pygame
from client import Client
from protocols import Protocols
import map1
import random
import spritesheet
import time

class MathGame:
    def __init__(self, client):
        self.client = client 
        client.start()
        self.map = client.get_map()
        self.wall = client.get_wall()
        self.font = None
        self.input_box = pygame.Rect(100, 100, 400, 45)
        self.color_inactive = pygame.Color("lightskyblue3")
        self.color_active = pygame.Color("dodgerblue2")
        self.color = self.color_inactive
        # self.player = 
        # self.opponent = 

        self.text = False
        self.done = False
        self.logged_in = False
    
    def display_movement(self):
        sprite_sheet_image = pygame.image.load('TAP.png').convert_alpha()
        spritesheet = spritesheet.SpriteSheet(sprite_sheet_image)
        BACKGROUND = (243, 211, 124)
        animation_list=[]
        animation_step=9
        step_counter = 0
        for i in range(4):
            temp_anim_list=[]
            for a in range(animation_step):
                temp_anim_list.append(spritesheet.get_image(a, i, 63, 65, 1, BACKGROUND))
                step_counter +=1
            animation_list.append(temp_anim_list)
        return animation_list
    def create_player(self,screen):
        action = 0
        frame = 0
        x=25
        y=25
        animation_list=self.display_movement()
        player=screen.blit(animation_list[action][frame], (x, y))
        return player

    def handle_event(self, event):
        animation_list = self.display_movement()
        player = self.create_player
        current_time = time.time()
        xmouse = int(pygame.mouse.get_pos()[0] / 100) * 100
        ymouse = int(pygame.mouse.get_pos()[1] / 100) * 100
        xrect=[]
        yrect=[]
        animation_cooldown = 500
        for m in range(len(self.map)):
            for i in self.map[m]:
                xrect.append(i.location[0])
                yrect.append(i.location[1])
        if pygame.mouse.get_pressed()[0]:
            
            xdep=min((abs(xmouse-xi), xi) for xi in xrect)[1]
            ydep=min((abs(ymouse-xi), xi) for xi in yrect)[1]
            getmouse=[xdep+25,ydep+25] 
        if player.collidelist(self.wall_position) != -1:
            xwall = self.wall_position[player.collidelist(self.wall_position)][0]
            ywall = self.wall_position[player.collidelist(self.wall_position)][1]
            
        if xwall == xdep:
            getmouse=[x,y]
        elif ywall == ydep:
            getmouse=[x,y] 
        self.client.send(Protocols.Response.PLAYER, getmouse)
        self.client.send(Protocols.Request.CAN, self.text)
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.color = self.color_active
            else:
                self.color = self.color_inactive
        
        if event.type != pygame.KEYDOWN or self.color == self.color_inactive:
            return
        
        # if event.key == pygame.K_RETURN:
        #     if not self.logged_in:
        #         # self.client.send(Protocols.Request.NICKNAME, self.text)
        #         # self.client.nickname = self.text
        #         # self.logged_in = True
        #         # self.text = ""
        #     elif self.client.started:
        #         self.client.send(Protocols.Request.ANSWER, int(self.text))
        #         self.client.client_validate_answer(self.text)
        #         self.text = ""
        elif event.key == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            self.text += event.unicode
    



    def draw(self, screen):
        screen.fill((255, 255, 255))
        if not self.client.started:
            self.draw_waiting(screen)
        else:
            self.draw_game(screen)
        
        pygame.display.update()

    def draw_waiting(self, screen):
        text = 'Waiting for player'
        text_surface = self.font.render(text, 1, (0, 0, 0))
        screen.blit(text_surface, (screen.get_width()/2 - text_surface.get_width()/2, screen.get_height()/2 - text_surface.get_height()/2))
    
    # def draw_login(self, screen):
    #     prompt = 'Enter A Nickname'
    #     prompt_surface = self.font.render(prompt, 1, (0, 0, 0))
    #     screen.blit(prompt_surface, (100, 50))
    #     self.draw_input(screen)
    def draw_player(self, screen):
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
    def draw_input(self, screen, wall_position, player, animation_cooldown):
        current_time = time.time()
        xmouse = int(pygame.mouse.get_pos()[0] / 100) * 100
        ymouse = int(pygame.mouse.get_pos()[1] / 100) * 100
        xrect=[]
        yrect=[]
        for m in range(len(self.map)):
            for i in self.map[m]:
                xrect.append(i.location[0])
                yrect.append(i.location[1])
        if pygame.mouse.get_pressed()[0]:
            
            xdep=min((abs(xmouse-xi), xi) for xi in xrect)[1]
            ydep=min((abs(ymouse-xi), xi) for xi in yrect)[1]
            getmouse=[xdep+25,ydep+25] 
        if player.collidelist(wall_position) != -1:
            xwall = wall_position[player.collidelist(wall_position)][0]
            ywall = wall_position[player.collidelist(wall_position)][1]
            
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
        # pygame.draw.rect(screen, self.color, self.input_box, 2)
        # txt_surface = self.font.render(self.text, 1, self.color)
        # screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 5))
        # self.input_box.w = max(100, txt_surface.get_width()+10)
        pass
    
    def draw_game(self, screen):
        # question = self.client.get_current_question()
        # question_surface = self.font.render(f"#{self.client.current_question_index + 1}: {question} = ", 1, (0, 0, 0))
        # screen.blit(question_surface, (100, 50))
        # self.draw_input(screen)
        # self.draw_opponent_data(screen)
        wall_position=[]
        for b in range(len(self.map)):
            for c in range(len(self.map[b])):
                self.map[b][c] = self.map[b][c].get_object(c,b)
                for i in self.map[b][c].get_wall():
                        wall=pygame.Rect(i)
                        wall_position.append(wall)
                screen.blit(self.map[b][c].image, self.map[b][c].location)
        return

    def draw_opponent_data(self, screen):
        if not self.client.opponent_data:
            return


        # name_surface = self.font.render(f"Opponent: {self.client.opponent_data['name']}", 1, (0, 0, 0))
        # screen.blit(name_surface, (550, 50))

        # wins_surface = self.font.render(f"Wins: {self.client.opponent_data['wins']}", 1, (0, 0, 0))
        # screen.blit(wins_surface, (550, 100))

        # loss_surface = self.font.render(f"Losses: {self.client.opponent_data['losses']}", 1, (0, 0, 0))
        # screen.blit(loss_surface, (550, 150))

        # question_num = self.client.opponent_question_index + 1
        # question_surface = self.font.render(f"Question #{question_num}", 1, (0,0,0))
        # screen.blit(question_surface, (550, 200))
    
    def handle_end(self, screen):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            
            # if self.client.winner:
            #     text = f"{self.client.winner} has won the game!"
            # else:
            #     text = f"Opponent left the game..."
            
            # text_surface = self.font.render(text, 1, (0, 0, 0))
            # screen.blit(text_surface,(screen.get_width()/2 - text_surface.get_width()/2, screen.get_height()/2 - text_surface.get_height()/2))
            pygame.display.update()

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsans", 32)

        while not self.client.closed:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.client.close()
                    pygame.quit()
                else:
                    self.handle_event(event)
            
            self.draw(screen)
        
        self.handle_end(screen)
        pygame.quit()

if __name__ == "__main__":
    game = MathGame(Client())
    game.run()