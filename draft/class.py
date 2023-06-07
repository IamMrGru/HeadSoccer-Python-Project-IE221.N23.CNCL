import pygame
import pymunk
from pymunk.vec2d import Vec2d
import random
import os

pygame.init()
pygame.mixer.init()
win = pygame.display.set_mode((1920,1000))
pygame.display.set_caption("Head Soccer")
clock=pygame.time.Clock()
space=pymunk.Space()
space.gravity=(0,-1000)
FPS=64
size=(1920,1000)
running=True

# Hình
background=pygame.image.load('stadium2.jpg')
background=pygame.transform.scale(background,size)
menubg=pygame.image.load('bong-da-dau-to-2023-640.jpg')
menubg=pygame.transform.scale(menubg,size)
ballpic=pygame.image.load('ball.png')
ballpic=pygame.transform.scale(ballpic,(30*2.8,30*2.8))
pc1=pygame.image.load('hien.png')
pc1=pygame.transform.scale(pc1,(40*3.2,40*3.2))
pc2=pygame.image.load('ronaldo.png')
pc2=pygame.transform.scale(pc2,(40*3.2,40*3.2))

#Sound effect
goal=pygame.mixer.Sound('anhkoanmung.wav')
goal2=pygame.mixer.Sound('goalde.wav')
siu=pygame.mixer.Sound('siu.wav')
net=pygame.mixer.Sound('net.wav')
head=pygame.mixer.Sound('ball.wav')
hitpost=pygame.mixer.Sound('hitpost.wav')
viva=pygame.mixer.Sound('viva.wav')
seven=pygame.mixer.Sound('Final Euro 2016 - Seven Nation Army.mp3')
ketthuc=pygame.mixer.Sound('ending.wav')
glory=pygame.mixer.Sound('Bài hát truyền thống CLB Man United -Glory Glory Man United- - Vinh quang cho Man United.wav')


movement = 0
movement2=0
running = True
game_running ='menu'

#Button
font = pygame.font.Font(None, 50)
play_button = pygame.Rect(300, 200, 200, 100)
quit_button = pygame.Rect(300, 500, 200, 100)
play_button2 = pygame.Rect(300, 350, 200, 100)
resume_button =pygame.Rect(300, 200, 200, 100)
menu_button= pygame.Rect(300, 350, 200, 100)
pause_button= pygame.Rect(180, 0, 130, 100)
winner=''

countdown_time = 120  # 2 minutes
countdown = countdown_time * 1000  # convert to milliseconds
start_time = pygame.time.get_ticks()

#Tạo cặp va chạm
collision_type_0 = 0
collision_type_1 = 1
collision_type_2 = 2
collision_type_3 = 3


score_player1 = 0
score_player2 = 0
max_score = 5



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

music_list=['viva.wav','Final Euro 2016 - Seven Nation Army.mp3','Bài hát truyền thống CLB Man United -Glory Glory Man United- - Vinh quang cho Man United.wav']
random_element = random.choice(music_list)
music_path = os.path.join('D:\DoanHead\HeadSoccer-Python', random_element)
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)

def touchball(shape_player,shape_player2,shape_ball1,bottom_shape):
    contacts = shape_player.shapes_collide(shape_ball1)
    contacts2 = shape_player2.shapes_collide(shape_ball1)
    contacts3=shape_ball1.shapes_collide(bottom_shape)
    if len(contacts.points) !=0  or len(contacts2.points)!=0 or len(contacts3.points) !=0 :
        head.play()


def touchpost(shape_ball1):
    contacts = right_post_shape.shapes_collide(shape_ball1)
    contacts2 = left_post_shape.shapes_collide(shape_ball1)
    if len(contacts.points) !=0  or len(contacts2.points)!=0 :
        hitpost.play()

def update_score(s1,s2):
    font = pygame.font.Font(None, 200)
    text2= font.render(f"{s2}", True, 'Red')
    text1 = font.render(f"{s1}", True, 'Green')
    win.blit(text1, (20, 10))
    win.blit(text2,(1820,10))

class Ball:
    def __init__(self):
        self.mass = 0.3
        self.radius2 = 30
        self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius2,(0,0))
        self.ball = pymunk.Body(self.mass, self.moment)
        self.ball.position = (960,500)
        self.shape_ball = pymunk.Circle(self.ball, self.radius2)
        self.shape_ball.collision_type=collision_type_1
        self.shape_ball.elasticity = 1  # Độ đàn hồi khi va chạm với các vật thể khác
        space.add(self.ball, self.shape_ball)
    def goal(self,p1,p2):
        pos=self.ball.position
        if(pos.x<60 and pos.y<167):
            net.play()
            goal.play()
            pygame.time.wait(4000)  # Wait for 2 seconds
            space.remove(self.ball, self.shape_ball)  # Remove the ball from the space
            self.ball.position = (960, 800)  # Reset the ball's position
            space.add(self.ball, self.shape_ball)  # Add the ball back to the space
            p2.score+=1
            siu.play()
        if(pos.x>1863 and pos.y<167):
            net.play()
            goal2.play()
            pygame.time.wait(4000)  # Wait for 2 seconds
            space.remove(self.ball, self.shape_ball)  # Remove the ball from the space
            self.ball.position = (960, 800)  # Reset the ball's position
            space.add(self.ball, self.shape_ball)  # Add the ball back to the space
            p1.score+=1
    def draw(self):
        pos=self.ball.position
        pygame.draw.circle(win,'Black',(int(pos.x),int(size[1]-pos.y)),self.radius2)
        ball_rect = ballpic.get_rect(center=(pos.x, 1000-pos.y))
        win.blit(ballpic, ball_rect)

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

ball=Ball()
p1=Player(200,100)
p2=Player(1720,100)
while running:
    win.blit(background,(0,0))
    if game_running=='menu':
        win.fill('white')
        f = pygame.font.Font(None, 200)
        title=f.render("HEAD SOCCER", True, 'black')
        win.blit(title, (560, 10))
        text2= f.render("Ronaldo wins", True, 'Red')
        text1 = f.render("Hien wins", True, 'Red')
        text3=f.render("DRAW", True, 'yellow')
        if winner=='Hien':
            win.blit(text1, (560, 500))
        elif winner=='Ronaldo':
            win.blit(text2, (560, 500))
        elif winner=='draw':
            win.blit(text3, (560, 500))   

        # Vẽ nút "Play"
        pygame.draw.rect(win, 'white', play_button)
        play_text = font.render("Play Fto5", True, 'black')
        play_text_rect = play_text.get_rect(center=play_button.center)
        win.blit(play_text, play_text_rect)

        pygame.draw.rect(win, 'white', play_button2)
        play_text2 = font.render("Play Time", True, 'black')
        play_text_rect2 = play_text2.get_rect(center=play_button2.center)
        win.blit(play_text2, play_text_rect2)

        # Vẽ nút "Quit"
        pygame.draw.rect(win, 'white', quit_button)
        quit_text = font.render("Quit", True, 'black')
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        win.blit(quit_text, quit_text_rect)
        pygame.display.flip()
        clock.tick(FPS)
        dt = 1 / FPS # Thời gian giữa các khung hình (60 FPS)
        space.step(dt)

    elif game_running== 'ingame':
        touchball(p1.shape_player,p2.shape_player,ball.shape_ball,segment_shape)
        touchpost(ball.shape_ball)
        p1.vtoc()
        p2.vtoc()
        ball.draw()
        p1.draw(pc1)
        p2.draw(pc2)
        ball.goal(p1,p2)
        update_score(p1.score,p2.score)
        if p1.score >= max_score or p2.score >= max_score:
            pygame.time.wait(5000)
            ketthuc.play()
            if p1.score>=max_score:
                winner='Hien'
            elif p2.score>=max_score:
                winner='Ronaldo'
            pygame.time.wait(5000)  # Wait for 2 seconds
            p1.score = 0  # Reset player 1's score
            p2.score = 0  # Reset player 2's score
            game_running='menu'


        pygame.draw.line(win,'white',(1830,800),(1920,800),5)
        pygame.draw.line(win,'white',(0,800),(90,800),5)

        pygame.draw.line(win,'white',(90,1000),(90,800),5)
        pygame.draw.line(win,'white',(1830,800),(1830,1000),5)

        pygame.draw.rect(win, 'red', pause_button)
        pause_text = font.render("Pause", True, 'white')
        pause_text_rect = pause_text.get_rect(center=pause_button.center)
        win.blit(pause_text, pause_text_rect)

        pygame.display.flip()   
        clock.tick(FPS)
        dt = 1 / FPS # Thời gian giữa các khung hình (60 FPS)
        space.step(dt)

    elif game_running=='time':
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        remaining_time = max(0, countdown - elapsed_time)
        seconds = remaining_time // 1000
        minutes = seconds // 60
        seconds %= 60
        text = font.render(f"{minutes:02}:{seconds:02}", True, 'black')
        text_rect = text.get_rect(center=(1920 // 2, 30))
        win.blit(text, text_rect)
        touchball(p1.shape_player,p2.shape_player,ball.shape_ball,segment_shape)
        touchpost(ball.shape_ball)
        p1.vtoc()
        p2.vtoc()
        ball.draw()
        p1.draw(pc1)
        p2.draw(pc2)
        ball.goal(p1,p2)
        update_score(p1.score,p2.score)
        
        if remaining_time == 0:
            pygame.time.wait(5000)
            ketthuc.play()
            if p1.score>p2.score:
                winner='Hien'  
            elif p1.score==p2.score:
                winner='draw'
            else :
                winner='Ronaldo'
            pygame.time.wait(5000)  # Wait for 2 seconds
            p1.score = 0  # Reset player 1's score
            p2.score= 0  # Reset player 2's score
            game_running='menu'


        pygame.draw.line(win,'white',(1830,800),(1920,800),5)
        pygame.draw.line(win,'white',(0,800),(90,800),5)

        pygame.draw.line(win,'white',(90,1000),(90,800),5)
        pygame.draw.line(win,'white',(1830,800),(1830,1000),5)

        pygame.draw.rect(win, 'red', pause_button)
        pause_text = font.render("Pause", True, 'white')
        pause_text_rect = pause_text.get_rect(center=pause_button.center)
        win.blit(pause_text, pause_text_rect)

        pygame.display.flip()   
        clock.tick(FPS)
        dt = 1 / FPS # Thời gian giữa các khung hình (60 FPS)
        space.step(dt)

    elif game_running =='pause':

        win.fill('Black')
        # Vẽ nút "Resume"
        pygame.draw.rect(win, 'white', resume_button)
        resume_text = font.render("Resume", True, 'black')
        resume_text_rect = resume_text.get_rect(center=resume_button.center)
        win.blit(resume_text, resume_text_rect)

        # Vẽ nút "Quit"
        pygame.draw.rect(win, 'white', quit_button)
        quit_text = font.render("Quit", True, 'black')
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        win.blit(quit_text, quit_text_rect)
        pygame.display.flip()   
        clock.tick(FPS)
        dt = 1 / FPS # Thời gian giữa các khung hình (60 FPS)
        space.step(dt)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                p1.jump(segment_shape)
            elif event.key== pygame.K_DOWN:
                p1.land(segment_shape)
            elif event.key == pygame.K_RIGHT:
                p1.movement= 1
            elif event.key == pygame.K_LEFT:
                p1.movement = -1
            elif event.key == pygame.K_w:
                p2.jump(segment_shape)
            elif event.key== pygame.K_s:
                p2.land(segment_shape)
            elif event.key == pygame.K_d:
                p2.movement = 1
            elif event.key == pygame.K_a:
                p2.movement = -1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and p1.movement == 1:
                p1.movement = 0
            elif event.key == pygame.K_LEFT and p1.movement == -1:
                p1.movement = 0
            elif event.key == pygame.K_d and p2.movement == 1:
                p2.movement = 0
            elif event.key == pygame.K_a and p2.movement == -1:
                p2.movement = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Nút trái chuột
                mouse_pos = event.pos
                if play_button.collidepoint(mouse_pos):
                    game_running = 'ingame'
                elif play_button2.collidepoint(mouse_pos):
                    game_running ='time'
                elif menu_button.collidepoint(mouse_pos):
                    game_running = 'menu'
                elif pause_button.collidepoint(mouse_pos):
                    game_running = 'pause'
                elif quit_button.collidepoint(mouse_pos):
                    running = False
                elif resume_button.collidepoint(mouse_pos):
                    win.blit(background,(0,0))