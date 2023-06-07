"""
Tên module: BUTTON.py

Mô tả: Tạo các nút xuất hiện trên màn hình.

Author: Đoàn Văn Anh Hiển
Latest Update: 08/06/2003

Các hằng số:
- play_button: Hình chữ nhật đại diện cho nút "Play".
- quit_button: Hình chữ nhật đại diện cho nút "Quit".
- play_button2: Hình chữ nhật đại diện cho nút "Play 2".
- resume_button: Hình chữ nhật đại diện cho nút "Resume".
- menu_button: Hình chữ nhật đại diện cho nút "Menu".
- pause_button: Hình chữ nhật đại diện cho nút "Pause".

"""

import pygame
import pymunk
from pymunk.vec2d import Vec2d
import random
import os


play_button = pygame.Rect(650, 200, 550, 100)
quit_button = pygame.Rect(650, 500, 550, 100)
play_button2 = pygame.Rect(650, 350, 550, 100)
resume_button =pygame.Rect(350, 200, 250, 100)
menu_button= pygame.Rect(1000, 700, 250, 100)
pause_button= pygame.Rect(180, 0, 130, 100)
