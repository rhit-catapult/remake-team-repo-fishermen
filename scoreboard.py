import pygame

class Scoreboard:

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.strikes = 0
        self.score_font = pygame.font.SysFont("comicsansms", 32)

        all_fonts = pygame.font.get_fonts()
        print(sorted(all_fonts))
    
    def draw(self):
        caption = self.score_font.render(f"Score: {self.score}", True, (0,0,0))
        self.screen.blit(caption, (100 - caption.get_width() // 2, 20))

    