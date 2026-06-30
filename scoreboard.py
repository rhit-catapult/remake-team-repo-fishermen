import pygame

class Scoreboard:

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.strikes = 0
        self.score_font = pygame.font.SysFont("arial", 28)
    
    def draw(self):
        caption = self.score_font.render(f"Score: {self.score}", True, (0,0,0))
        self.screen.blit(caption, (10, 10))

    