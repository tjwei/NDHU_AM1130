# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:17:57 2018

@author: tjw
"""

import pygame
import sys

WIDTH, HEIGHT = 800, 600
XS, YS = 200/1000, 200/1000

class Item:
    def __init__(self, x, y, r, x_speed, y_speed):
        self.x = x
        self.y = y
        self.r = r
        self.x_speed = x_speed
        self.y_speed = y_speed
    def pos(self):
        return (int(self.x), int(self.y))
    def next_pos(self, diff_ticks):
        x, y = self.x, self.y
        x = x + self.x_speed * XS * diff_ticks 
        y = y + self.y_speed * YS * diff_ticks
        return x,y
    

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

ball = Item(400, 300, 10, 1, 1)
board = Item(700, 300, 60, 0, 0)

ticks0 = pygame.time.get_ticks()
last_ticks = ticks0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                board.y_speed -= 1
            if event.key == pygame.K_DOWN:
                board.y_speed += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                board.y_speed += 1
            if event.key == pygame.K_DOWN:
                board.y_speed -= 1
    ticks = pygame.time.get_ticks()
    diff_ticks = ticks - last_ticks
        
    x, y = board.next_pos(diff_ticks)
    if y > HEIGHT:
        y = HEIGHT-1
    if y<=0:
        y = 0
    board.x, board.y = x, y    
    
    x, y = ball.next_pos(diff_ticks)    
    if y>=HEIGHT:
        y = HEIGHT-1
        ball.y_speed = -ball.y_speed
    if board.x>=x>=board.x-5 and \
       board.y+board.r>=y>=board.y-board.r and \
       ball.x_speed>0:
        ball.x_speed=-ball.x_speed
        ball.y_speed = 1 if ball.y_speed>0 else -1
        ball.y_speed = ball.y_speed + (ball.y-board.y)/board.r
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
    pygame.draw.circle(screen, (0,255,0), ball.pos(), ball.r, 4)
    x, y = board.pos()    
    pygame.draw.rect(screen, (255,255,255), 
                     (x-5,y-board.r,10,2*board.r), 4)
    pygame.display.flip()
    last_ticks = ticks
pygame.quit()


