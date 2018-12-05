# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:17:57 2018

@author: tjw
"""

import pygame
import sys
import random

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
font_score = pygame.font.Font(None, 140)
hit_effect = pygame.mixer.Sound('sfx_exp_odd7.wav')
dead_effect = pygame.mixer.Sound('sfx_exp_odd2.wav')




ball = Item(400, 300, 10, random.choice([-1, 1]), random.uniform(-1,1))
board = Item(700, 300, 60, 0, 0)
enemy = Item(100, 300, 60, 0, 0)


ticks0 = pygame.time.get_ticks()
last_ticks = ticks0
score = [0, 0]
pause_ticks = 1000
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
    # 玩家位置更新
    x, y = board.next_pos(diff_ticks)
    if y > HEIGHT:
        y = HEIGHT-1
    if y<=0:
        y = 0
    board.x, board.y = x, y   
    
    # 簡單的敵人邏輯
    predict_y = ball.y
    # 線性敵人邏輯
    predict_y = ball.y + ball.y_speed/ball.x_speed*(enemy.x-ball.x)
    # 隨機敵人變化
    predict_y += random.uniform(-enemy.r*0.8,enemy.r*0.8)
    
    if predict_y > enemy.y:
        enemy.y_speed = 1
    elif predict_y < enemy.y:
        enemy.y_speed = -1
            
    # 敵人位置更新
    x, y = enemy.next_pos(diff_ticks)
    if y > HEIGHT:
        y = HEIGHT-1
    if y<=0:
        y = 0
    enemy.x, enemy.y = x, y 
    
    x, y = ball.next_pos(diff_ticks)    

    # 玩家擊球判斷
    if board.x>=x>=board.x-5 and \
       board.y+board.r>=y>=board.y-board.r and \
       ball.x_speed>0:
        ball.x_speed=-ball.x_speed
        ball.y_speed = 1 if ball.y_speed>0 else -1
        ball.y_speed = ball.y_speed + (ball.y-board.y)/board.r
        hit_effect.play()
        
    # 敵人擊球判斷
    if enemy.x<=x<=enemy.x+5 and \
       enemy.y+enemy.r>=y>=enemy.y-enemy.r and \
       ball.x_speed<0:
        ball.x_speed=-ball.x_speed
        ball.y_speed = 1 if ball.y_speed>0 else -1
        ball.y_speed = ball.y_speed + (ball.y-enemy.y)/enemy.r
        hit_effect.play()
        
    # 球的邊界判斷
    if x>=WIDTH:
        score[1]+=1        
        ball = Item(400, 300, 10, -1, random.uniform(-1,1))
        #x, y = ball.pos()
        pause_ticks = 1000
        dead_effect.play()
        
    if x<0:
        score[0]+=1
        ball = Item(400, 300, 10, 1, random.uniform(-1,1))
        #x, y = ball.pos()
        pause_ticks = 1000
        dead_effect.play()
        
    if y>=HEIGHT:
        y = HEIGHT-1
        ball.y_speed = -ball.y_speed
    if y<=0:
        y = 0
        ball.y_speed = -ball.y_speed
    
    if pause_ticks>0:
        pause_ticks-=diff_ticks
    else:
        ball.x, ball.y = x, y
    
    # 清空螢幕 開始畫圖
    screen.fill((128,0,128))
    # 印出分數
    score1 = font_score.render("{:02d}".format(score[0]), True, (255, 170, 170))
    score1_rect = score1.get_rect(center=(550, 100))
    screen.blit(score1, score1_rect)
    score2 = font_score.render("{:02d}".format(score[1]), True, (255, 170, 170))
    score2_rect = score2.get_rect(center=(250, 100))
    screen.blit(score2, score2_rect)
    pygame.draw.circle(screen, (0,255,0), ball.pos(), ball.r, 4)
    # 把玩家的板子畫出
    x, y = board.pos()    
    pygame.draw.rect(screen, (255,255,255), 
                     (x-5,y-board.r,10,2*board.r), 4)
    # 把敵人的板子畫出
    #enemy.y = board.y
    x, y = enemy.pos()    
    pygame.draw.rect(screen, (255,255,255), 
                     (x-5,y-enemy.r,10,2*enemy.r), 4)
    pygame.display.flip()
    last_ticks = ticks
pygame.quit()


