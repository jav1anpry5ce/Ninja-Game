import pygame
import sys
import math
import time
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, rectx, recty):
        self.rectx = rectx
        self.recty = recty
        self.width = 50
        self.height = 58
        self.health = 10
        self.rect = pygame.Rect(self.rectx, recty, self.width, self.height)
        self.x = self.rect.x
        self.y = 0
        self.left = True
        self.right = False
        self.walking = True
        self.attacking = False
        self.speed = 2
        self.walk_count = 0
        self.attack_count = 0
        self.movement = [0,0]
        self.vertical = 0
        self.walkright = [pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_000.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_001.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_002.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_003.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_004.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_005.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_006.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_007.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_008.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_009.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_010.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_011.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_012.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_013.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_014.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_015.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_016.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_017.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_018.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_walk_019.png')]
        self.walkleft = [pygame.transform.flip(self.walkright[0], True, False), pygame.transform.flip(self.walkright[1], True, False), pygame.transform.flip(self.walkright[2], True, False), pygame.transform.flip(self.walkright[3], True, False),
        pygame.transform.flip(self.walkright[4], True, False), pygame.transform.flip(self.walkright[5], True, False), pygame.transform.flip(self.walkright[6], True, False), pygame.transform.flip(self.walkright[7], True, False),
        pygame.transform.flip(self.walkright[8], True, False), pygame.transform.flip(self.walkright[9], True, False), pygame.transform.flip(self.walkright[10], True, False), pygame.transform.flip(self.walkright[11], True, False),
        pygame.transform.flip(self.walkright[12], True, False), pygame.transform.flip(self.walkright[13], True, False), pygame.transform.flip(self.walkright[14], True, False), pygame.transform.flip(self.walkright[15], True, False),
        pygame.transform.flip(self.walkright[16], True, False), pygame.transform.flip(self.walkright[17], True, False), pygame.transform.flip(self.walkright[18], True, False), pygame.transform.flip(self.walkright[19], True, False)]
        self.attackright = [pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_000.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_001.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_002.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_003.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_004.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_005.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_006.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_007.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_008.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_009.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_010.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_011.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_012.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_013.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_014.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_015.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_016.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_017.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_018.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_attack_019.png')]
        self.attackleft = [pygame.transform.flip(self.attackright[0], True, False), pygame.transform.flip(self.attackright[1], True, False), pygame.transform.flip(self.attackright[2], True, False), pygame.transform.flip(self.attackright[3], True, False),
        pygame.transform.flip(self.attackright[4], True, False), pygame.transform.flip(self.attackright[5], True, False), pygame.transform.flip(self.attackright[6], True, False), pygame.transform.flip(self.attackright[7], True, False),
        pygame.transform.flip(self.attackright[8], True, False), pygame.transform.flip(self.attackright[9], True, False), pygame.transform.flip(self.attackright[10], True, False), pygame.transform.flip(self.attackright[11], True, False),
        pygame.transform.flip(self.attackright[12], True, False), pygame.transform.flip(self.attackright[13], True, False), pygame.transform.flip(self.attackright[14], True, False), pygame.transform.flip(self.attackright[15], True, False),
        pygame.transform.flip(self.attackright[16], True, False), pygame.transform.flip(self.attackright[17], True, False), pygame.transform.flip(self.attackright[18], True, False), pygame.transform.flip(self.attackright[19], True, False)]
        self.die = [pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_000.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_001.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_002.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_003.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_004.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_005.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_006.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_007.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_008.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_009.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_010.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_011.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_012.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_013.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_014.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_015.png'),
        pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_016.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_017.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_018.png'), pygame.image.load('Asset/Enemy/PNG/1/1_enemies_1_die_019.png')]
        self.image = self.walkright[0]
        self.deadani = 0
        self.died = False


    def movearound(self):
        self.movement = [0,0]
        self.movement[1] += self.vertical
        self.vertical += 0.4
        if self.vertical >= 6:
            self.vertical = 13
        if self.walk_count + 1 > 59:
            self.walk_count = -1
        if self.walking:
            if self.right:
                self.walk_count += 1
                self.image = self.walkright[self.walk_count // 3]
                self.movement[0] += self.speed
                self.x += self.speed
                self.left = False

            elif self.left:
                self.walk_count += 1
                self.image = self.walkleft[self.walk_count // 3]
                self.movement[0] -= self.speed
                self.x -= self.speed
                self.right = False

    def attack(self, x1, x2):
        self.distance = math.sqrt((math.pow(x2 - x1, 2)))
        if self.distance <= 30:
            self.attacking = True
            self.walking = False
            self.attack_count += 1
            if self.attack_count + 1 > 59:
                self.attack_count = -1
            if self.right:
                self.image = self.attackright[self.attack_count // 3]
            else:
                self.image = self.attackleft[self.attack_count // 3]
        else:
            self.attacking = False
            self.walking = True

    def dead(self):
        if self.died:
            self.walking = False
            self.attacking = False
            if self.deadani + 1 > 59:
                self.deadani = -1
            if self.died:
                self.deadani += 1
                self.image = self.die[self.deadani // 3]
