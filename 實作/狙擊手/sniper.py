import random
import pygame
pygame.init()
# pygame開始

screen = pygame.display.set_mode((512, 512))
# 設定螢幕大小

scope = pygame.image.load("scope.png")
target = pygame.image.load("target.png")
# 載入圖片

sx = 194
sy = 194
# 準心的位置

tx = random.randint(64, 192)
ty = random.randint(64, 192)
# 標靶的座標隨機產生

tx_change = 0
ty_change = 0
# 標靶的移動，不是準心移動喔!

while True:
    screen.fill((145, 200, 255))

    screen.blit(target, (tx, ty))
    screen.blit(scope, (sx, sy))
    # 將兩個物品的圖片資料貼上到相對座標

    trect = pygame.draw.circle(screen, (0, 255, 0), (256, 256, 10, 10))
    srect = pygame.draw.rect(screen, (255, 0, 0), (tx + 60, ty + 60, 10, 10))
    # 增加可以碰撞的圖形

    tx_change = 0
    ty_change = 0

    for event in pygame.event.get():
        # 按鍵事件

        pygame.mouse.set_pos(256, 256)

        mouse = pygame.mouse.get_rel()

        tx_change -= mouse[0]
        ty_change -= mouse[1]

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and srect.colliderect(trect):
            tx = random.randint(50, 550)
            ty = random.randint(50, 550)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            pygame.display.update()

    tx += tx_change
    ty += ty_change

    pygame.display.update()
