win = pygame.display.set_mode((1920,1000))
pygame.display.set_caption("Head Soccer")
clock=pygame.time.Clock()
space=pymunk.Space()
space.gravity=(0,-1000)
FPS=64
size=(1920,1000)