import pygame
import sys


class TextButton:
    def __init__(self, screen, center_x, center_y, text, text_color=(255, 255, 255), background_color=(67, 177, 230),
                 border_color=(255, 255, 255), padding=20, font_name="menlo", font_size=24):
        self.screen = screen
        font = pygame.font.SysFont(font_name, font_size)
        self.caption = font.render(text.upper(), True, text_color, background_color)
        self.caption_x = center_x - self.caption.get_width() / 2
        self.caption_y = center_y - self.caption.get_height() / 2
        self.padding = padding
        self.bound_left_x = self.caption_x - self.padding
        self.bound_right_x = self.caption_x + self.caption.get_width() + self.padding
        self.bound_top_y = self.caption_y - self.padding
        self.bound_bottom_y = self.caption_y + self.caption.get_height() + self.padding
        self.background_color = background_color
        self.border_color = border_color

    def is_clicked_by(self, pos):
        pos_x = pos[0]
        pos_y = pos[1]
        return (self.bound_left_x < pos_x < self.bound_right_x and
                self.bound_top_y < pos_y < self.bound_bottom_y)  # Chained comparisons are only a Python thing.

    def draw(self):
        # API --> pygame.draw.rect(screen, (r,g,b), (x, y, width, height), thickness)
        width = self.bound_right_x - self.bound_left_x
        height = self.bound_bottom_y - self.bound_top_y
        pygame.draw.rect(self.screen, self.background_color, (self.bound_left_x, self.bound_top_y, width, height))
        pygame.draw.rect(self.screen, self.border_color, (self.bound_left_x, self.bound_top_y, width, height), 4)

        self.screen.blit(self.caption, (self.caption_x, self.caption_y))
