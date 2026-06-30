import pygame
import random

class BattingSystem:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.bat = Bat(screen, 110, 675)
        self.ball = Ball(screen, 110, 600)
        
    def draw(self):
        pygame.draw.rect(self.screen, (220,220,220), (30,475,140,120))
        self.bat.move()
        self.bat.draw()
        self.ball.draw()
    
    def pitch(self):
        self.ball.move()
        self.ball.is_visible = True
        self.bat.is_moving = True
    
    def swing(self):
        self.bat.is_moving = False

    def reset(self):
        self.ball.is_visible = False
        self.bat.is_moving = False
    
    def get_bat_ball_distance(self):
        if self.bat.is_moving:
            return 100
        return abs(self.ball.x - self.bat.x)

class Bat:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 5
        self.is_moving = False
        self.image = pygame.image.load("BatSystem.bat.png")
        self.image = pygame.transform.scale(self.image, (200, 200))

    def draw(self):
        self.screen.blit(self.image, (self.x - 100, self.y - 100))    

    def move(self):
        if self.is_moving:
            self.x += self.speed
            if self.x > 170:
                self.speed = -self.speed
            if self.x < 30:
                self.speed = -self.speed

class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.is_visible = False
        self.image = pygame.image.load("Baseball.png")
        # self.image = pygame.transform.scale(self.image, (200, 200))

    def draw(self):
        if self.is_visible:
            self.screen.blit(self.image, (self.x - 8, self.y - 8))    

    def move(self): 
        self.x = random.randint(34, 166)
        self.y = random.randint(479, 591)
