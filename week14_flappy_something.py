import pygame
from time import sleep
#import math
import random
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
birds = []
for i in range(1, 9):
    #bird = pygame.image.load(r"C:\Users\tjw\Pictures\frame-%d.png"%i)
    bird = pygame.image.load(r"C:\Users\tjw\Pictures\frame-{}.png".format(i))
    bird = pygame.transform.scale(bird, (50,42))
    birds.append(bird)
    
pipe_top = pygame.image.load(r"C:\Users\tjw\Pictures\tube1.gif")
pipe_bottom = pygame.image.load(r"C:\Users\tjw\Pictures\tube2.gif")

bird_x = width//2-140
bird_y0 = height//2
running = True
i0 = i = 0
pipes = [(300,)] * 10
pipe_n = 0
while running:       
    screen.fill((0,0,0))
    pipe_x = width* (1 - i / 150.)
    for j in range(10):
        screen.blit( pipe_top, ( pipe_x+ (j+pipe_n)*width/3, pipes[j][0]-400) )
        screen.blit( pipe_bottom, ( pipe_x+ (j+pipe_n)*width/3, pipes[j][0]) )
    if pipe_x+ pipe_n*width/3 < -width/3:
        pipes.pop(0)
        pipes.append((random.randint(200, 600), ))
        pipe_n += 1
            
            
    
    bird_y = (i-i0-9)**2/2 + bird_y0 - 30
    screen.blit(birds[abs( (i//3)%15-7)], (bird_x, bird_y ))
    pygame.display.flip()
    sleep(1./30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y0 = bird_y
                i0 = i
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False

            
    i+=1
pygame.quit()
