import pygame
import random

class SideProfile:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.batter = Batter(screen, 110, 675)
        self.ball = ProfileBall(screen, 820, 600)
        self.pitcher = Pitcher(screen, 700, 700)
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
        #self.pitch.draw()
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
        self.screen.blit(self.image, (self.x - 8, self.y - 8)) 

    def move(self): 
        self.x -= self.speed


class Pitcher:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 4
        self.image = pygame.image.load("pitcher.png")

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))    
    