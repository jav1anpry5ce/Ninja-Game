import pygame
import sys
import math
import time

class Player(object):
    def __init__(self):
        self. x = 0
        self.y = 0
        self.height = 64
        self.width = 50
        self.rect = pygame.Rect(260, 800, self.width, self.height)
        self.left = False
        self.right = False
        self.attacking = False
        self.speed = 6
        self.vertical_momentum = 0
        self.air_timer = 0
        self.walk_count = 0
        self.movement = [self.x, self.y]
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
        self.attackleft = [pygame.image.load('Asset/Ninja/Attackleft__000.png'), pygame.image.load('Asset/Ninja/Attackleft__001.png'), pygame.image.load('Asset/Ninja/Attackleft__002.png'),
        pygame.image.load('Asset/Ninja/Attackleft__003.png'), pygame.image.load('Asset/Ninja/Attackleft__004.png'), pygame.image.load('Asset/Ninja/Attackleft__005.png'),
        pygame.image.load('Asset/Ninja/Attackleft__006.png'), pygame.image.load('Asset/Ninja/Attackleft__007.png'), pygame.image.load('Asset/Ninja/Attackleft__008.png'),
        pygame.image.load('Asset/Ninja/Attackleft__009.png')]
        self.loop = 0
        self.idle = pygame.image.load('Asset/Ninja/Idle__001.png')
        self.standing_right = False
        self.image = self.idle

    def movearound(self):
        self.movement = [self.x, self.y]
        if self.walk_count + 1 > 27:
            self.walk_count = 0

        if self.right:
            self.walk_count += 1
            self.image = self.run_right[self.walk_count // 3]
            self.movement[0] += self.speed
            self.standing_right = True

        elif self.left:
            self.walk_count += 1
            self.image = self.run_left[self.walk_count // 3]
            self.movement[0] -= self.speed
            self.standing_right = False
        else:
            self.movement[0] = 0
            if self.standing_right:
                self.image = self.idle
            else:
                self.image = pygame.transform.flip(self.idle, True, False)
        self.movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.4
        if self.vertical_momentum >= 6:
            self.vertical_momentum = 13

    def attackk(self):
        pygame.time.delay(20)
        if self.attacking:
            self.loop += 1
            if self.standing_right:
                self.image = self.attackright[self.loop - 1]
            else:
                self.image = self.attackleft[self.loop - 1]
            if self.loop >= 10:
                self.loop = 0
                self.attacking = False
                self.image = self.idle
