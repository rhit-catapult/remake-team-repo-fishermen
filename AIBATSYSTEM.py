import pygame


class BattingSystem:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, (220, 220, 220), (50, 475, 120, 120))


class Bat:
    def __init__(self, screen, x=70, y=70):
        """Creates a bat sprite."""
        self.screen = screen
        self.x = x
        self.y = y

        # Load the image
        self.image = pygame.image.load("BatSystem.bat.png").convert_alpha()

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))