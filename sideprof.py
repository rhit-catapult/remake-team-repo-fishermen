import pygame
import random

class SideProfile:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.batter = Batter(screen, 110, 675)
        self.ball = ProfileBall(screen, 820, 600)
        self.pitcher = Pitcher(screen)
        self.background = pygame.image.load("backround.png")
        self.background = pygame.transform.scale(self.background, (1438 * 0.67, 1122 * 0.67))
        self.is_ball_moving = False


    def pitch(self):
        self.ball.x = 820
        self.ball.speed = 3
        self.is_ball_moving = True

    def reset(self):
        self.ball.speed = -10

    def draw(self):
        self.screen.blit(self.background, (200,0))
        if self.is_ball_moving:
            self.ball.move()
            if self.ball.x < 50:
                self.is_ball_moving = False
        self.ball.draw()
        
        # pygame.draw.line(self.screen, (128,0,0), (280,200), (280,1200), 5)
        self.pitcher.draw()

    def is_ball_to_batter(self):
        return self.ball.x < 280
    
class Batter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 4
        self.image = pygame.image.load("BatSystem.bat.png")

    def draw(self):
        self.screen.blit(self.image, (self.x - 100, self.y - 100))    

class ProfileBall:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("Baseball.png")
        self.speed = 3

    def draw(self):
        self.screen.blit(self.image, (self.x - 80, self.y - 50)) 

    def move(self): 
        self.x -= self.speed


class Pitcher:
    def __init__(self, screen):
        self.screen = screen
        self.speed = 4
        self.image_to_show = 3
        self.image1 = pygame.image.load("pitcherbeforethrow.png")
        self.image1 = pygame.transform.scale(self.image1, (200,266))
        self.image2 = pygame.image.load("pitchermidthrow.png")
        self.image2 = pygame.transform.scale(self.image2, (245,310))
        self.image3 = pygame.image.load("pitcherafterthrow.png")
        self.image3 = pygame.transform.scale(self.image3, (230,305))

    def draw(self):
        if self.image_to_show == 1:
            self.screen.blit(self.image1, (750, 490))    
        if self.image_to_show == 2:
            self.screen.blit(self.image2, (755, 455))    
        if self.image_to_show == 3:
            self.screen.blit(self.image3, (690, 440))    
    