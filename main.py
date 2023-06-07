from headscooer.BALL import *
from headscooer.PLAYER import*
from headscooer.BUTTON import *
from headscooer.CONDITION import *
from headscooer.PICTURE import *
from headscooer.SOUNDEFFECT import *
from headscooer.ENV import *

ball=Ball()
p1=Player(200,100)
p2=Player(1720,100)

paused=False

while running:
    win.blit(background,(0,0))
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
            if event.button == 1:  # Nut trai
                mouse_pos = event.pos
                if play_button.collidepoint(mouse_pos):
                    game_running = 'ingame'
                elif play_button2.collidepoint(mouse_pos):
                    game_running ='time'
                    start_time = pygame.time.get_ticks()
                elif menu_button.collidepoint(mouse_pos):
                    game_running = 'menu'
                elif pause_button.collidepoint(mouse_pos):
                    old_running=game_running
                    game_running = 'pause'
                    if old_running=='time':
                        paused=True
                elif quit_button.collidepoint(mouse_pos):
                    running = False
                elif resume_button.collidepoint(mouse_pos) and old_running=='ingame':
                    game_running='ingame'
                elif resume_button.collidepoint(mouse_pos) and old_running=='time':
                    game_running='time'
                elif menu_button.collidepoint(mouse_pos):
                    game_running='menu'
                print('game:',game_running)

    if game_running=='menu':
        win.fill('white')
        p1.score=0
        p2.score=0
        f = pygame.font.Font(None, 200)
        title=f.render("HEAD SOCCER", True, 'black')
        win.blit(title, (470, 10))
        text2= f.render("Ronaldo wins", True, 'Red')
        text1 = f.render("Hien wins", True, 'Red')
        text3=f.render("DRAW", True, 'yellow')
        if winner=='Hien':
            win.blit(text1, (573, 700))
        elif winner=='Ronaldo':
            win.blit(text2, (510, 700))
        elif winner=='draw':
            win.blit(text3, (680, 700))  
    
        # Ve nut "Play"
        pygame.draw.rect(win, 'green', play_button)
        play_text = font.render("Play Fto5", True, 'black')
        play_text_rect = play_text.get_rect(center=play_button.center)
        win.blit(play_text, play_text_rect)

        pygame.draw.rect(win, 'green', play_button2)
        play_text2 = font.render("Play Time", True, 'black')
        play_text_rect2 = play_text2.get_rect(center=play_button2.center)
        win.blit(play_text2, play_text_rect2)

        # Ve nut "Quit"
        pygame.draw.rect(win, 'red', quit_button)
        quit_text = font.render("Quit", True, 'black')
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        win.blit(quit_text, quit_text_rect)
        
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
        win.blit(gl,(0,800))
        pygame.draw.line(win,'white',(90,1000),(90,800),5)
        pygame.draw.line(win,'white',(1830,800),(1830,1000),5)
        win.blit(gr,(1830,800))

        pygame.draw.rect(win, 'red', pause_button)
        pause_text = font.render("Pause", True, 'white')
        pause_text_rect = pause_text.get_rect(center=pause_button.center)
        win.blit(pause_text, pause_text_rect)

        

    elif game_running=='time':
        current_time = pygame.time.get_ticks()
        print(current_time)
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
        win.blit(gl,(0,800))
        pygame.draw.line(win,'white',(90,1000),(90,800),5)
        pygame.draw.line(win,'white',(1830,800),(1830,1000),5)
        win.blit(gr,(1830,800))
        pygame.draw.rect(win, 'red', pause_button)
        pause_text = font.render("Pause", True, 'white')
        pause_text_rect = pause_text.get_rect(center=pause_button.center)
        win.blit(pause_text, pause_text_rect)

        

    elif game_running =='pause':

        pygame.time.delay(16)
        # Nut "Resume"
        pygame.draw.rect(win, 'white', resume_button)
        resume_text = font.render("Resume", True, 'black')
        resume_text_rect = resume_text.get_rect(center=resume_button.center)
        win.blit(resume_text, resume_text_rect)

        # Nut "Quit"
        pygame.draw.rect(win, 'red', quit_button)
        quit_text = font.render("QUIT", True, 'white')
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        win.blit(quit_text, quit_text_rect)

        pygame.draw.rect(win, 'red', menu_button)
        quit_text = font.render("Menu", True, 'white')
        quit_text_rect = quit_text.get_rect(center=menu_button.center)
        win.blit(quit_text, quit_text_rect)
    
    
    pygame.display.flip()   
    clock.tick(FPS)
    dt = 1 / FPS 
    space.step(dt)
    