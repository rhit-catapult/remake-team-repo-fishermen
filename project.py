import pygame
import sys
import batting_system
import random
import time
import sideprof


def main():
    # turn on pygame
    pygame.init()

    # create a screen
    pygame.display.set_caption("Cool Project")
    # TODO: Change the size of the screen as you see fit!
    screen = pygame.display.set_mode((1163, 750))
    # creates a Character from the my_character.py file
    bs = batting_system.BattingSystem(screen)
    sp = sideprof.SideProfile(screen)

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

        # TODO: Fill the screen with whatever background color you like!
        screen.fill((255, 255, 255))

        # draws the character every frame
        bs.draw()
        sp.draw()
        # TODO: Add your project code

        # don't forget the update, otherwise nothing will show up!
        pygame.display.update()
        


main()
