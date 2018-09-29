# # -*- coding: utf-8 -*-
# import pygame, sys
# from random import *
# class MyBallClass(pygame.sprite.Sprite):
#     def __init__(self, image_file, location, speed):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#
#         self.speed = speed
#     def move(self):
#         self.rect = self.rect.move(self.speed)
#         if self.rect.left < 0 or self.rect.right > width:
#             self.speed[0] = -self.speed[0]
#
#         if self.rect.top < 0 or self.rect.bottom > height:
#             self.speed[1] = -self.speed[1]
#
# size = width, height = 640, 480
# screen = pygame.display.set_mode(size)
# screen.fill ([255,255,255])
# img_file = "skier_down.png"
# balls = []
# for row in range (0,3):
#     for column in range (0,5):
#         location = [column * 180 + 10, row * 180 + 10]
#         speed = [choice([-2,2]), choice([-2,2])]
#         ball = MyBallClass(img_file, location,speed)
#         balls.append(ball)
# # for ball in balls:
# #     screen.blit(ball.image, ball.rect)
# # pygame.display.flip()
#
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     pygame.time.delay(20)
#     screen.fill([255,255,255])
#     for ball in balls:
#         ball.move()
#         screen.blit(ball.image, ball.rect)
#     pygame.display.flip()import sys,pygame
# from random import *
#
# class MyBallClass(pygame.sprite.Sprite):
#     def __init__(self,image_file,location,speed):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left,self.rect.top = location
#         self.speed = speed
#     def move(self):
#         self.rect = self.rect.move(self.speed)
#         if self.rect.left < 0 or self.rect.right > width:
#             self.speed[0] = - self.speed[0]
#
#         if self.rect.top < 0 or self.rect.bottom > height:
#             self.speed[1] = -self.speed[1]
#
# def animate(group):
#     screen.fill([255,255,255])
#     for ball in group:
#         group.remove(ball)
#         if pygame.sprite.spritecollide(ball,group,False):
#             ball.speed[0] = -ball.speed[0]
#             ball.speed[1] = -ball.speed[1]
#         group.add(ball)
#         ball.move()
#         screen.blit(ball.image,ball.rect)
#     pygame.display.flip()
#     pygame.time.delay(50)
# size = width,height = 640,480
# screen =pygame.display.set_mode(size)
# screen.fill([255,255,255])
# img_file = "skier_down.png"
# group = pygame.sprite.Group()
#
# for row in range (0,2):
#     for column in range (0,2):
#         location = [column *180 +10,row * 180 +10]
#         speed = [choice([-5,5]),choice([-5,5])]
#         ball = MyBallClass(img_file,location,speed)
#         group.add(ball)
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     animate(group)
# pygame.quit()
# pygame.quit()


# 17-3
import sys, pygame
from random import *


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
            self.speed[0] = - self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]


def animate(group):
    screen.fill([255, 255, 255])
    for ball in group:
        ball.move()
    for ball in group:
        group.remove(ball)
        if pygame.sprite.spritecollide(ball, group, False):
            ball.speed[0] = -ball.speed[0]
            ball.speed[1] = -ball.speed[1]
        group.add(ball)

        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
 #   pygame.time.delay(50)

clock = pygame.time.Clock()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
img_file = "skier_down.png"
group = pygame.sprite.Group()

for row in range(0, 2):
    for column in range(0, 2):
        location = [column * 180 + 10, row * 180 + 10]
        speed = [choice([-5, 5]), choice([-5, 5])]
        ball = MyBallClass(img_file, location, speed)
        group.add(ball)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            frame_rate = clock.get_fps()
            print "frame rate = ", frame_rate
    animate(group)
    clock.tick(30)
pygame.quit()
