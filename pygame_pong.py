# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:17:57 2018

@author: tjw
"""

import pygame
import sys

WIDTH, HEIGHT = 800, 600
XS, YS = 200/1000, 200/1000

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 20
        self.x_speed = 1
        self.y_speed = 1

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

ball = Ball(400, 300)
ticks0 = pygame.time.get_ticks()
last_ticks = ticks0
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
    x, y = ball.x, ball.y
    ticks = pygame.time.get_ticks()
    diff_ticks = ticks - last_ticks
    x = x + ball.x_speed * XS * diff_ticks 
    y = y + ball.y_speed * YS * diff_ticks 
    if y>=HEIGHT:
        y = HEIGHT-1
        ball.y_speed = -ball.y_speed
    if x>=WIDTH:
        x = WIDTH-1
        ball.x_speed = -ball.x_speed
    if y<=0:
        y = 0
        ball.y_speed = -ball.y_speed
    if x<=0:
        x = 0
        ball.x_speed = -ball.x_speed
    ball.x, ball.y = x, y
    screen.fill((128,0,128))
    pygame.draw.circle(screen, (0,255,0), 
                       (int(ball.x), int(ball.y)), ball.r, 4)
    pygame.display.flip()
    last_ticks = ticks
pygame.quit()


