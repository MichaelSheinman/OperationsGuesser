import pygame


pygame.init()

win = pygame.display.set_mode(((500, 500)))

pygame.display.set_caption("Test")


x = 50
y = 50
width = 50
height = 70

run = True

clicking_rect = False

while run:
    win.fill((0, 0, 0))

    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and x <= mx <= x + width and y <= my <= my + height:
                clicking_rect = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicking_rect = False

    if clicking_rect:
        x = mx
        y = my
    pygame
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()








pygame.quit()