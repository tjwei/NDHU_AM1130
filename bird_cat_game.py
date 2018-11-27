import pygame, sys
import numpy as np
import time

size = width, height = 800, 600

pygame.init()
screen = pygame.display.set_mode(size)
bird_imgs = []
cat = pygame.image.load('Pictures\\cat_white-32x32.png')
for i in range(1, 5):
    bird = pygame.image.load("Pictures\\frame-{}.png".format(i))
    bird = pygame.transform.scale(bird, (40,40))
    bird_imgs.append(bird)
x, y = 400, 300
x_speed = 0
y_speed = 0
ticks0 = pygame.time.get_ticks()
last_ticks = ticks0
cat_numbers = 70
cat_positions = np.random.randint(0, 599, size=cat_numbers)
cat_birthday = last_ticks+np.random.randint(0, 50, size=cat_numbers)*100
font = pygame.font.Font(None, 60)
font_big = pygame.font.Font(None, 180)
life = 1000
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:           
                pygame.quit()
                sys.exit()
            inc_speed = [1, -1][event.type == pygame.KEYUP]
            if event.key == pygame.K_UP:
                y_speed -= inc_speed
            if event.key == pygame.K_DOWN:
                y_speed += inc_speed
            if event.key == pygame.K_LEFT:
                x_speed -= inc_speed
            if event.key == pygame.K_RIGHT:
                x_speed += inc_speed
    current_ticks = pygame.time.get_ticks()
    distance = (current_ticks-last_ticks)*0.15
    y += y_speed*distance
    x += x_speed*distance
    x = min(max(50, x), 750)
    y = min(max(50, y), 550)
    screen.fill((100,100,255))
    bird_wing_state = (current_ticks//250)%4       
    screen.blit(bird_imgs[bird_wing_state], (int(x),int(y)))
    hit = False
    for i in range(cat_numbers):
        age = current_ticks-cat_birthday[i]
        y_pos = int(cat_positions[i])
        cat_state = (age//150)%3
        x_pos = int(age//10)%800
        screen.blit(cat, (x_pos,y_pos), area=(cat_state*32,0,32,32))
        if (x_pos-x)**2 + (y_pos-y)**2 < 25**2:
            life -=1
            hit =True
    if hit:
        pygame.draw.circle(screen, (255,0,0), 
                           (int(x)+20,int(y)+20),
                           20, 5)
    live_secs = (current_ticks-ticks0)/1000
    text = font.render("{:.1f}".format(live_secs), True, (255, 255, 170))
    screen.blit(text, (100,0))
    text = font.render("{:04d}".format(life), True, (255, 190, 190))
    screen.blit(text, (600,0))
    pygame.display.flip()
    last_ticks=current_ticks
    if life <=0:
        life=1000
        text = font_big.render("Game Over", True, (255, 100, 100))
        screen.blit(text, (100,200))
        pygame.display.flip()
        time.sleep(10)
        pygame.quit()
        sys.exit()
        



    
        
            
            
    


