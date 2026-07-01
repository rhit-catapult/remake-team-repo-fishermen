import pygame
import button_module

class Scoreboard:

    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.total = 0

        self.pitches_per_round = 5
        self.pitch_count = 0

        # Hall of Fame: list of [score, name] entries, best rounds ever
        self.hall_of_fame = []
        # TODO: we're testing 7 to see how many names actually fit!
        self.hall_of_fame_size = 7

        self.current_name = "AAA"

        self.pitch_icon = pygame.image.load("Baseball.png")
        self.pitch_icon = pygame.transform.scale(self.pitch_icon, (22, 22))

        # how far off each pitch's swing was, one entry per pitch thrown this round
        self.pitch_distances = []
        self.crosshairs_icon = pygame.image.load("crosshairs.png")
        self.crosshairs_icon = pygame.transform.scale(self.crosshairs_icon, (16, 16))

        # centered above the batting box, which spans x=30-170, y=475-595
        self.restart_button = button_module.TextButton(
            screen, center_x=100, center_y=420, text="New Round",
            font_size=18, padding=10)

        self.total_font = pygame.font.SysFont("stencil", 32)
        self.score_font = pygame.font.SysFont("stencil", 15)
        self.hof_font = pygame.font.SysFont("stencil", 18)
        # names were too small at the regular score_font size, so triple it just for the Hall of Fame entries
        self.hof_entry_font = pygame.font.SysFont("stencil", 15 * 3)

        all_fonts = pygame.font.get_fonts()
        # print(sorted(all_fonts))

    def record_pitch(self, points, distance):
        self.score = points
        self.total += points
        self.pitch_count += 1
        self.pitch_distances.append(distance)
        if self.pitch_count >= self.pitches_per_round:
            self.hall_of_fame.append([self.total, self.current_name])
            self.hall_of_fame.sort(reverse=True)

    def is_round_over(self):
        return self.pitch_count >= self.pitches_per_round

    def restart_round(self):
        self.pitch_count = 0
        self.total = 0
        self.pitch_distances = []

    def add_letter(self, letter):
        self.current_name = (self.current_name + letter)[-3:]

    def draw(self):
        caption = self.total_font.render(f"Total: {self.total}", True, (0,0,0))
        self.screen.blit(caption, (100 - caption.get_width() // 2, 20))

        caption = self.score_font.render(f"score: {self.score}", True, (0,0,0))
        self.screen.blit(caption, (100 - caption.get_width() // 2, 50))

        caption = self.score_font.render("Pitch Counter:", True, (0,0,0))
        self.screen.blit(caption, (100 - caption.get_width() // 2, 70))

        # 5 baseballs evenly spaced in a line - filled in as pitches happen
        icon_size = 22
        icon_y = 145
        # TODO: change how far the crosshairs can travel above the baseball!
        max_crosshair_offset = 40
        for i in range(self.pitches_per_round):
            icon_center_x = 10 + 180 * (i + 0.5) / self.pitches_per_round
            icon_x = icon_center_x - icon_size // 2
            if i < self.pitch_count:
                self.screen.blit(self.pitch_icon, (icon_x, icon_y))

                # crosshairs sit above the baseball - farther away the bat missed
                # the ball, the higher up the crosshairs are, so you can see how
                # far off that pitch was, graphically, at a glance
                distance = self.pitch_distances[i]
                offset = min(distance, 140) / 140 * max_crosshair_offset
                crosshairs_x = icon_center_x - 8
                crosshairs_y = icon_y - offset - 16
                self.screen.blit(self.crosshairs_icon, (crosshairs_x, crosshairs_y))
            else:
                pygame.draw.circle(self.screen, (180, 180, 180), (int(icon_center_x), icon_y + icon_size // 2), icon_size // 2, 2)

        caption = self.score_font.render(f"Currently at Bat: {self.current_name}", True, (0,0,0))
        self.screen.blit(caption, (100 - caption.get_width() // 2, 175))

        # Hall of Fame panel, left side, top N highest scores first
        hof_panel_rect = pygame.Rect(10, 200, 180, 190)
        pygame.draw.rect(self.screen, (255, 250, 205), hof_panel_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), hof_panel_rect, 3)

        caption = self.hof_font.render("HALL OF FAME", True, (0,0,0))
        self.screen.blit(caption, (hof_panel_rect.centerx - caption.get_width() // 2, hof_panel_rect.y + 10))

        y = hof_panel_rect.y + 40
        for i, entry in enumerate(self.hall_of_fame[:self.hall_of_fame_size]):
            entry_score = entry[0]
            entry_name = entry[1]
            caption = self.hof_entry_font.render(f"{i + 1}. {entry_score}  {entry_name}", True, (0,0,0))
            self.screen.blit(caption, (hof_panel_rect.x + 10, y))
            y += caption.get_height() + 5

        # Restart Round button
        self.restart_button.draw()