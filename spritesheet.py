import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, line, width, height, scale, colour):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width),(line * height), width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey((colour))

        return image
    def get_wall(self, frame, line, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet,(0,0),((frame * width), (line * height), width,height))
        return image