import sys, pygame
from time import sleep
import math
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
bird = pygame.image.load(r"C:\Users\tjw\Pictures\frame-1.png")
bird = pygame.transform.scale(bird, (50,42))
for i in range(300):
    screen.fill((0,0,0))
    screen.blit(bird, (width//2, height//2 + height//3 * math.sin(i*2*math.pi/30)))
    pygame.display.flip()
    sleep(1./30)

pygame.quit()
