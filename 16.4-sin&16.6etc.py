# -*- coding: utf-8 -*-
import pygame, sys
import math
pygame.init()
plotPoints = []
screen = pygame.display.set_mode([640,480])
# screen = pygame.display.set_mode([800,600])
screen.fill([255,255,255])

# 16.4
# for x in range(0,640):
#     y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
#     plotPoints.append([x,y])
# #    pygame.draw.rect(screen, [0,0,0], [x,y,1,1], 1)
# pygame.draw.lines(screen, [0,0,0], False, plotPoints,1)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 16.6 移动一下
# peo = pygame.image.load('skier_down.png')
# screen.blit(peo,[50,50])
# pygame.display.flip()
# pygame.time.delay(2000)
# screen.blit(peo,[150,50])
# pygame.draw.rect(screen,[255,255,255],[50,50,90,90],0)  #擦掉
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 16.8 更流畅
# peo = pygame.image.load('skier_down.png')
# x = 50
# y = 50
#
# screen.blit(peo,[x,y])
# pygame.display.flip()
# for looper in range(1,100):
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x = x + 5
#     screen.blit(peo,[x,y])
#     pygame.display.flip()
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 16.9 反弹！
# peo = pygame.image.load('skier_down.png')
# x = 50
# y = 50
# x_speed = 1
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x = x + x_speed
#     if x < 0 or x > screen.get_width() - 30:
#         x_speed =  -x_speed
#     screen.blit(peo,[x,y])
#     pygame.display.flip()
# pygame.quit()

# 2D反弹!
# peo = pygame.image.load('skier_down.png')
# x = 50
# y = 50
# x_speed = 5
# y_speed = 6
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 30, 64], 0)
#     x = x + x_speed
#     y = y + y_speed
#     if x < 0 or x > screen.get_width() - 30:
#         x_speed =  -x_speed
#     if y < 0 or y > screen.get_height() - 64:
#         y_speed =  -y_speed
#     screen.blit(peo,[x,y])
#     pygame.display.flip()
# pygame.quit()

# 16.10 穿越
peo = pygame.image.load('skier_down.png')
x = 50
y = 50
x_speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 30, 64], 0)
    x = x + x_speed
    if x > screen.get_width() :
        x = -30
    screen.blit(peo,[x,y])
    pygame.display.flip()
pygame.quit()