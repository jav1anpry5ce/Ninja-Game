import pygame
import sys
import math
from Player import Player

pygame.init()
screen_size = (1000, 650)
screen = pygame.display.set_mode(screen_size, 0, 32)
clock = pygame.time.Clock()

class Map(object):
    def __init__(self):
        self.grass = pygame.image.load('Asset/Forrest/png/Tiles/2.png').convert()
        self.dirt = pygame.image.load('Asset/Forrest/png/Tiles/5.png').convert()
        self.bg = pygame.image.load("Asset/Forrest/png/BG/BG.png").convert()
        self.sign2 = pygame.image.load('Asset/Forrest/png/Object/Sign_2.png')
        self.mushroom1 = pygame.image.load('Asset/Forrest/png/Object/Mushroom_1.png')
        self.stone = pygame.image.load('Asset/Forrest/png/Object/Stone.png')

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
                    screen.blit(self.dirt,(x*128 - game.scroll[0],y*128 - game.scroll[1]))
                if tile == '2':
                    screen.blit(self.grass,(x*128 - game.scroll[0],y*128 - game.scroll[1]))
                if tile == '3':
                    screen.blit(self.sign2, (x*62 - game.scroll[0], y*420 - game.scroll[1]))
                if tile == '4':
                    screen.blit(self.mushroom1, (x*80 - game.scroll[0], y* 430 - game.scroll[1]))
                if tile == '5':
                    screen.blit(self.stone, (x*100 - game.scroll[0], y*430 - game.scroll[1]))
                if tile != '0':
                    self.tile_rects.append(pygame.Rect(x*128,y*128,128,128))
                x += 1
            y += 1


class Game(object):
    def __init__(self):
        self.true_scroll = [0,0]
        self.scroll = self.true_scroll.copy()
        self.screen = pygame.display.set_mode(screen_size, 0, 32)

    def collide(self, rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(self, rect, movement, tiles):
        collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        rect.x += movement[0]
        hit_list = self.collide(rect,tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += round(movement[1])
        hit_list = self.collide(rect,tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types

    def redrawnscreen(self):
        player.rect,collisions = self.move(player.rect, player.movement, map.tile_rects)
        if collisions["bottom"] or collisions["top"] == True:
            player.air_timer = 0
            player.vertical_momentum = 0
        else:
            player.air_timer += 9
        player.movearound()
        player.attackk()
        screen.blit(player.image, (player.rect.x - self.scroll[0], player.rect.y - self.scroll[1]))
        pygame.display.update()

    def main(self):
        clock.tick(60)
        self.true_scroll[0] += (player.rect.x - self.true_scroll[0] - 532) / 15
        self.true_scroll[1] += (player.rect.y - self.true_scroll[1] - 357) / 15
        self.scroll = self.true_scroll.copy()
        self.scroll[0] = int(self.scroll[0])
        self.scroll[1] = int(self.scroll[1])
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
                if event.key == pygame.K_c:
                    player.attacking = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.right = False
                if event.key == pygame.K_LEFT:
                    player.left = False
        game.redrawnscreen()
        pygame.display.update()

game = Game()
map = Map()
player = Player()

running = True
while running:
    game.main()
