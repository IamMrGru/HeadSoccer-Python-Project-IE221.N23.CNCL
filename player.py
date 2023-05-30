import pygame
import pymunk
from pymunk.vec2d import Vec2d

pygame.init()
win = pygame.display.set_mode((1920,1000))
pygame.display.set_caption("Demo Ball movement")
clock=pygame.time.Clock()
space=pymunk.Space()
space.gravity=(0,-1000)
FPS=80
size=(1910,1000)
running=True

#Tạo cặp va chạm
collision_type_0=0
collision_type_1 = 1
collision_type_2 = 2
collision_type_3 = 3


# width, height = 1920, 1000
# mass = 0.1
# radius = 30                             
# moment = pymunk.moment_for_circle(mass, 0, radius,(0,0))
# body = pymunk.Body(mass, moment)
# body.position = (960,0)               
# shape = pymunk.Circle(body, radius)
# shape.collision_type=collision_type_1
# shape.density=1
# shape.elasticity = 1  # Độ đàn hồi khi va chạm với các vật thể khác
# shape.friction=2
# space.add(body, shape)  

mass = 0.5
radius1 = 40
moment = pymunk.moment_for_circle(mass, 0, radius1,(0,0))
player = pymunk.Body(mass, moment)
player.position = (200,100)
shape_player  = pymunk.Circle(player, radius1)
shape_player .collision_type=collision_type_0
shape_player .elasticity = 0.4  # Độ đàn hồi khi va chạm với các vật thể khác
space.add(player, shape_player )

mass = 0.5
radius1 = 40
moment = pymunk.moment_for_circle(mass, 0, radius1,(0,0))
player2 = pymunk.Body(mass, moment)
player2.position = (1720,100)
shape_player2  = pymunk.Circle(player2, radius1)
shape_player2 .collision_type=collision_type_0
shape_player2 .elasticity = 0.4  # Độ đàn hồi khi va chạm với các vật thể khác
space.add(player2, shape_player2 )

mass = 0.5
radius2 = 30
moment = pymunk.moment_for_circle(mass, 0, radius2,(0,0))
ball1 = pymunk.Body(mass, moment)
ball1.position = (960,500)
shape_ball1 = pymunk.Circle(ball1, radius2)
shape_ball1.collision_type=collision_type_1
shape_ball1.elasticity = 1  # Độ đàn hồi khi va chạm với các vật thể khác
space.add(ball1, shape_ball1)


# # Tạo đường biên giới bên trái
left_wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
left_wall_shape = pymunk.Segment(left_wall_body, (0, 0), (0, 1000),30 )
left_wall_shape.elasticity=0
space.add(left_wall_body,left_wall_shape)

# # Tạo đường biên giới bên phải

right_wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
right_wall_shape = pymunk.Segment(right_wall_body, (1920, 0), (1920, 1000), 27)
right_wall_shape.elasticity=0
space.add(right_wall_body,right_wall_shape)

# #Đường ở dưới
segment_body=pymunk.Body(body_type=pymunk.Body.STATIC)
segment_shape=pymunk.Segment(segment_body,(0,0),(1920,0),10)
segment_shape.elasticity=1
space.add(segment_body,segment_shape)

top_body=pymunk.Body(body_type=pymunk.Body.STATIC)
top_shape=pymunk.Segment(top_body,(0,1000),(1920,1000),5)
top_shape.elasticity=1
space.add(top_body,top_shape)




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

def goal_reached(arbiter, space, data):
    # Lấy đối tượng bóng
    Ball = arbiter.shapes[0] if arbiter.shapes[0].collision_type != 1 else arbiter.shapes[1]    
    # Kiểm tra nếu đối tượng bóng qua vạch goaline
    if (Ball.body.position.x <1900 and Ball.body.position.y<20):
        print("Bàn thắng cho đội khách!")
    return True

def goal_reached2(arbiter1, space, data):
    # Lấy đối tượng bóng
    Ball2 = arbiter1.shapes[0] if arbiter1.shapes[0].collision_type != 1 else arbiter1.shapes[1]    
    # Kiểm tra nếu đối tượng bóng qua vạch goaline
    if (Ball2.body.position.x <10 and Ball2.body.position.y<20):
        print("Bàn thắng cho đội nhà!")
    return True


def jump():
    # Kiểm tra xem nhân vật có đang tiếp xúc với mặt phẳng không
    contacts = shape_player.shapes_collide(segment_shape)
    if contacts:
        player .apply_impulse_at_local_point((0, 230))  # Áp dụng một lực để nhân vật nhảy lên

def jump1():
    # Kiểm tra xem nhân vật có đang tiếp xúc với mặt phẳng không
    contacts = shape_player2.shapes_collide(segment_shape)
    if contacts:
        player2 .apply_impulse_at_local_point((0, 230))  # Áp dụng một lực để nhân vật nhảy lên

handler = space.add_collision_handler(collision_type_1, collision_type_2)  # Đăng ký bộ xử lý cho cặp collision types
handler2= space.add_collision_handler(collision_type_1,collision_type_3)


handler.begin =goal_reached  
handler2.begin=goal_reached2

movement = 0
movement2=0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jump()
            elif event.key == pygame.K_RIGHT:
                movement = 1
            elif event.key == pygame.K_LEFT:
                movement = -1
            elif event.key == pygame.K_w:
                jump1()
            elif event.key == pygame.K_d:
                movement2 = 1
            elif event.key == pygame.K_a:
                movement2 = -1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and movement == 1:
                movement = 0
            elif event.key == pygame.K_LEFT and movement == -1:
                movement = 0
            elif event.key == pygame.K_d and movement2 == 1:
                movement2 = 0
            elif event.key == pygame.K_a and movement2 == -1:
                movement2 = 0

    win.fill('White')  # Xóa màn hình

    # Cập nhật không gian vật lý
    dt = 1 / 60.0  # Thời gian giữa các khung hình (60 FPS)
    space.step(dt)
    player .velocity = (movement * 350, player .velocity.y)
    player2 .velocity = (movement2 * 350, player2 .velocity.y)
    # Vẽ nhân vật
    pos1 = player .position
    pygame.draw.circle(win,'green',(int(pos1.x),int(size[1]-pos1.y)),radius1)
    pos2 = player2 .position
    pygame.draw.circle(win,'red',(int(pos2.x),int(size[1]-pos2.y)),radius1)

    pygame.draw.line(win,'red',(0, 0), (0, 1000),30)
    pygame.draw.line(win,'red',(1920, 0), (1920, 1000), 30)
    pygame.draw.line(win,'red', (0,1000),(1920,1000),10)
    pos=ball1.position
    pygame.draw.circle(win,'Black',(int(pos.x),int(size[1]-pos.y)),radius2)
    # pos=body.position
    # pygame.draw.circle(win, 'blue', (int(pos.x), int(size[1] - pos.y)), radius)
    pygame.display.flip()   
    clock.tick(60)



