import pygame
import sys
import math
import random
from Player import Player
from Enemy import Enemy
from Map import Map

pygame.init()
clock = pygame.time.Clock()

class Game(object):
    def __init__(self):
        self.screen_size = (1000, 650)
        self.screen = pygame.display.set_mode(self.screen_size, 0, 32)
        self.true_scroll = [0, 0]
        self.scroll = self.true_scroll.copy()

    def collide(self, rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(self, rect, movement, tiles):
        collision_types = {'top': False, 'bottom': False,
                           'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = self.collide(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += round(movement[1])
        hit_list = self.collide(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types

    def redrawnscreen(self):
        player.rect, collisions = self.move(
            player.rect, player.movement, map.tile_rects)
        enemy.rect, enemycollisions = self.move(
            enemy.rect, enemy.movement, map.tile_rects)

        if enemycollisions["right"] == True:
            enemy.right = False
            if enemy.right == False:
                enemy.left = True
        elif enemycollisions["left"] == True:
            enemy.left = False
            if enemy.left == False:
                enemy.right = True
        if collisions["bottom"] == True:
            player.air_timer = 0
            player.vertical_momentum = 0
            player.jumping = False
        elif collisions["top"] == True:
            player.air_timer = 0
            player.vertical_momentum = 0
        else:
            player.air_timer += 9

        player.deadanimation()
        enemy.deadanimation()
        if not player.dead:
            player.movearound()
            player.attack(self.scroll)
            if player.throwattack and player.loop >= 14:
                self.screen.blit(player.kunaiimg, (player.kunai.x, player.kunai.y))


        if not enemy.dead:
            enemy.movearound()
            enemy.attack(player.x, enemy.x, player.y, enemy.y)

        if enemy.attacking and pygame.sprite.collide_mask(player, enemy):
            if enemy.attack_count == 58 // 3:
                player.health -= 1
        if player.attacking and pygame.sprite.collide_mask(player, enemy):
            if player.loop == 10 - 1:
                enemy.health -= 2

        self.screen.blit(player.image, (player.rect.x - self.scroll[0], player.rect.y - self.scroll[1]))
        self.screen.blit(enemy.image, (enemy.rect.x - self.scroll[0], enemy.rect.y - self.scroll[1]))
        pygame.display.update()

    def main(self):
        clock.tick(60)
        self.true_scroll[0] += (player.rect.x - self.true_scroll[0] - 532) / 15
        self.true_scroll[1] += (player.rect.y - self.true_scroll[1] - 357)
        self.scroll = self.true_scroll.copy()
        self.scroll[0] = int(self.scroll[0])
        self.scroll[1] = int(self.scroll[1])
        map.map1(self.screen, self.scroll)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.right = True
                    player.left = False
                    player.animation += 1
                    player.standing = False

                if event.key == pygame.K_LEFT:
                    player.left = True
                    player.right = False
                    player.animation += 1
                    player.standing = False

                if event.key == pygame.K_SPACE:
                    if player.air_timer <= 9:
                        player.vertical_momentum = -18

                if event.key == pygame.K_c:
                    player.attacking = True
                if event.key == pygame.K_v:
                    player.throwattack = True

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
enemy = Enemy(800, 850)

running = True
while running:
    game.main()
