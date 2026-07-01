import pygame
import sys
import batting_system
import random
import time
import sideprof
import scoreboard

def main():
    # turn on pygame
    pygame.init()
    pygame.mixer.init()

    bat_sound = pygame.mixer.Sound("sounds/bat_crack_wood.mp3")
    # TODO: change the normal volume for the bat crack sound!
    bat_sound_volume = 0.6
    bat_sound.set_volume(bat_sound_volume)

    pygame.mixer.music.load("sounds/ballpark_organ.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    # create a screen
    pygame.display.set_caption("Ballpark Blast")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1163, 750))
    # creates a Character from the my_character.py file
    bs = batting_system.BattingSystem(screen)
    sp = sideprof.SideProfile(screen)
    sb = scoreboard.Scoreboard(screen)
    did_batter_swing = False
    need_to_handle_score = False

    # let's set the framerate
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)  # this sets the framerate of your game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO: Add you events code
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE: 
                    print("Score", bs.get_bat_ball_distance())
                    bs.swing()
                    did_batter_swing = True
                    need_to_handle_score = True
            

                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_UP]:
                    if not sb.is_round_over():
                        sp.pitcher.image_to_show = 2
                        sp.batter.image_to_show = 1
                        did_batter_swing = False
                        need_to_handle_score = False

                # typing a batter name works any time, using any letter key
                if pygame.K_a <= event.key <= pygame.K_z:
                    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    letter = alphabet[event.key - pygame.K_a]
                    sb.add_letter(letter)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    if not sb.is_round_over():
                        sp.pitch()
                        bs.pitch()
                        # a pitch is now on its way and needs to be scored,
                        # even if the batter never swings (a no-swing is a 0)
                        need_to_handle_score = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if sb.restart_button.is_clicked_by(event.pos):
                    sb.restart_round()
                    sp.batter.image_to_show = 1

        if sp.is_ball_to_batter():
            if need_to_handle_score:
                distance = bs.get_bat_ball_distance()
                if did_batter_swing:
                    score = bs.get_score()
                    if score >= 97:
                        # !HOMERUN! - play the bat crack 1.6 times louder
                        bat_sound.set_volume(min(1.0, bat_sound_volume * 1.6))
                    else:
                        bat_sound.set_volume(bat_sound_volume)
                    bat_sound.play()
                    sb.record_pitch(score, distance)
                else:
                    sb.record_pitch(0, distance)
                sp.reset(did_batter_swing, sb.score)
                bs.show_score(sb.score)
                sb.show_hit_result(sb.score)
                need_to_handle_score = False
            bs.reset()

        screen.fill((255, 255, 255))

        # draws every frame
        bs.draw()
        sp.draw()
        sb.draw()

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()


main()
