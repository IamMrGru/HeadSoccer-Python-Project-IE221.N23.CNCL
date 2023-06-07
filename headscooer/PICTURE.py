import pygame
import pymunk
from pymunk.vec2d import Vec2d
import random
import os

# Hình
background=pygame.image.load('stadium2.jpg')
background=pygame.transform.scale(background,(1920,1000))
menubg=pygame.image.load('bong-da-dau-to-2023-640.jpg')
menubg=pygame.transform.scale(menubg,(1920,1000))
ballpic=pygame.image.load('ball.png')
ballpic=pygame.transform.scale(ballpic,(30*2.8,30*2.8))
pc1=pygame.image.load('hien.png')
pc1=pygame.transform.scale(pc1,(40*3.2,40*3.2))
pc2=pygame.image.load('ronaldo.png')
pc2=pygame.transform.scale(pc2,(40*3.2,40*3.2))
gl=pygame.image.load('goal_l.png')
gl=pygame.transform.scale(gl,(90,200))
gr=pygame.image.load('goal_r.png')
gr=pygame.transform.scale(gr,(90,200))