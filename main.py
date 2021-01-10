import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_icon(pygame.image.load("favico.jpg"))

pygame.display.set_caption("Ethan, Michael, and Rehmat's Ultimate Learning Math Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False