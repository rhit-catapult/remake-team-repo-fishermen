import pygame
import random

class BattingSystem:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.bat = Bat(screen, 110, 675)
        self.ball = Ball(screen, 110, 600)
    def draw(self):
        pygame.draw.rect(self.screen, (220,220,220), (50,475,120,120))
        self.bat.move()
        self.bat.draw()
        self.ball.draw()
        # self.ball.move() 
    def get_bat_ball_distance(self):
        return abs(self.ball.x - self.bat.x)
class Bat:
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

class Ball:
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