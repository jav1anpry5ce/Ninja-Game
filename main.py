import pygame
import sys
import math
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

screen_size = (1000, 650)
screen = pygame.display.set_mode(screen_size, 0, 32)
true_scroll = [0,0]

class GameMap(object):
    def __init__(self):
        self.grass = pygame.image.load('Asset/Forrest/png/Tiles/2.png')
        self.dirt = pygame.image.load('Asset/Forrest/png/Tiles/5.png')
        self.bg = pygame.image.load("Asset/Forrest/png/BG/BG.png").convert()

    def load_map(self, path):
        f = open(path + '.txt','r')
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map

    def map1(self):
        screen.blit(self.bg, (0,0))
        self.game_map = self.load_map('map')
        self.tile_rects = []
        y = 0
        for layer in self.game_map:
            x = 0
            for tile in layer:
                if tile == '1':
                    screen.blit(self.dirt,(x*128 - scroll[0],y*128 - scroll[1]))
                if tile == '2':
                    screen.blit(self.grass,(x*128 - scroll[0],y*128 - scroll[1]))
                if tile != '0':
                    self.tile_rects.append(pygame.Rect(x*128,y*128,128,128))
                x += 1
            y += 1


class Player(object):
    def __init__(self):
        self. x = 0
        self.y = 0
        self.height = 64
        self.width = 50
        self.rect = pygame.Rect(260, 835, self.width, self.height)
        self.left = False
        self.right = False
        self.speed = 6
        self.vertical_momentum = 0
        self.air_timer = 0
        self.walk_count = 0
        self.movement = [self.x, self.y]
        self.run_right = [pygame.image.load('Asset/Ninja/Run__000.png'), pygame.image.load('Asset/Ninja/Run__001.png'), pygame.image.load('Asset/Ninja/Run__002.png'), pygame.image.load('Asset/Ninja/Run__003.png'),pygame.image.load('Asset/Ninja/Run__004.png'), pygame.image.load('Asset/Ninja/Run__005.png'), pygame.image.load('Asset/Ninja/Run__006.png'), pygame.image.load('Asset/Ninja/Run__007.png'), pygame.image.load('Asset/Ninja/Run__008.png'), pygame.image.load('Asset/Ninja/Run__009.png')]
        self.run_left = [pygame.transform.flip(self.run_right[0], True, False), pygame.transform.flip(self.run_right[1], True, False), pygame.transform.flip(self.run_right[2], True, False), pygame.transform.flip(self.run_right[3], True, False), pygame.transform.flip(self.run_right[4], True, False), pygame.transform.flip(self.run_right[5], True, False), pygame.transform.flip(self.run_right[6], True, False), pygame.transform.flip(self.run_right[7], True, False), pygame.transform.flip(self.run_right[8], True, False), pygame.transform.flip(self.run_right[9], True, False)]
        self.jump_move = [pygame.image.load('Asset/Ninja/Jump__000.png'), pygame.image.load('Asset/Ninja/Jump__001.png'), pygame.image.load('Asset/Ninja/Jump__002.png'), pygame.image.load('Asset/Ninja/Jump__003.png'), pygame.image.load('Asset/Ninja/Jump__004.png'), pygame.image.load('Asset/Ninja/Jump__005.png'), pygame.image.load('Asset/Ninja/Jump__006.png'), pygame.image.load('Asset/Ninja/Jump__007.png'), pygame.image.load('Asset/Ninja/Jump__008.png')]
        self.idle = pygame.image.load('Asset/Ninja/Idle__001.png')
        self.standing = False

    def movearound(self):
        self.movement = [self.x, self.y]
        if self.walk_count + 1 > 27:
            self.walk_count = 0

        if self.right:
            self.walk_count += 1
            self.image = self.run_right[self.walk_count // 3]
            self.movement[0] += self.speed

        elif self.left:
            self.walk_count += 1
            self.image = self.run_left[self.walk_count // 3]
            self.movement[0] -= self.speed
        else:
            self.movement[0] = 0
            if self.standing:
                self.image = self.idle
            else:
                self.image = pygame.transform.flip(self.idle, True, False)

        self.movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.4
        if self.vertical_momentum >= 6:
            self.vertical_momentum = 6
        screen.blit(self.image, (self.rect.x - scroll[0], self.rect.y - scroll[1]))



player = Player()
map = GameMap()

def collide(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collide(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += round(movement[1])
    hit_list = collide(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

def redrawnscreen():
    player.rect,collisions = move(player.rect, player.movement, map.tile_rects)
    if collisions["bottom"] == True:
        player.air_timer = 0
        player.vertical_momentum = 0
    else:
        player.air_timer += 9

    player.movearound()
    pygame.display.update()


running = True
while running:
    clock.tick(60)
    true_scroll[0] += (player.rect.x - true_scroll[0] - 532) / 25
    true_scroll[1] += (player.rect.y - true_scroll[1] - 357) / 25
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    map.map1()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.right = True
                player.left = False
                player.walk_count += 1
                player.standing = False
            if event.key == pygame.K_LEFT:
                player.left = True
                player.right = False
                player.walk_count += 1
                player.standing = False
            if event.key == pygame.K_SPACE:
                if player.air_timer <= 9:
                    player.vertical_momentum = -18

            else:
                player.standing = True
                player.walk_count = 0

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.right = False
            if event.key == pygame.K_LEFT:
                player.left = False
    redrawnscreen()
    pygame.display.update()
