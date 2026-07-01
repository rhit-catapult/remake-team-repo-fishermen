import pygame
import random
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
        # self.hall_of_fame.append([500, "DSF"])
        # self.hall_of_fame.append([490, "DSF"])
        # self.hall_of_fame.append([480, "DSF"])
        # self.hall_of_fame.append([470, "DSF"])
        # self.hall_of_fame.append([460, "DSF"])


        # TODO: we're testing 7 to see how many names actually fit!
        self.hall_of_fame_size = 5

        self.current_name = "AAA"

        self.pitch_icon = pygame.image.load("Baseball.png")
        self.pitch_icon = pygame.transform.scale(self.pitch_icon, (22, 22))

        # one entry per pitch thrown this round
        self.pitch_distances = []
        self.pitch_scores = []

        self.crosshairs_icon = pygame.image.load("crosshairs.png")
        self.crosshairs_icon = pygame.transform.scale(self.crosshairs_icon, (32, 32))
        # gold crosshairs for homeruns, red for strikes - hits just use the normal icon
        self.crosshairs_homerun = self.crosshairs_icon.copy()
        self.crosshairs_homerun.fill((150, 150, 0), special_flags=pygame.BLEND_RGB_ADD)
        self.crosshairs_strike = self.crosshairs_icon.copy()
        self.crosshairs_strike.fill((200, 0, 0), special_flags=pygame.BLEND_RGB_ADD)

        # centered above the batting box, which spans x=30-170, y=475-595
        self.restart_button = button_module.TextButton(
            screen, center_x=100, center_y=430, text="New Round",
            font_size=18, padding=10)

        self.total_font = pygame.font.SysFont("stencil", 40)
        self.score_font = pygame.font.SysFont("stencil", 22)
        self.hof_font = pygame.font.SysFont("stencil", 18)
        # names were too small at the regular score_font size, so triple it just for the Hall of Fame entries
        self.hof_entry_font = pygame.font.SysFont("stencil", 13 * 3)

        self.hit_text = ""
        self.hit_text_frames = 0
        self.hit_text_font = pygame.font.SysFont("stencil", 90)
        # the !HOMERUN! text is twice the size of Hit!/STRIKE, and flashes rainbow colors
        self.homerun_text_font = pygame.font.SysFont("stencil", 90 * 2)

        all_fonts = pygame.font.get_fonts()
        # print(sorted(all_fonts))

    def record_pitch(self, points, distance):
        self.score = points
        self.total += points
        self.pitch_count += 1
        self.pitch_distances.append(distance)
        self.pitch_scores.append(points)
        if self.pitch_count >= self.pitches_per_round:
            self.hall_of_fame.append([self.total, self.current_name])
            self.hall_of_fame.sort(reverse=True)

    def is_round_over(self):
        return self.pitch_count >= self.pitches_per_round

    def restart_round(self):
        self.pitch_count = 0
        self.total = 0
        self.pitch_distances = []
        self.pitch_scores = []

    def add_letter(self, letter):
        self.current_name = (self.current_name + letter)[-3:]

    def show_hit_result(self, score):
        if score >= 92:
            self.hit_text = "!HOMERUN!"
            homerun_sound = pygame.mixer.Sound("sounds/batterhomerun.mp3")
            homerun_sound.set_volume(1.8)
            homerun_sound.play()

            
        elif score >= 52:
            
            self.hit_text = "Hit!"
            pygame.mixer.Sound("sounds/bat_crack_wood.mp3").play()
        else:
            self.hit_text = "STRIKE"
            pygame.mixer.Sound("sounds/battermisseffect.mp3").play()
        self.hit_text_frames = 90  # about 1.5 seconds at 60 frames per second

    def draw(self):
        caption = self.total_font.render(f"Total: {self.total}", True, (0,0,0))
        self.screen.blit(caption, (100 - caption.get_width() // 2, 20))

        caption = self.score_font.render(f"score: {self.score}", True, (0,0,0))
        self.screen.blit(caption, (100 - caption.get_width() // 2, 50))

        # caption = self.score_font.render("Pitch Counter:", True, (0,0,0))
        # self.screen.blit(caption, (100 - caption.get_width() // 2, 70))

        # 5 baseballs evenly spaced in a line - filled in as pitches happen
        icon_size = 22
        icon_y = 130
        # TODO: change how far the crosshairs sit from the ball for hits and strikes!
        closest_hit_offset = 8
        farthest_hit_offset = 40
        strike_offset = 45
        for i in range(self.pitches_per_round):
            icon_center_x = 10 + 180 * (i + 0.5) / self.pitches_per_round
            icon_x = icon_center_x - icon_size // 2
            if i < self.pitch_count:
                self.screen.blit(self.pitch_icon, (icon_x, icon_y))

                # crosshairs sit above the baseball - a homerun lands right on
                # the ball, a hit sits closer the higher the score, and a
                # strike sits the farthest away, so you can see how each
                # pitch went, graphically, at a glance
                score = self.pitch_scores[i]
                if score >= 97:
                    crosshairs_icon = self.crosshairs_homerun
                    offset = 0
                elif score >= 52:
                    crosshairs_icon = self.crosshairs_icon
                    offset = farthest_hit_offset - (score - 52) / (96 - 52) * (farthest_hit_offset - closest_hit_offset)
                else:
                    crosshairs_icon = self.crosshairs_strike
                    offset = strike_offset

                crosshairs_x = icon_center_x - 16
                crosshairs_y = icon_y - offset - 6
                self.screen.blit(crosshairs_icon, (crosshairs_x, crosshairs_y))
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

        y = hof_panel_rect.y + 30
        for i, entry in enumerate(self.hall_of_fame[:self.hall_of_fame_size]):
            entry_score = entry[0]
            entry_name = entry[1]
            caption = self.hof_entry_font.render(f"{i + 1}.  {entry_score}  {entry_name}", True, (0,0,0))
            self.screen.blit(caption, (hof_panel_rect.x + 15, y))
            y += caption.get_height() + 5

        # Restart Round button
        self.restart_button.draw()

        # drawn last so it always shows up on top of everything else
        if self.hit_text_frames > 0:
            self.hit_text_frames -= 1
            center_x = self.screen.get_width() // 2
            center_y = self.screen.get_height() // 2
            if self.hit_text == "!HOMERUN!":
                # alternating rainbow - a new random color every frame
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                caption = self.homerun_text_font.render(self.hit_text, True, (r, g, b))
            else:
                caption = self.hit_text_font.render(self.hit_text, True, (255, 0, 0))
            self.screen.blit(caption, (center_x - caption.get_width() // 2, center_y - caption.get_height() // 2))