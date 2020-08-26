import pygame
import sys
import math
import time

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.height = 64
        self.width = 50
        self.health = 100
        self.rect = pygame.Rect(256, 832, self.width, self.height)
        self.left = False
        self.right = False
        self.attacking = False
        self.throwattack = False
        self.speed = 6
        self.vertical_momentum = 0
        self.air_timer = 0
        self.movement = [0,0]
        self.jumping = False
        self.loop = 0
        self.animation = 0
        self.standing_right = True
        self.dead = False
        self.kunaispeed = 1
        self.run_right = [pygame.image.load('Asset/Ninja/Run__000.png'), pygame.image.load('Asset/Ninja/Run__001.png'), pygame.image.load('Asset/Ninja/Run__002.png'),
        pygame.image.load('Asset/Ninja/Run__003.png'),pygame.image.load('Asset/Ninja/Run__004.png'), pygame.image.load('Asset/Ninja/Run__005.png'),
        pygame.image.load('Asset/Ninja/Run__006.png'), pygame.image.load('Asset/Ninja/Run__007.png'), pygame.image.load('Asset/Ninja/Run__008.png'),
        pygame.image.load('Asset/Ninja/Run__009.png')]
        self.run_left = [pygame.transform.flip(self.run_right[0], True, False), pygame.transform.flip(self.run_right[1], True, False),
        pygame.transform.flip(self.run_right[2], True, False), pygame.transform.flip(self.run_right[3], True, False),
        pygame.transform.flip(self.run_right[4], True, False), pygame.transform.flip(self.run_right[5], True, False),
        pygame.transform.flip(self.run_right[6], True, False), pygame.transform.flip(self.run_right[7], True, False),
        pygame.transform.flip(self.run_right[8], True, False), pygame.transform.flip(self.run_right[9], True, False)]
        self.jump_move = [pygame.image.load('Asset/Ninja/Jump__000.png'), pygame.image.load('Asset/Ninja/Jump__001.png'), pygame.image.load('Asset/Ninja/Jump__002.png'), pygame.image.load('Asset/Ninja/Jump__003.png'),
        pygame.image.load('Asset/Ninja/Jump__004.png'), pygame.image.load('Asset/Ninja/Jump__005.png'), pygame.image.load('Asset/Ninja/Jump__006.png'), pygame.image.load('Asset/Ninja/Jump__007.png'),
        pygame.image.load('Asset/Ninja/Jump__008.png'), pygame.image.load('Asset/Ninja/Jump__009.png')]
        self.attackright = [pygame.image.load('Asset/Ninja/Attack__000.png'), pygame.image.load('Asset/Ninja/Attack__001.png'), pygame.image.load('Asset/Ninja/Attack__002.png'),
        pygame.image.load('Asset/Ninja/Attack__003.png'), pygame.image.load('Asset/Ninja/Attack__004.png'), pygame.image.load('Asset/Ninja/Attack__005.png'),
        pygame.image.load('Asset/Ninja/Attack__006.png'), pygame.image.load('Asset/Ninja/Attack__007.png'), pygame.image.load('Asset/Ninja/Attack__008.png'),
        pygame.image.load('Asset/Ninja/Attack__009.png')]
        self.attackleft = [pygame.transform.flip(self.attackright[0], True, False), pygame.transform.flip(self.attackright[1], True, False),
        pygame.transform.flip(self.attackright[2], True, False), pygame.transform.flip(self.attackright[3], True, False),
        pygame.transform.flip(self.attackright[4], True, False), pygame.transform.flip(self.attackright[5], True, False),
        pygame.transform.flip(self.attackright[6], True, False), pygame.transform.flip(self.attackright[7], True, False),
        pygame.transform.flip(self.attackright[8], True, False), pygame.transform.flip(self.attackright[9], True, False)]
        self.idle = [pygame.image.load('Asset/Ninja/Idle__000.png'), pygame.image.load('Asset/Ninja/Idle__001.png'), pygame.image.load('Asset/Ninja/Idle__002.png'), pygame.image.load('Asset/Ninja/Idle__003.png'),
        pygame.image.load('Asset/Ninja/Idle__004.png'), pygame.image.load('Asset/Ninja/Idle__005.png'), pygame.image.load('Asset/Ninja/Idle__006.png'), pygame.image.load('Asset/Ninja/Idle__007.png'),
        pygame.image.load('Asset/Ninja/Idle__008.png'), pygame.image.load('Asset/Ninja/Idle__009.png')]
        self.deadright = [pygame.image.load('Asset/Ninja/Dead__000.png'), pygame.image.load('Asset/Ninja/Dead__001.png'), pygame.image.load('Asset/Ninja/Dead__002.png'),
        pygame.image.load('Asset/Ninja/Dead__003.png'), pygame.image.load('Asset/Ninja/Dead__004.png'), pygame.image.load('Asset/Ninja/Dead__005.png'),
        pygame.image.load('Asset/Ninja/Dead__006.png'), pygame.image.load('Asset/Ninja/Dead__007.png'), pygame.image.load('Asset/Ninja/Dead__008.png'),
        pygame.image.load('Asset/Ninja/Dead__009.png')]
        self.deadleft = [pygame.transform.flip(self.deadright[0], True, False), pygame.transform.flip(self.deadright[1], True, False),
        pygame.transform.flip(self.deadright[2], True, False), pygame.transform.flip(self.deadright[3], True, False),
        pygame.transform.flip(self.deadright[4], True, False), pygame.transform.flip(self.deadright[5], True, False),
        pygame.transform.flip(self.deadright[6], True, False), pygame.transform.flip(self.deadright[7], True, False),
        pygame.transform.flip(self.deadright[8], True, False), pygame.transform.flip(self.deadright[9], True, False)]
        self.throwright = [pygame.image.load('Asset/Ninja/Throw__000.png'), pygame.image.load('Asset/Ninja/Throw__001.png'), pygame.image.load('Asset/Ninja/Throw__002.png'),
        pygame.image.load('Asset/Ninja/Throw__003.png'), pygame.image.load('Asset/Ninja/Throw__004.png'), pygame.image.load('Asset/Ninja/Throw__005.png'),
        pygame.image.load('Asset/Ninja/Throw__006.png'), pygame.image.load('Asset/Ninja/Throw__007.png'), pygame.image.load('Asset/Ninja/Throw__008.png'),
        pygame.image.load('Asset/Ninja/Throw__009.png')]
        self.throwleft = [pygame.transform.flip(self.throwright[0], True, False), pygame.transform.flip(self.throwright[1], True, False),
        pygame.transform.flip(self.throwright[2], True, False), pygame.transform.flip(self.throwright[3], True, False),
        pygame.transform.flip(self.throwright[4], True, False), pygame.transform.flip(self.throwright[5], True, False),
        pygame.transform.flip(self.throwright[6], True, False), pygame.transform.flip(self.throwright[7], True, False),
        pygame.transform.flip(self.throwright[8], True, False), pygame.transform.flip(self.throwright[9], True, False)]
        self.kunaiimg = pygame.image.load('Asset/Ninja/Kunai.png')
        self.kunai = pygame.Rect(self.rect.x, self.rect.y, 32, 6)


    def movearound(self):
        self.x = self.rect.x
        self.y = self.rect.y
        self.movement = [0,0]
        self.movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.4
        if self.vertical_momentum >= 9:
            self.vertical_momentum = 16

        if self.animation + 1 > 45:
            self.animation = 0

        if self.right:
            self.animation += 1
            self.image = self.run_right[self.animation // 5]
            self.movement[0] += self.speed
            self.standing_right = True


        elif self.left:
            self.animation += 1
            self.image = self.run_left[self.animation // 5]
            self.movement[0] -= self.speed
            self.standing_right = False

        else:
            self.movement[0] = 0
            if self.standing_right:
                self.animation += 1
                self.image = self.idle[self.animation // 5]
            else:
                self.animation += 1
                self.image = pygame.transform.flip(self.idle[self.animation // 5], True, False)


    def attack(self, scroll):
        if self.attacking:
            self.left = False
            self.right = False
            self.loop += 1
            if self.standing_right:
                self.image = self.attackright[self.loop // 5]
            else:
                self.image = self.attackleft[self.loop // 5]
            if self.loop + 1 > 45:
                self.loop = 0
                self.attacking = False
        if self.throwattack:
            self.left = False
            self.right = False
            self.loop += 1
            if self.standing_right:
                self.kunaiimg = pygame.transform.flip(self.kunaiimg, False, False)
                self.image = self.throwright[self.loop // 5]
                if self.loop >= 14:
                    self.kunai.x += 15
            else:
                self.image = self.throwleft[self.loop // 5]
                self.kunaiimg = pygame.transform.flip(self.kunaiimg, True, False)
                if self.loop >= 14:
                    self.kunai.x -= 15
            if self.loop + 1 > 45:
                self.loop = 0
                self.throwattack = False

        if self.throwattack == False:
            self.kunai.x = self.rect.x - scroll[0]
            self.kunai.y = self.rect.y - scroll[1] + 15


    def deadanimation(self):
        if self.health <= 0:
            self.dead = True

        else:
            self.dead = False

        if self.dead:
            self.attacking = False
            self.animation += 1
            if self.animation + 1 > 45:
                self.animation = 45
            if self.standing_right:
                self.image = self.deadright[self.animation // 5]
            else:
                self.image = self.deadleft[self.animation // 5]
