# -*- coding: utf-8 -*-
# import pygame, sys
#
# pygame.init()
# screen = pygame.display.set_mode([640,480])
# screen.fill([255,255,255])
#
# pygame.draw.circle(screen,[255,0,0],[200,100],30,10)
# pygame.display.flip()
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()


import pygame, sys, random
from pygame.color import THECOLORS

pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range(100):
    width = random.randint(0,250)
    height = random.randint(0,100)
    top = random.randint(0,400)
    left = random.randint(0,500)

    color_name = random.choice(THECOLORS.keys())    # 随机生成100个矩形，大小随机，颜色随机
    color = THECOLORS[color_name]
    line_width = random.randint(1,3)
    pygame.draw.rect(screen, color, [left, top, width, height], line_width)
    # pygame.draw.rect(screen, [0,0,0], [left, top, width, height], 1)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()