import pygame
import pymunk

pygame.init()
win = pygame.display.set_mode((1920,1000))
pygame.display.set_caption("Demo Ball movement")
clock=pygame.time.Clock()
space=pymunk.Space()
space.gravity=(0,-1000)
FPS=80
size=(1910,1000)
running=True

def conver_coordinates(point): #đỔI TỌA ĐỘ
    return point[0],1000-point[1]
ball_radius=30
body=pymunk.Body()
body.position=955,1000 #Gốc tọa độ là phía dưới bên trái (ngược lại với Pygame)
shape=pymunk.Circle(body,ball_radius)
shape.density=1
shape.elasticity=0.7
space.add(body,shape)

segment_body=pymunk.Body(body_type=pymunk.Body.STATIC)
segment_shape=pymunk.Segment(segment_body,(0,2),(1920,2),2)
segment_shape.elasticity=1
space.add(segment_body,segment_shape)

im_ball=pygame.image.load('ball.png')
im_ball=pygame.transform.scale(im_ball,(ball_radius*2.5,ball_radius*2.5))
while running:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running=False
    win.fill('Black')
    x,y= conver_coordinates (body.position)
    #pygame.draw.circle(win,'Red',(int(x),int(y)),ball_radius)
    win.blit(im_ball,(int(x)-ball_radius,int(y)-ball_radius))
    pygame.draw.line(win,'Green',(0,1000),(1920,1000),10)
    pygame.display.update()
    clock.tick(FPS)
    space.step(1/FPS)