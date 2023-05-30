import pymunk
import pygame
from pymunk import pygame_util
from pymunk.vec2d import Vec2d

pygame.init()
width, height = 1920, 1000
win = pygame.display.set_mode((width, height))

def draw(space, window, draw_options):
    window.fill('white')
    space.debug_draw(draw_options)
    pygame.display.update()

def createBoundaries(space, width, height):
    rects = [
        [(width / 2, height - 10), (width, 20)],
        [(width / 2, 10), (width, 20)],
        [(10, height / 2), (20, height)],
        [(width - 10, height / 2), (20, height)]
    ]
    for pos, size in rects:
        limit_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        limit_body.position = pos
        limit_shape = pymunk.Poly.create_box(limit_body, size)
        limit_shape.elasticity = 0.4
        limit_shape.friction = 0.5
        space.add(limit_body, limit_shape)

def ball(space, radius, mass):
    ball_body = pymunk.Body()
    ball_body.position = (300, 300)
    ball_shape = pymunk.Circle(ball_body, radius)
    ball_shape.mass = mass
    ball_shape.elasticity = 0.7
    ball_shape.friction = 0.4
    space.add(ball_body, ball_shape)
    return ball_body

def run(window, width, height):
    running = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1 / fps

    space = pymunk.Space()
    space.gravity = (0, 1000)

    ball_body = ball(space, 30, 10)
    createBoundaries(space, width, height)

    movement = 0

    draw_options = pygame_util.DrawOptions(win)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jump(ball_body)
                if event.key == pygame.K_RIGHT:
                    movement = 1
                elif event.key == pygame.K_LEFT:
                    movement = -1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and movement == 1:
                    movement = 0
                elif event.key == pygame.K_LEFT and movement == -1:
                    movement = 0

        ball_body.velocity = (movement * 300, ball_body.velocity.y)  # Đặt vận tốc theo hướng di chuyển

        draw(space, win, draw_options)
        space.step(dt)
        clock.tick(fps)

    pygame.quit()

def jump(body):
    # Kiểm tra xem đối tượng có đang tiếp xúc với mặt phẳng không
    contacts = body.shapes_collide()
    if contacts:
        body.apply_impulse_at_local_point((0, -10000))  # Áp dụng một lực để nhảy lên

if __name__ == '__main__':
    run(win,width,height)
