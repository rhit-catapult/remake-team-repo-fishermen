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

    # try changing these to 1, 2, or 3 to pick a different sound!
    use_backgroun_sound = 1
    use_bat_sound = 1

    if use_backgroun_sound == 1:
        pygame.mixer.music.load("sounds/crowd_ambience_loop.mp3")
    if use_backgroun_sound == 2:
        pygame.mixer.music.load("sounds/crowd_chant.mp3")
    if use_backgroun_sound == 3:
        pygame.mixer.music.load("sounds/crowd_roar.mp3")
    pygame.mixer.music.play(-1)

    if use_bat_sound == 1:
        bat_sound = pygame.mixer.Sound("sounds/bat_crack_wood.mp3")
    if use_bat_sound == 2:
        bat_sound = pygame.mixer.Sound("sounds/bat_crack_ball.mp3")
    if use_bat_sound == 3:
        bat_sound = pygame.mixer.Sound("sounds/bat_crack_punch.mp3")

    # create a screen
    pygame.display.set_caption("Cool Project")
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
                    bat_sound.play()
                    did_batter_swing = True
                    need_to_handle_score = True

                keys_pressed = pygame.key.get_pressed()
                if keys_pressed[pygame.K_p]:
                    sp.pitcher.image_to_show = 2
                    sp.batter.image_to_show = 1
                    did_batter_swing = False
                    need_to_handle_score = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    sp.pitch()
                    bs.pitch()

        if sp.is_ball_to_batter(): 
            if need_to_handle_score:
                sp.reset(did_batter_swing)
                sb.score += bs.get_score()
                need_to_handle_score = False
            bs.reset()

            # if event.type == pygame.QUIT:
            #     running=False
            #     #lambros added two lines above

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # draws the character every frame
        bs.draw()
        sp.draw()
        sb.draw()

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()
        


main()
