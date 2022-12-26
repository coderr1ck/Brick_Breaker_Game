import pygame,random
# code for rectangular blocks formation and management
rectLs1 = [[50, 50, 50, 20],
           [110, 50, 50, 20],
           [170, 50, 50, 20],
           [230, 50, 50, 20],
           [290, 50, 50, 20],
           [350, 50, 50, 20],
           [410, 50, 50, 20],
           [470, 50, 50, 20],
           [530, 50, 50, 20],
           [590, 50, 50, 20],
           [650, 50, 50, 20],
           [710, 50, 50, 20]]

rectLs2 = [[50, 80, 50, 20],
           [110, 80, 50, 20],
           [170, 80, 50, 20],
           [230, 80, 50, 20],
           [290, 80, 50, 20],
           [350, 80, 50, 20],
           [410, 80, 50, 20],
           [470, 80, 50, 20],
           [530, 80, 50, 20],
           [590, 80, 50, 20],
           [650, 80, 50, 20],
           [710, 80, 50, 20]]

rectLs3 = [[50, 110, 50, 20],
           [110, 110, 50, 20],
           [170, 110, 50, 20],
           [230, 110, 50, 20],
           [290, 110, 50, 20],
           [350, 110, 50, 20],
           [410, 110, 50, 20],
           [470, 110, 50, 20],
           [530, 110, 50, 20],
           [590, 110, 50, 20],
           [650, 110, 50, 20],
           [710, 110, 50, 20]]

rectLs4 = [[50, 140, 50, 20],
           [110, 140, 50, 20],
           [170, 140, 50, 20],
           [230, 140, 50, 20],
           [290, 140, 50, 20],
           [350, 140, 50, 20],
           [410, 140, 50, 20],
           [470, 140, 50, 20],
           [530, 140, 50, 20],
           [590, 140, 50, 20],
           [650, 140, 50, 20],
           [710, 140, 50, 20]]

pygame.init()                    
state = True

def gamestate(reservedRect):
    state = True
    global rectLs1,rectLs2,rectLs3,rectLs4
    rectLs1 = reservedRect[0]
    rectLs2 = reservedRect[1]
    rectLs3 = reservedRect[2]
    rectLs4 = reservedRect[3]
    main(state)

def main(state):
    Reserved_rect = [rectLs1.copy(),rectLs2.copy(),rectLs3.copy(),rectLs4.copy()]
    # empty lists for storing and updating rectangular objects
    ls1 = [x for x in range(12)]
    ls2 = [x for x in range(12)]
    ls3 = [x for x in range(12)]
    ls4 = [x for x in range(12)] # for upating rect obj of rectLs4

    clock = pygame.time.Clock()
    WHITE = (225,225,225)
    BLACK = (0,0,0)
    red = (255,130,71)
    red1 = (127,255,212)
    WIDTH,HEIGHT = 800,600
    score = 0
    Lives = 4
    #slider bar paramaters
    x,y = 370,520
    vel = 5
    #moving ball parameters
    x_ball = 400
    y_ball = 500
    x_speed = random.uniform(1.3,2.5)
    y_speed = random.uniform(3.3,4.7)

    #button check
    play_btn = False
    ext_btn = False

    #function for displaying game over
    def livescount(Lives):
        font = pygame.font.SysFont('impact',20)
        text = font.render("Lives x " + str(Lives),True,BLACK)
        screen.blit(text,(50,20))
    def Score(score):
        font = pygame.font.SysFont('impact',20)
        text = font.render("Score x " + str(score),True,BLACK)
        screen.blit(text,(640,20))
        
    def gameOver():
        font = pygame.font.SysFont('bauhaus93',36)
        text = font.render("GAME OVER",True,BLACK)
        txtRect = pygame.draw.rect(screen,red,[300,260,200,50],width = 5,border_radius = 7)
        screen.blit(text,(310,265))
        

    #function for displaying game over
    def playAgain():
        font = pygame.font.SysFont('bauhaus93',34)
        text = font.render("PLAY AGAIN",True,BLACK)
        txtRect = pygame.draw.rect(screen,red,[300,320,200,50],width = 5,border_radius = 7)
        screen.blit(text,(317,325))
           

    #function for displaying game over
    def exit_btn():
        global run
        font = pygame.font.SysFont('bauhaus93',36)
        text = font.render("EXIT",True,BLACK)
        txtRect = pygame.draw.rect(screen,red,[300,380,200,50],width = 5,border_radius = 7)
        screen.blit(text,(360,385))
        
    # function for bouncing ball
    def bouncing_ball(ball,slider):
        nonlocal x_speed,y_speed,y_ball,x_ball,Lives
        if x_ball < 20 or x_ball>740:
            x_speed *= -1
        if y_ball <70 :
            y_speed *= -1
        if y_ball > 600:
            y_ball = 170
            Lives -= 1
        # collision check of ball and lower slider
        collision_tolerance = 10
        if ball.colliderect(slider):
            if abs(slider.top - ball.bottom) <  collision_tolerance :
                y_speed *= -1
            if abs(slider.right - ball.left) <  collision_tolerance :
                x_speed *= -1
            if abs(slider.left - ball.right) <  collision_tolerance :
                x_speed *= -1
                
    #funcction for returing boxes that got hit by ball so that they can be removed            
    def brickBreak(ball_that_hit,list_of_rect_obj):
        nonlocal y_speed,score
        collision_tolerance = 10
        for i in range(len(list_of_rect_obj)):
            rect_obj = list_of_rect_obj[i]
            if ball_that_hit.colliderect(rect_obj):
                if abs(rect_obj.bottom - ball_that_hit.top) <  collision_tolerance :
                    y_speed *= -1
                    score +=10
                    return rect_obj
    #function for creating updated lists with rectangle objects and drawing boxes
    def lsUpdate(listToUpdate,ls):
        for i in range(len(listToUpdate)):
            r_obj = pygame.draw.rect(screen, red, listToUpdate[i])
            ls[i] = r_obj
    #function for updating lists with rectangle objects after collision
    def collisionUpdate(rect_got_hit,rect_obj_list,main_list):
        if rect_got_hit in rect_obj_list:
            rect_obj_list.remove(rect_got_hit)
            main_list.remove(list(rect_got_hit)) # removal form main list
       
    while state:
        clock.tick(120)
        pygame.display.set_caption("Brick Game In Pygame !")
        screen = pygame.display.set_mode((WIDTH,HEIGHT))
        screen.fill(WHITE)

        #for updating empty lists with rect objs
        lsUpdate(rectLs4,ls4)
        lsUpdate(rectLs3, ls3)
        lsUpdate(rectLs2, ls2)
        lsUpdate(rectLs1, ls1)
        livescount(Lives)
        Score(score)
        # slider controlling setup using pygame
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_LEFT] and x>20:
            x -= vel
        if keys[pygame.K_RIGHT] and x<730:
            x += vel    
        # ball movement parameters controls       
        x_ball += x_speed
        y_ball += y_speed
        #mouse button tapping
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] >300 and mouse_pos[0]<500:
            if mouse_pos[1] > 320 and mouse_pos[1]<370:
                if pygame.mouse.get_pressed()[0]:
                    play_btn = True
                else:
                    if play_btn:
                        gamestate(Reserved_rect)
                        play_btn = False
            if mouse_pos[1] > 380 and mouse_pos[1]<430:
                if pygame.mouse.get_pressed()[0]:
                    ext_btn =  True
                else:
                    if ext_btn:
                        pygame.quit()
                        ext_btn = False
        #rendering ball and slider
        ball = pygame.draw.circle(screen,BLACK,(x_ball,y_ball),10)
        slider = pygame.draw.rect(screen,red,[x,y,80,10])
        if Lives > 0:
            if rectLs1:
                #executing ball bouncing
                bouncing_ball(ball,slider)
                #execting rect that got hit functionality
                rct_gothit4 = brickBreak(ball,ls4)
                rct_gothit3 = brickBreak(ball,ls3)
                rct_gothit2 = brickBreak(ball,ls2)
                rct_gothit1 = brickBreak(ball,ls1)
                #removing hitted rectangles form game
                collisionUpdate(rct_gothit4,ls4,rectLs4)
                collisionUpdate(rct_gothit3,ls3,rectLs3)
                collisionUpdate(rct_gothit2,ls2,rectLs2)
                collisionUpdate(rct_gothit1,ls1,rectLs1)
            
            else:
                gameOver()
                playAgain()
                exit_btn()
        else:
            gameOver()
            playAgain()
            exit_btn()
            
        pygame.display.update()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False

main(state)
