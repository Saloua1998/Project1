import pygame

pygame.init()

screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
pygame.display.set_caption('Guess The Number!')
pygame.display.set_icon()

black = (0, 0, 0)
condition = True

while condition:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    pygame.display.update()
