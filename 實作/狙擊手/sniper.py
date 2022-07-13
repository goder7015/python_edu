import random
import pygame
import os
import sys
import pygame.freetype
pygame.init()
# pygame開始

screen = pygame.display.set_mode((1024, 1024))
# 設定螢幕大小

scope = pygame.image.load("scope.png")
target = pygame.image.load("target.png")
# 載入圖片

sx = 448
sy = 448
# 準心的位置

tx = random.randint(64, 192)
ty = random.randint(64, 192)
# 標靶的座標隨機產生

reseter = 0

while True:
    pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
    reseter += 1
    if reseter == 500:
        reseter = 0
        pygame.mouse.set_pos(512, 512)
        # 每500次偵測重置一次滑鼠位置

    screen.fill((145, 200, 255))

    screen.blit(target, (tx, ty))
    screen.blit(scope, (sx, sy))
    # 將兩個物品的圖片資料貼上到相對座標

    trect = pygame.draw.circle(screen, (0, 255, 0), (512, 512), 10, 10)
    srect = pygame.draw.circle(screen, (255, 0, 0), (tx + 63, ty + 63), 10, 10)
    # 增加可以碰撞的圖形

    for event in pygame.event.get():
        # 按鍵事件

        mouse = pygame.mouse.get_rel()
        keys = pygame.key.get_pressed()
        # 滑鼠與鍵盤事件

        if event.type == pygame.MOUSEMOTION:
            tx += mouse[0]
            ty += mouse[1]
            # 移動滑鼠

        if pygame.mouse.get_pressed()[0] and srect.colliderect(trect):
            tx = random.randint(50, 950)
            ty = random.randint(50, 950)
            # 射中標靶

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                tx = random.randint(50, 950)
                ty = random.randint(50, 950)
                # 重置標靶 

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                # 離開遊戲
        
    pygame.display.update()
