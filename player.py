import pymunk
import pygame

win = pygame.display.set_mode((1920,1000))
pygame.display.set_caption("Head Soccer")
clock=pygame.time.Clock()
space=pymunk.Space()
space.gravity=(0,-1000)
FPS=64
size=(1920,1000)
collision_type_0 = 0
collision_type_1 = 1
collision_type_2 = 2
collision_type_3 = 3

class Player:
    def __init__(self,x,y):
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
        contacts = self.shape_player.shapes_collide(bottom_shape)
        if  len(contacts.points) !=0:
            self.player .apply_impulse_at_local_point((0, 700)) 
    def land(self,bottom_shape):
        contacts = self.shape_player.shapes_collide(bottom_shape)
        if  len(contacts.points) ==0:
            self.player .apply_impulse_at_local_point((0, -900))
    def vtoc(self):
        self.player .velocity = (self.movement * 400, self.player.velocity.y)
    def draw(self,pic):
        pos1=self.player.position
        pygame.draw.circle(win,'green',(int(pos1.x),int(size[1]-pos1.y)),self.radius1)
        rect = pic.get_rect(center=(pos1.x, 1000-pos1.y))
        win.blit(pic, rect)
