import pygame

class BattingSystem:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, (220,220,220), (50,475,120,120))

class Bat:
    def __init__(self, screen, (70, 70), BatSystem.bat.png):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        self.screen = screen 
        self.x = x
        self.y = y 
        self.image = pygame.image.load(BatSystem.bat.png)



class Bat:
    def __init__(self, screen, x, y, BatSystem.bat.png ):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(BatSystem.bat.png)

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))