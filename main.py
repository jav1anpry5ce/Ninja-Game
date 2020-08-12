import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))

backgorund = pygame.image.load("Asset/Forrest/png/BG/BG.png")

map = [['0' '0', '0', '0', '0', '0', '0', '0']]


running = True
while running:
    win.blit(backgorund, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
