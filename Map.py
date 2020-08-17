import pygame
import sys

class Map(object):
    def __init__(self):
        self.grass = pygame.image.load(
            'Asset/Forrest/png/Tiles/2.png').convert()
        self.dirt = pygame.image.load(
            'Asset/Forrest/png/Tiles/5.png').convert()
        self.bg = pygame.image.load("Asset/Forrest/png/BG/BG.png").convert()
        self.sign2 = pygame.image.load('Asset/Forrest/png/Object/Sign_2.png')
        self.mushroom1 = pygame.image.load(
            'Asset/Forrest/png/Object/Mushroom_1.png')
        self.stone = pygame.image.load('Asset/Forrest/png/Object/Stone.png')

    def load_map(self, path):
        f = open(path + '.txt', 'r')
        data = f.read()
        f.close()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map

    def map1(self, screen, scroll):
        screen.blit(self.bg, (0,0))
        self.game_map = self.load_map('map')
        self.tile_rects = []
        y = 0
        for layer in self.game_map:
            x = 0
            for tile in layer:
                if tile == '1':
                    screen.blit(
                        self.dirt, (x * 128 - scroll[0], y * 128 - scroll[1]))
                if tile == '2':
                    screen.blit(
                        self.grass, (x * 128 - scroll[0], y * 128 - scroll[1]))
                if tile == '3':
                    screen.blit(
                        self.sign2, (x * 62 - scroll[0], y * 420 - scroll[1]))
                if tile == '4':
                    screen.blit(self.mushroom1, (x * 80 -
                                                 scroll[0], y * 430 - scroll[1]))
                if tile == '5':
                    screen.blit(
                        self.stone, (x * 100 - scroll[0], y * 430 - scroll[1]))
                if tile != '0':
                    self.tile_rects.append(
                        pygame.Rect(x * 128, y * 128, 128, 128))
                x += 1
            y += 1
