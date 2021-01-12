import pygame
pygame.init()
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
font = pygame.font.Font('freesansbold.ttf', 32)
green = (0, 255, 0)
blue = (0, 0, 128)

win = pygame.display.set_mode(((WINDOW_WIDTH, WINDOW_HEIGHT)))

pygame.display.set_caption("Test")

test_string = "(2 + 3) + 86 + 17/ 5 = 1"
num_spaces = len(test_string)
equation_display = []

for i in range(num_spaces):
    if test_string[i] == "+" or test_string[i] == "-" or test_string[i] == "/" or test_string[i] == "*":
        equation_display.append(((20 + i*(WINDOW_WIDTH - 50)/num_spaces), WINDOW_HEIGHT*0.30, 30, 30))
    elif test_string[i].isnumeric() or test_string[i] in "()=": 
        num = font.render(test_string[i], True, green, blue)
        rect = num.get_rect()
        rect.topleft = ((20 + i*(WINDOW_WIDTH - 50)/num_spaces),
                       WINDOW_HEIGHT*0.30)
        equation_display.append((num, rect))


mult = mult_x, mult_y, symbol_width, symbol_height = (50, WINDOW_HEIGHT*0.70, 30, 30)
add = add_x, add_y, symbol_width, symbol_height = ((50 + (WINDOW_WIDTH - 50)/4), WINDOW_HEIGHT*0.70, 30, 30)
subtract = subtract_x, subtract_y, symbol_width, symbol_height = ((50 + 2*(WINDOW_WIDTH - 50)/4), WINDOW_HEIGHT*0.70, 30, 30)
divide = divide_x, divide_y, symbol_width, symbol_height = ((50 + 3*(WINDOW_WIDTH - 50)/4), WINDOW_HEIGHT*0.70, 30, 30)

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
                clicking_mult = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicking_rect = False

    if clicking_rect:
        x = mx
        y = my
    pygame
    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    for item in equation_display:
        if len(item) == 2:
            win.blit(item[0], item[1])
        else:
            pygame.draw.rect(win, (255, 0, 0), item)
    
    pygame.draw.rect(win, green, mult)
    pygame.draw.rect(win, green, add)
    pygame.draw.rect(win, green, subtract)
    pygame.draw.rect(win, green, divide)

    pygame.display.update()








pygame.quit()
