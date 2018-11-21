import pygame, sys
import numpy as np

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
last_ticks = pygame.time.get_ticks()
cat_numbers = 100
cat_positions = np.random.randint(0, 599, size=cat_numbers)
cat_birthday = last_ticks+np.random.randint(0, 50, size=cat_numbers)*100

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
    y = y+y_speed*(current_ticks-last_ticks)*0.1
    x = x+x_speed*(current_ticks-last_ticks)*0.1
    screen.fill((100,100,255))
    bird_wing_state = (current_ticks//250)%4       
    screen.blit(bird_imgs[bird_wing_state], (int(x),int(y)))
    for i in range(cat_numbers):
        age = current_ticks-cat_birthday[i]
        y_pos = int(cat_positions[i])
        cat_state = (age//150)%3
        x_pos = int(age//10)%800
        screen.blit(cat, (x_pos,y_pos), area=(cat_state*32,0,32,32))
    pygame.display.flip()
    last_ticks=current_ticks

    
        
            
            
    


