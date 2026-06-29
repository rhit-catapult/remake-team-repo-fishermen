import pygame
import random

class SideProfile:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.batter = Batter(screen, 110, 675)
        self.ball = ProfileBall(screen, 110, 600)
        self.pitcher = Pitcher(screen, 700, 700)
        self.background = pygame.image.load("backround.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
    def draw(self):
        self.screen.blit(self.background, (200,0))
        # self.bat.move()
        # self.bat.draw()
        # self.ball.draw()
        # self.ball.move() 
    def get_bat_ball_distance(self):
        return abs(self.ball.x - self.bat.x)
    
class Batter:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 4
        self.image = pygame.image.load("BatSystem.bat.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
    def draw(self):
        self.screen.blit(self.image, (self.x - 100, self.y - 100))    
    def move(self):
        self.x += self.speed
        if self.x > (175):
            self.speed = -self.speed
        if self.x < (50):
            self.speed = -self.speed

class ProfileBall:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load("Baseball.png")
        # self.image = pygame.transform.scale(self.image, (200, 200))
    def draw(self):
        self.screen.blit(self.image, (self.x - 8, self.y - 8))    
    def move(self): 
        self.x = random.randint(58, 162)
        self.y = random.randint(483, 587)


class Pitcher:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 4
        self.image = pygame.image.load("BatSystem.bat.png")
        self.image = pygame.transform.scale(self.image, (200, 200))
    def draw(self):
        self.screen.blit(self.image, (self.x - 100, self.y - 100))    
    def move(self):
        self.x += self.speed
        if self.x > (175):
            self.speed = -self.speed
        if self.x < (50):
            self.speed = -self.speed