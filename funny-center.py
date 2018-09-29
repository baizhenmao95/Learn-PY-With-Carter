# -*- coding: utf-8 -*-
import pygame
from random import *
pygame.init()
screen = pygame.display.set_mode([640,480])
backgroup = pygame.Surface(screen.get_size())
backgroup .fill ([255,255,255])

class MyBallClass(pygame.sprite.Sprite):
    def __init__(self, image_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

class MyPaddleClass(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface([100,10])
        image_surface.fill([0,0,0])
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill ([255,255,255])
img_file = "skier_flag.png"
ball_speed = [4,5]
my_ball = MyBallClass(img_file, [50,100], ball_speed)
ballGroup = pygame.sprite.Group(my_ball)
paddle = MyPaddleClass([270,450])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
#            paddle.rect.centerx = event.pos[0]
            paddle.rect.center = event.pos
#        elif event.type == pygame.USEREVENT:
#            my_ball.rect.centery = my_ball.rect.centery + (30*direction)
#             if my_ball.rect.top <= 0 or my_ball.rect.bottom >= screen.get_rect().bottom:
#                 direction = -direction
#    clock.tick(30)
    pygame.time.delay(20)
    screen.blit(backgroup,(0,0))
    my_ball.move()
    if pygame.sprite.spritecollide(paddle, ballGroup, False):
    #    my_ball.speed[0] = -my_ball.speed[0]
        my_ball.speed[1] = -my_ball.speed[1]
    screen.blit(my_ball.image,my_ball.rect)
    screen.blit(paddle.image, paddle.rect)
    pygame.display.flip()
pygame.quit()