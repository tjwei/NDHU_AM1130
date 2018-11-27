import pygame, sys
import numpy as np
import time

size = width, height = 800, 600

pygame.init()
screen = pygame.display.set_mode(size)
x, y = 400, 300
x_speed = 0
y_speed = 0
ticks0 = pygame.time.get_ticks()
last_ticks = ticks0
font = pygame.font.Font(None, 60)
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
    screen.fill((100,100,255))
    pygame.draw.circle(screen, (255,0,0), 
                        (int(x)+20,int(y)+20),
                           20, 5)
    live_secs = (current_ticks-ticks0)/1000
    text = font.render("{:.1f}".format(live_secs), True, (255, 255, 170))
    screen.blit(text, (100,0))    
    pygame.display.flip()
    last_ticks=current_ticks
        



    
        
            
            
    


