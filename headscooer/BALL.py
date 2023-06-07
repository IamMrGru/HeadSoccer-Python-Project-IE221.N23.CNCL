"""
Tên module: BALL.py

Mô tả: Khởi tạo đối tượng Ball/ quả bóng.

Author: Đoàn Văn Anh Hiển
Latest Update: 08/06/2003

"""
import pygame
import pymunk
from pymunk.vec2d import Vec2d
from .ENV import *
from .SOUNDEFFECT import *
from .PICTURE import *

class Ball:
    def __init__(self):
        """ 
Ball.__init__(self)
Input: NONE
Output: NONE
Chức năng:
- Hàm khởi tạo lớp Ball. 
- Tạo một vật thể hình tròn (self.ball) và một hình dạng tròn (self.shape_ball) sử dụng module pymunk.
- Thiết lập các thuộc tính của vật thể và hình dạng, sau đó thêm chúng vào không gian vật lý (space). 
        """
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
        ''' 
goal(self,p1,p2)
Input: p1: Đối tượng Player 1, p2: Đối tượng Player 2.
Output: NONE
Chức năng:
- Kiểm tra xem vị trí hiện tại của quả bóng có nằm trong vùng ghi bàn hay không.
- Nếu bóng đi qua vùng ghi bàn của Player 1 hoặc Player 2, cập nhật điểm số tương ứng và thực hiện các tác vụ liên quan như phát âm thanh và đặt lại vị trí của quả bóng.
        '''
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
        ''' 
draw(self)
Input: hình ảnh
Output: NONE
Chức năng:
-  Chèn hình ảnh quả bóng
        '''
        pos=self.ball.position
        pygame.draw.circle(win,'Black',(int(pos.x),int(size[1]-pos.y)),self.radius2)
        ball_rect = ballpic.get_rect(center=(pos.x, 1000-pos.y))
        win.blit(ballpic, ball_rect)


