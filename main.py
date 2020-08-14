import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen_size = (1000, 650)
screen = pygame.display.set_mode(screen_size, 0, 32)


true_scroll = [0,0]

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

game_map = load_map('map')

bg = pygame.image.load("Asset/Forrest/png/BG/BG.png").convert()
grass = pygame.image.load('Asset/Forrest/png/Tiles/2.png')
dirt = pygame.image.load('Asset/Forrest/png/Tiles/5.png')

class Player(object):
    def __init__(self):
        self. x = 300
        self.y = 835
        self.height = 64
        self.width = 50
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.left = False
        self.right = False
        self.jump = False
        self.jump_count = 10
        self.walk_count = 0
        self.run_right = [pygame.image.load('Asset/Ninja/Run__000.png'), pygame.image.load('Asset/Ninja/Run__001.png'), pygame.image.load('Asset/Ninja/Run__002.png'), pygame.image.load('Asset/Ninja/Run__003.png'),pygame.image.load('Asset/Ninja/Run__004.png'), pygame.image.load('Asset/Ninja/Run__005.png'), pygame.image.load('Asset/Ninja/Run__006.png'), pygame.image.load('Asset/Ninja/Run__007.png'), pygame.image.load('Asset/Ninja/Run__008.png')]
        self.run_left = [pygame.transform.flip(self.run_right[0], True, False), pygame.transform.flip(self.run_right[1], True, False), pygame.transform.flip(self.run_right[2], True, False), pygame.transform.flip(self.run_right[3], True, False), pygame.transform.flip(self.run_right[4], True, False), pygame.transform.flip(self.run_right[5], True, False), pygame.transform.flip(self.run_right[6], True, False), pygame.transform.flip(self.run_right[7], True, False), pygame.transform.flip(self.run_right[8], True, False)]
        self.jump_move = [pygame.image.load('Asset/Ninja/Jump__000.png'), pygame.image.load('Asset/Ninja/Jump__001.png'), pygame.image.load('Asset/Ninja/Jump__002.png'), pygame.image.load('Asset/Ninja/Jump__003.png'), pygame.image.load('Asset/Ninja/Jump__004.png'), pygame.image.load('Asset/Ninja/Jump__005.png'), pygame.image.load('Asset/Ninja/Jump__006.png'), pygame.image.load('Asset/Ninja/Jump__007.png'), pygame.image.load('Asset/Ninja/Jump__008.png')]
        self.idle = pygame.image.load('Asset/Ninja/Idle__001.png')
        self.standing = False


player = Player()

def redrawnscreen():
    player.hitbox = (player.x, player.y, player.width, player.height)
    pygame.draw.rect(screen, (0,0,0), player.hitbox, 2)
    if player.walk_count + 1 > 27:
        player.walk_count = 0

    if player.right:
        screen.blit(player.run_right[player.walk_count // 3], (player.x - scroll[0], player.y - scroll[1]))
        player.walk_count += 1
        player.standing = True
        player.x += 3
    elif player.left:
        screen.blit(player.run_left[player.walk_count // 3], (player.x - scroll[0], player.y - scroll[1]))
        player.walk_count += 1
        player.x -= 3
    else:
        if player.standing:
            screen.blit(player.idle, (player.x - scroll[0], player.y - scroll[1]))
        else:
            screen.blit(pygame.transform.flip(player.idle, True, False), (player.x - scroll[0], player.y - scroll[1]))
    pygame.display.update()


running = True
while running:
    clock.tick(60)
    screen.blit(bg, (0,0))
    true_scroll[0] += (player.x - true_scroll[0] - 532) / 20
    true_scroll[1] += (player.y - true_scroll[1] - 357) / 20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])
    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                screen.blit(dirt,(x*128 - scroll[0],y*128 - scroll[1]))
            if tile == '2':
                screen.blit(grass,(x*128 - scroll[0],y*128 - scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x*128,y*128,128,128))
            x += 1
        y += 1
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
