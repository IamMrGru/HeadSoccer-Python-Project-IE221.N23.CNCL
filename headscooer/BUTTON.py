import pygame
import pymunk
from pymunk.vec2d import Vec2d
import random
import os


play_button = pygame.Rect(300, 200, 200, 100)
quit_button = pygame.Rect(300, 500, 200, 100)
play_button2 = pygame.Rect(300, 350, 200, 100)
resume_button =pygame.Rect(300, 200, 200, 100)
menu_button= pygame.Rect(300, 350, 200, 100)
pause_button= pygame.Rect(180, 0, 130, 100)
winner=''