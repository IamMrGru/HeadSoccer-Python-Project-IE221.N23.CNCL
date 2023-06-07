import pygame
import pymunk
from pymunk.vec2d import Vec2d
from .ENV import *
from .SOUNDEFFECT import *
from .PICTURE import *

class Ball:
    def __init__(self):
        self.mass = 0.3
        self.radius2 = 30
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius2,(0,0))
        self.ball = pymunk.Body(self.mass, self.moment)
        self.ball.position = (960,500)
        self.shape_ball = pymunk.Circle(self.ball, self.radius2)
        self.shape_ball.collision_type=1
        self.shape_ball.elasticity = 1  # Độ đàn hồi khi va chạm với các vật thể khác
        space.add(self.ball, self.shape_ball)
    def goal(self,p1,p2):
        pos=self.ball.position
        if(pos.x<60 and pos.y<167):
            net.play()
            goal.play()
            pygame.time.wait(2000)  # Wait for 2 seconds
            space.remove(self.ball, self.shape_ball)  # Remove the ball from the space
            self.ball.position = (960, 800)  # Reset the ball's position
            space.add(self.ball, self.shape_ball)  # Add the ball back to the space
            p2.score+=1
            siu.play()
        if(pos.x>1863 and pos.y<167):
            net.play()
            goal2.play()
            pygame.time.wait(2000)  # Wait for 2 seconds
            space.remove(self.ball, self.shape_ball)  # Remove the ball from the space
            self.ball.position = (960, 800)  # Reset the ball's position
            space.add(self.ball, self.shape_ball)  # Add the ball back to the space
            p1.score+=1
    def draw(self):
        pos=self.ball.position
        pygame.draw.circle(win,'Black',(int(pos.x),int(size[1]-pos.y)),self.radius2)
        ball_rect = ballpic.get_rect(center=(pos.x, 1000-pos.y))
        win.blit(ballpic, ball_rect)