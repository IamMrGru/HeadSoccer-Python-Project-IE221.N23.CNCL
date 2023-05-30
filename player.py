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

#Tạo cặp va chạm
collision_type_1 = 1
collision_type_2 = 2
collision_type_3 = 3


width, height = 1920, 1000
mass = 0.5
radius = 30
moment = pymunk.moment_for_circle(mass, 0, radius,(0,0))
body = pymunk.Body(mass, moment)
body.position = (1910,10)
shape = pymunk.Circle(body, radius)
shape.collision_type=collision_type_1
shape.elasticity = 0.5  # Độ đàn hồi khi va chạm với các vật thể khác
space.add(body, shape)


# Tạo đường biên giới bên trái
left_wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
left_wall_shape = pymunk.Segment(left_wall_body, (0, 0), (0, 1000),30 )
left_wall_shape.elasticity=0
space.add(left_wall_body,left_wall_shape)

# Tạo đường biên giới bên phải

right_wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
right_wall_shape = pymunk.Segment(right_wall_body, (1920, 0), (1920, 1000), 30)
right_wall_shape.elasticity=0
space.add(right_wall_body,right_wall_shape)

#Đường ở dưới
segment_body=pymunk.Body(body_type=pymunk.Body.STATIC)
segment_shape=pymunk.Segment(segment_body,(0,0),(1910,0),2)
segment_shape.elasticity=1
space.add(segment_body,segment_shape)


top_body=pymunk.Body(body_type=pymunk.Body.STATIC)
top_shape=pymunk.Segment(top_body,(0,1000),(1910,1000),2)
top_shape.elasticity=1
space.add(top_body,top_shape)

#GOaline
goal_line_body = pymunk.Body(body_type=pymunk.Body.STATIC)
goal_line_shape = pymunk.Segment(goal_line_body, (1900, 0), (1900, 200), 5)
goal_line_shape.sensor = True  # Đánh dấu shape là sensor
goal_line_shape.collision_type=collision_type_2
space.add(goal_line_body,goal_line_shape)

#GOaline2
goal_line2_body = pymunk.Body(body_type=pymunk.Body.STATIC)
goal_line2_shape = pymunk.Segment(goal_line2_body, (0, 0), (0, 200), 5)
goal_line2_shape.sensor = True  # Đánh dấu shape là sensor
goal_line2_shape.collision_type=collision_type_3
space.add(goal_line2_body,goal_line2_shape)

def goal_reached(arbiter, space, data):
    # Lấy đối tượng bóng
    ball = arbiter.shapes[0] if arbiter.shapes[0].collision_type != 1 else arbiter.shapes[1]    
    # Kiểm tra nếu đối tượng bóng qua vạch goaline
    if (ball.body.position.x <1800 and ball.body.position.y<20):
        print("Bàn thắng cho đội khách!")
    return True
def goal_reached2(arbiter1, space, data):
    # Lấy đối tượng bóng
    ball2 = arbiter1.shapes[0] if arbiter1.shapes[0].collision_type != 1 else arbiter1.shapes[1]    
    # Kiểm tra nếu đối tượng bóng qua vạch goaline
    if (ball2.body.position.x <10 and ball2.body.position.y<20):
        print("Bàn thắng cho đội nhà!")
    return True


def jump():
    # Kiểm tra xem nhân vật có đang tiếp xúc với mặt phẳng không
    contacts = shape.shapes_collide(segment_shape)
    if contacts:
        body.apply_impulse_at_local_point((0, 230))  # Áp dụng một lực để nhân vật nhảy lên

handler = space.add_collision_handler(collision_type_1, collision_type_2)  # Đăng ký bộ xử lý cho cặp collision types
handler2= space.add_collision_handler(collision_type_1,collision_type_3)
handler.begin = goal_reached  
handler2.begin=goal_reached2
movement = 0
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()
            elif event.key == pygame.K_RIGHT:
                movement = 1
            elif event.key == pygame.K_LEFT:
                movement = -1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and movement == 1:
                movement = 0
            elif event.key == pygame.K_LEFT and movement == -1:
                movement = 0
    

    win.fill('White')  # Xóa màn hình

    # Cập nhật không gian vật lý
    dt = 1 / 60.0  # Thời gian giữa các khung hình (60 FPS)
    space.step(dt)
    body.velocity = (movement * 290, body.velocity.y)
    # Vẽ nhân vật
    pos = body.position
    pygame.draw.circle(win, (0, 0, 255), (int(pos.x), int(1000 - pos.y)), radius)
    # print(pos.x,pos.y)
    # Vẽ mặt phẳng

    #pygame.draw.line(win, (0, 0, 0), (0, height - 10), (width, height - 10), 5)
    #pygame.draw.line(win, (0, 0, 0), (0, height - 10), (0,0), 5)

    
    pygame.display.flip()   
    clock.tick(60)



