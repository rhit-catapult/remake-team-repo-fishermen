import pygame

class Scoreboard:

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.total = 0
        self.strikes = 0
        self.total_font = pygame.font.SysFont("stencil", 32)
        self.score_font = pygame.font.SysFont("stencil", 15)

        all_fonts = pygame.font.get_fonts()
        print(sorted(all_fonts))
    
    def draw(self):
        caption = self.total_font.render(f"Total: {self.total}", True, (0,0,0))
        self.screen.blit(caption, (100 - caption.get_width() // 2, 20))

        caption = self.score_font.render(f"score: {self.score}", True, (0,0,0))
        self.screen.blit(caption, (100 - caption.get_width() // 2, 50))