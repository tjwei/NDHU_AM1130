import sys, pygame
from time import sleep
import math
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
birds = []
for i in range(1, 9):
    #bird = pygame.image.load(r"C:\Users\tjw\Pictures\frame-%d.png"%i)
    bird = pygame.image.load(r"C:\Users\tjw\Pictures\frame-{}.png".format(i))
    bird = pygame.transform.scale(bird, (50,42))
    birds.append(bird)
    
bird_x = width//2-140
bird_y0 = height//2
running = True
i0 = i = 0

while running:       
    screen.fill((0,0,0))
    bird_y = (i-i0-9)**2/2 + bird_y0 - 30
    screen.blit(birds[abs( (i//3)%15-7)], (bird_x, bird_y ))
    pygame.display.flip()
    sleep(1./30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            bird_y0 = bird_y
            i0 = i
    i+=1
pygame.quit()
