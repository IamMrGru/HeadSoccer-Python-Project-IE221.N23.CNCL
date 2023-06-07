"""
Tên module: PLAYER.py

Mô tả: 
Tạo lớp người chơi

Author: Đoàn Văn Anh Hiển
Latest Update: 08/06/2003

"""
import pygame
import pymunk
from .ENV import *

collision_type_0 = 0
collision_type_1 = 1
collision_type_2 = 2
collision_type_3 = 3


class Player:
    def __init__(self,x,y):
        """ 
__init__(self,x,y)
Input: tọa độ x,y của người chơi
Output: NONE
Chức năng:
- Hàm khởi tạo lớp Player. 
- Tạo một vật thể hình tròn (self.player) và một hình dạng tròn (self.shape_player) sử dụng module pymunk.
- Thiết lập các thuộc tính của vật thể và hình dạng, sau đó thêm chúng vào không gian vật lý (space). 
    """
        self.mass = 1
        self.radius1 = 40
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius1,(0,0))
        self.player = pymunk.Body(self.mass, self.moment)
        self.player.position = (x,y)
        self.shape_player  = pymunk.Circle(self.player, self.radius1)
        self.shape_player .collision_type=collision_type_0
        self.shape_player .elasticity = 0.2  # Độ đàn hồi khi va chạm với các vật thể khác
        space.add(self.player, self.shape_player)
        self.score=0
        self.movement=0
    def jump(self,bottom_shape):
        """ 
jump(self,bottom_shape)
Input: hình dạng của mặt sàn
Output: NONE
Chức năng:
- Phát hiện nhân vật có chạm sàn hay không
- Nếu có thì có áp dụng một lực nhảy
- Nếu không thì có áp dụng một lực hút để có thể hạ mặt đất 
    """
        contacts = self.shape_player.shapes_collide(bottom_shape)
        if  len(contacts.points) !=0:
            self.player .apply_impulse_at_local_point((0, 700)) 
    def land(self,bottom_shape):
        """ 
land(self,bottom_shape)
Input: hình dạng của mặt sàn
Output: NONE
Chức năng:
- Phát hiện nhân vật có chạm sàn hay không
- Nếu không thì có áp dụng một lực hút để có thể hạ mặt đất 
    """
        contacts = self.shape_player.shapes_collide(bottom_shape)
        if  len(contacts.points) ==0:
            self.player .apply_impulse_at_local_point((0, -900))
    def vtoc(self):
        """ 
vtoc(self)
Input: NONE
Output: NONE
Chức năng:
- Tăng tốc cho nhân vật di chuyển trên trục tung
    """
        self.player .velocity = (self.movement * 400, self.player.velocity.y)
    def draw(self,pic):
        """ 
draw(self,pic)
Input: hình ảnh nhân vật
Output: NONE
Chức năng:
- Chèn hình ảnh 
    """   
        pos1=self.player.position
        pygame.draw.circle(win,'green',(int(pos1.x),int(size[1]-pos1.y)),self.radius1)
        rect = pic.get_rect(center=(pos1.x, 1000-pos1.y))
        win.blit(pic, rect)
