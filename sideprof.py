import pygame
import random

class SideProfile:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.batter = Batter(screen)
        self.ball = ProfileBall(screen, 820, 600)
        self.pitcher = Pitcher(screen)
        self.background = pygame.image.load("backround.png")
        self.background = pygame.transform.scale(self.background, (1438 * 0.67, 1122 * 0.67))
        self.is_ball_moving = False


    def pitch(self):
        self.pitcher.image_to_show = 3
        self.ball.x = 820
        self.ball.y = self.ball.start_y
        self.ball.speed = 4
        self.ball.vertical_speed = 0
        self.ball.is_visible = True
        self.is_ball_moving = True

    def reset(self, did_batter_swing, score):
        if did_batter_swing:
            self.batter.image_to_show = 2
            self.ball.speed = -10
            if score <= 51:
                # a really low score is a strike - the ball just disappears
                self.ball.is_visible = False
            elif score >= 92:
                # !HOMERUN! - send it to the highest point
                self.ball.vertical_speed = 6
                self.ball.speed = -6
            else:
                # mid range hit - the higher the score, the higher it goes
                # TODO: change how high mid range hits go!
                self.ball.vertical_speed = 1 + (score - 52) / (96 - 52) * 4
        else:
            pass
        self.pitcher.image_to_show = 1

    def draw(self):
        self.screen.blit(self.background, (200,0))
        if self.is_ball_moving:
            self.ball.move()
            if self.ball.x < 50:
                self.is_ball_moving = False
        self.ball.draw()
        
        # pygame.draw.line(self.screen, (128,0,0), (280,200), (280,1200), 5)
        self.pitcher.draw()
        self.batter.draw()

    def is_ball_to_batter(self):
        return self.ball.x < 400
    
class Batter:
    def __init__(self, screen):
        self.screen = screen
    
        self.image_to_show = 1
        self.image1 = pygame.image.load("newbatterbeforeswing.png")
        self.image1 = pygame.transform.scale(self.image1, (200,266))
        self.image1 = pygame.transform.flip(self.image1, True, False)
        self.image2 = pygame.image.load("newbatterafterswing.png")
        self.image2 = pygame.transform.scale(self.image2, (200,266))
        self.image2 = pygame.transform.flip(self.image2, True, False)
    def draw(self):
        if self.image_to_show == 1:
            self.screen.blit(self.image1, (180, 490))    
        if self.image_to_show == 2:
            self.screen.blit(self.image2, (210, 490))  
      
class ProfileBall:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.start_y = y
        self.image = pygame.image.load("Baseball.png")
        self.speed = 3
        self.vertical_speed = 0
        self.is_visible = True

    def draw(self):
        if self.x > 280 and self.is_visible:
            self.screen.blit(self.image, (self.x - 80, self.y - 50))

    def move(self):
        self.x -= self.speed
        self.y -= self.vertical_speed


class Pitcher:
    def __init__(self, screen):
        self.screen = screen
        self.image_to_show = 1
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
    