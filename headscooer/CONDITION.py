"""
Tên module: CONDITION.py

Mô tả: Thiết lập các điều kiện cần thiết:
- Giới hạn khung hình 
- Tạo các vật tĩnh khung thành
- GOALine
- Công nhận bàn thắng
- Chạm bóng và các vật thể còn lại
- Chạm xà ngang
- Bảng tỉ số, tỉ số của mỗi người chơi
- Cài đặt thời gian cho chế độ time là 2 phút

Author: Đoàn Văn Anh Hiển
Latest Update: 08/06/2003

"""
import pygame
import pymunk
from pymunk.vec2d import Vec2d
import random
import os
from .ENV import *
from .SOUNDEFFECT import *

collision_type_0=0
collision_type_1=1
collision_type_2=2
collision_type_3=3


#Boundary
# # Tạo đường biên giới bên trái
left_wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
left_wall_shape = pymunk.Segment(left_wall_body, (0, 0), (0, 1000),30 )
left_wall_shape.elasticity=0.2
space.add(left_wall_body,left_wall_shape)

# # Tạo đường biên giới bên phải

right_wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
right_wall_shape = pymunk.Segment(right_wall_body, (1920, 0), (1920, 1000), 27)
right_wall_shape.elasticity=0.2
space.add(right_wall_body,right_wall_shape)

# #Đường ở dưới
segment_body=pymunk.Body(body_type=pymunk.Body.STATIC)
segment_shape=pymunk.Segment(segment_body,(0,0),(1920,0),10)
segment_shape.elasticity=1
space.add(segment_body,segment_shape)

top_body=pymunk.Body(body_type=pymunk.Body.STATIC)
top_shape=pymunk.Segment(top_body,(0,1000),(1920,1000),5)
top_shape.elasticity=0.5
space.add(top_body,top_shape)

right_post_body=pymunk.Body(body_type=pymunk.Body.STATIC)
right_post_shape=pymunk.Segment(right_post_body,(1830,200),(1920,200),5)
right_post_shape.elasticity=1.2
space.add(right_post_body,right_post_shape)

left_post_body=pymunk.Body(body_type=pymunk.Body.STATIC)
left_post_shape=pymunk.Segment(left_post_body,(0,200),(90,200),5)
left_post_shape.elasticity=1.2
space.add(left_post_body,left_post_shape)
#GOaline

goal_line_body = pymunk.Body(body_type=pymunk.Body.STATIC)
goal_line_shape = pymunk.Segment(goal_line_body, (1900, 0), (1900, 200),30)
goal_line_shape.sensor = True  # Đánh dấu shape là sensor
goal_line_shape.collision_type=collision_type_2
space.add(goal_line_body,goal_line_shape)

#GOaline2
goal_line2_body = pymunk.Body(body_type=pymunk.Body.STATIC)
goal_line2_shape = pymunk.Segment(goal_line2_body, (40, 0), (40, 200), 30)
goal_line2_shape.sensor = True  # Đánh dấu shape là sensor
goal_line2_shape.collision_type=collision_type_3
space.add(goal_line2_body,goal_line2_shape)

def touchball(shape_player,shape_player2,shape_ball1,bottom_shape):
    """ 
touchball(shape_player,shape_player2,shape_ball1,bottom_shape)
Input: hình dạng người chơi 1 ,2 , hình dạng bóng, hình dạng mặt sàn
Output: NONE
Chức năng:
- Phát hiện sự va chạm giữa các vật thể
- Phát âm thanh chạm bóng

    """
    contacts = shape_player.shapes_collide(shape_ball1)
    contacts2 = shape_player2.shapes_collide(shape_ball1)
    contacts3=shape_ball1.shapes_collide(bottom_shape)
    if len(contacts.points) !=0  or len(contacts2.points)!=0 or len(contacts3.points) !=0 :
        head.play()


def touchpost(shape_ball1):
    """ 
touchpost(shape_ball1)
Input: hình dạng bóng
Output: NONE
Chức năng:
- Phát hiện sự va chạm giữa bóng và xà ngang
- Phát âm thanh
    """
    contacts = right_post_shape.shapes_collide(shape_ball1)
    contacts2 = left_post_shape.shapes_collide(shape_ball1)
    if len(contacts.points) !=0  or len(contacts2.points)!=0 :
        hitpost.play()

def update_score(s1,s2):
    """ 
update_score(s1,s2)
Input: điểm của người chơi 1 và 2
Output: NONE
Chức năng:
- In lên màn hình điểm của người chơi
    """
    font = pygame.font.Font(None, 200)
    text2= font.render(f"{s2}", True, 'Red')
    text1 = font.render(f"{s1}", True, 'Green')
    win.blit(text1, (20, 10))
    win.blit(text2,(1820,10))

movement = 0
movement2=0
running = True
game_running ='menu'

collision_type_0 = 0
collision_type_1 = 1
collision_type_2 = 2
collision_type_3 = 3


score_player1 = 0
score_player2 = 0
max_score = 5

winner=''

countdown_time = 120  # 2 minutes
countdown = countdown_time * 1000  # convert to milliseconds

