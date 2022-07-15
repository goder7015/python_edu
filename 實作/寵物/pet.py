import pygame
import sys
import os
import random
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

alive = 1

pygame.init()
screen = pygame.display.set_mode([1000, 600])
screen.fill([255, 255, 255])

pet_images = ['normal.png', 'sleep.png',
              'happy.png', 'sad.png', 'eat.png', 'play.png']
ball_image = ['ball.png']
night_image = ['night.png']
food_image = ['food.png']


class PetClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pet_images[0])
        self.rect = self.image.get_rect()
        self.rect.center = [500, 350]
        self.angle = 0


class BallClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('ball.png')
        self.rect = self.image.get_rect()
        #self.rect.center = [270, 120]
        self.angle = 0


class NightClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('night.png')
        self.rect = self.image.get_rect()
        #self.rect.center = [570, 120]
        self.angle = 0


class FoodClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('food.png')
        self.rect = self.image.get_rect()
        #self.rect.center = [870, 120]
        self.angle = 0


def update_object(object):
    screen.blit(object.image, object.rect)
    pygame.display.flip()


def update_all():
    update_object(pet)
    update_object(ball)
    update_object(night)
    update_object(food)


def chk_happy():
    if status['happy'] < 3 or status['hungry'] < 3 or status['sleep'] < 3 or status['hp'] < 3:
        pet.image = pygame.image.load(pet_images[3])
    elif status['happy'] > 7:
        pet.image = pygame.image.load(pet_images[2])    
    else:
        pet.image = pygame.image.load(pet_images[0])
    update_all()


def chk_status():
    global alive
    if status['sleep'] <= 1:
        status['hp'] -= 1
    if status['happy'] <= 1:
        status['hungry'] -= 1
        status['sleep'] += 1
    if status['hp'] == 0:
        alive = 0
    if status['hungry'] <= 1:
        status['hp'] -= 1
    if status['sleep'] >= 10 and status['hungry'] >= 10:
        status['hp'] += 1


pet = PetClass()
ball = BallClass()
ball.rect.center = [250, 120]
night = NightClass()
night.rect.center = [500, 120]
food = FoodClass()
food.rect.center = [750, 120]

status = {'hungry': 10, 'happy': 10, 'hp': 10, 'sleep': 10}

timer = 0

update_all()

while 1:
    timer += 1
    if timer == 10000:
        timer = 0
        status['happy'] -= 1
        status['hungry'] -= 1
        status['sleep'] -= 1
        chk_status()
        chk_happy()
        update_all()
    print(timer, status)
    for event in pygame.event.get():
        if alive == 0:
            messagebox.showinfo('Your pet is leaving!', 'OK')
            pygame.quit()

        if status['happy'] > 10:
            status['happy'] = 10

        if status['happy'] < 1:
            status['happy'] = 1

        if status['hungry'] > 10:
            status['hungry'] = 10

        if status['hungry'] < 1:
            status['hungry'] = 1

        if status['sleep'] > 10:
            status['sleep'] = 10

        if status['sleep'] < 1:
            status['sleep'] = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

            if event.key == pygame.K_f:
                pet.image = pygame.image.load(pet_images[4])
                update_all()
                status['hungry'] += 3
                status['sleep'] -= 1
                pygame.time.delay(3000)

            if event.key == pygame.K_g:
                pet.image = pygame.image.load(pet_images[5])
                update_all()
                status['hungry'] -= 2
                status['sleep'] -= 2
                status['happy'] += 3
                pygame.time.delay(3000)

            if event.key == pygame.K_h:
                pet.image = pygame.image.load(pet_images[1])
                update_all()
                status['hungry'] -= 1
                status['sleep'] += 3
                status['happy'] += 1
                pygame.time.delay(3000)

            chk_happy()

pygame.quit()
