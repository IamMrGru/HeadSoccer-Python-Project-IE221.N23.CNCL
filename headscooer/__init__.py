import pygame
import pymunk
from pymunk.vec2d import Vec2d
import random
import os

pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((1920,1000))
pygame.display.set_caption("Head Soccer")
clock=pygame.time.Clock()
space=pymunk.Space()
space.gravity=(0,-1000)
FPS=64
size=(1920,1000)
running=True
font = pygame.font.Font(None, 50)

collision_type_0=0
collision_type_1=1
collision_type_2=2
collision_type_3=3











