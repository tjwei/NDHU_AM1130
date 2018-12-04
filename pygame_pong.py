# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:17:57 2018

@author: tjw
"""

import pygame
import sys

WIDTH, HEIGHT = 800, 600

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

ball = Ball(400, 300)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.y -= 10
            if event.key == pygame.K_DOWN:
                ball.y += 10
        if event.type == pygame.MOUSEBUTTONDOWN:            
            ball.x, ball.y = pygame.mouse.get_pos()
    screen.fill((128,0,128))
    pygame.draw.circle(screen, (0,255,0), 
                       (ball.x, ball.y), 50, 10)
    pygame.display.flip()
pygame.quit()


