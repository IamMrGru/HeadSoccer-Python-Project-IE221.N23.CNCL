"""
Tên module: SOUNDEFFECT.py

Mô tả: 
Import các file âm thanh 

Author: Đoàn Văn Anh Hiển
Latest Update: 08/06/2003

"""
import pygame
import pymunk
from pymunk.vec2d import Vec2d
import random
import os

pygame.mixer.init()
#Sound effect
goal=pygame.mixer.Sound('anhkoanmung.wav')
goal2=pygame.mixer.Sound('goalde.wav')
siu=pygame.mixer.Sound('siu.wav')
net=pygame.mixer.Sound('net.wav')
head=pygame.mixer.Sound('ball.wav')
hitpost=pygame.mixer.Sound('hitpost.wav')
viva=pygame.mixer.Sound('viva.wav')
seven=pygame.mixer.Sound('Final Euro 2016 - Seven Nation Army.mp3')
ketthuc=pygame.mixer.Sound('ending.wav')
glory=pygame.mixer.Sound('Bài hát truyền thống CLB Man United -Glory Glory Man United- - Vinh quang cho Man United.wav')

music_list=['viva.wav','Final Euro 2016 - Seven Nation Army.mp3','Bài hát truyền thống CLB Man United -Glory Glory Man United- - Vinh quang cho Man United.wav']
random_element = random.choice(music_list)
music_path = os.path.join('D:\DoanHead\HeadSoccer-Python', random_element)
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)
