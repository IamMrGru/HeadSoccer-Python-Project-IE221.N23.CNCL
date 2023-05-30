import pygame
import pymunk

# Khởi tạo Pygame và Pymunk
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, -900)

# Tạo mặt đất
ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
ground_shape = pymunk.Segment(ground_body, (0, 50), (800, 50), 5)
ground_shape.friction = 1.0
space.add(ground_body,ground_shape)

# Tạo nhân vật
player_body = pymunk.Body(1, 1666)
player_shape = pymunk.Poly.create_box(player_body, (40, 80))
player_shape.friction = 0.7
player_body.position = 100, 100
space.add(player_body, player_shape)

# Xử lý di chuyển nhân vật
movement = 0

# Xử lý nhảy nhân vật
can_jump = False

def jump():
    if can_jump:
        player_body.apply_impulse_at_local_point((0, 30000))

# Vòng lặp chính
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

    screen.fill((255, 255, 255))

    # Cập nhật vật lý
    dt = 1.0 / 60.0
    for _ in range(10):
        space.step(dt / 10.0)

    # Di chuyển nhân vật
    player_body.velocity = (movement * 300, player_body.velocity.y)

    # Kiểm tra xem nhân vật có chạm mặt đất không
    can_jump = False
    for contact in space.shapes_collide(ground_shape, player_shape):
        if contact.point.y < 50:
            can_jump = True

    # Vẽ mặt đất
    pygame.draw.line(screen, (0, 0, 0), (0, 50), (800, 50), 5)

    # Vẽ nhân vật
    vertices = player_shape.get_vertices()
    vertices = [(int(v.x), int(v.y)) for v in vertices]
    pygame.draw.polygon(screen, (0, 0, 0), vertices)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
