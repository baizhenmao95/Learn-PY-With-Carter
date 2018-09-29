# -*- coding: utf-8 -*-
import pygame
from random import *
pygame.init()
screen = pygame.display.set_mode([640,480])
backgroup = pygame.Surface(screen.get_size())
backgroup .fill ([255,255,255])

class MyBallClass(pygame.sprite.Sprite):   # 定义一个我的球类，用了继承，继承了动画精灵
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:    # 左右反弹
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 :                               # 顶部反弹
            self.speed[1] = -self.speed[1]
            global score, score_font, score_surf
            score = score + 1
            score_surf = score_font.render(str(score), 1, (0,0,0))


class MyPaddleClass(pygame.sprite.Sprite):   # 创建一个球拍类，也继承了动画精灵
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,10])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# 参数初始化
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill ([255,255,255])
img_file = "skier_flag.png"
ball_speed = [4,5]
my_ball = MyBallClass(img_file, [50,100], ball_speed)
ballGroup = pygame.sprite.Group(my_ball)
paddle = MyPaddleClass([270,450])
global score
score = 0
score_font = pygame.font.Font(None, 50)
score_surf = score_font.render(str(score), 1, (0,0,0))
score_pos = [10,10]
done = False
lives = 3

# 主循环开始
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:  # 底部挡板随鼠标左右移动
            paddle.rect.centerx = event.pos[0]
#            paddle.rect.center = event.pos
#        elif event.type == pygame.USEREVENT:
#            my_ball.rect.centery = my_ball.rect.centery + (30*direction)
#             if my_ball.rect.top <= 0 or my_ball.rect.bottom >= screen.get_rect().bottom:
#                 direction = -direction
#    clock.tick(30)
    pygame.time.delay(20)
    screen.blit(backgroup,(0,0))
    my_ball.move()

    if not done:
        screen.blit(my_ball.image, my_ball.rect)
        screen.blit(paddle.image, paddle.rect)
        screen.blit(score_surf, score_pos)
        for i in range(lives):
            width = screen.get_rect().width
            screen.blit(my_ball.image, [width - 40 * i, 20])
    # 如果碰到长杆，反弹
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
    #    my_ball.speed[0] = -my_ball.speed[0]
        my_ball.speed[1] = -my_ball.speed[1]
#        score = score + 1
#        score_surf = score_font.render(str(score), 1, (0, 0, 0))
    #
    if my_ball.rect.top >= screen.get_rect().bottom:
        lives = lives - 1
        if lives ==  0:   # 如果用光三条命就 game over
            final_text1 = "Game Over"
            final_text2 = "Your final score is:   " + str(score)
            ft1_font = pygame.font.Font(None, 70)
            ft1_surf = ft1_font.render(final_text1, 1, (0,0,0))
            ft2_font = pygame.font.Font(None, 50)
            ft2_surf = ft2_font.render(final_text2, 1, (0, 0, 0))
            screen.blit(ft1_surf, [screen.get_width()/2 - \
                               ft1_surf.get_width()/2,100])
            screen.blit(ft2_surf, [screen.get_width() / 2 - \
                               ft2_surf.get_width() / 2, 200])
            pygame.display.flip()
            done = True
        else:
            # score = 0   # 若没接住则得分清零，暂且不用
            # score_surf = score_font.render(str(score), 1, (0, 0, 0))
            pygame.time.delay(2000)
            my_ball.rect.topleft = [50,50]
    pygame.display.flip()
pygame.quit()