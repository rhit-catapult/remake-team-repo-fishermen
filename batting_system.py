import pygame

class BattingSystem:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, (220,220,220), (50,475,120,120))

