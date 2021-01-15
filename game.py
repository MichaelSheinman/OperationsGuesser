import pygame

pygame.init()
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
font = pygame.font.Font('freesansbold.ttf', 32)
green = (0, 255, 0)
blue = (0, 0, 128)
pale = (255, 255, 153)

win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Test")

plus = pygame.image.load("images/plus_sign.png")
times = pygame.image.load("images/multiplication_sign.png")
divide = pygame.image.load("images/division_sign.png")

plus = pygame.transform.scale(plus, (30, 30))
minus = 0
mult = pygame.transform.scale(times, (30, 30))
divide = pygame.transform.scale(divide, (30, 30))

test_string = "(2 + 3) + 86 + 17 / 5 = 1"
omited_string = ""
final_string = ""

num_spaces = len(test_string)
equation_display = []

for i in range(num_spaces):
    if test_string[i] == "+" or test_string[i] == "-" or test_string[
        i] == "/" or test_string[i] == "*":
        equation_display.append(((20 + i * (WINDOW_WIDTH - 50) / num_spaces),
                                 WINDOW_HEIGHT * 0.30, 30, 30))
        omited_string += '#'
    elif test_string[i].isnumeric() or test_string[i] in "()=":
        num = font.render(test_string[i], True, blue, pale)
        rect = num.get_rect()
        rect.topleft = ((20 + i * (WINDOW_WIDTH - 50) / num_spaces),
                        WINDOW_HEIGHT * 0.30)
        equation_display.append((num, rect))
        omited_string += test_string[i]
    else:
        omited_string += test_string[i]

print(omited_string)

mult_l = mult_x, mult_y = [50, WINDOW_HEIGHT * 0.70]
plus_l = plus_x, plus_y = [(50 + (WINDOW_WIDTH - 50) / 4), WINDOW_HEIGHT * 0.70]
minus_l = minus_x, minus_y = [(50 + 2 * (WINDOW_WIDTH - 50) / 4),
                              WINDOW_HEIGHT * 0.70 + 12]
divide_l = divide_x, divide_y = [(50 + 3 * (WINDOW_WIDTH - 50) / 4),
                                 WINDOW_HEIGHT * 0.70]

mult_orig = (mult_x, mult_y)
plus_orig = (plus_x, plus_y)
minus_orig = (minus_x, minus_y)
divide_orig = (divide_x, divide_y)

signs = []
signs_placed = []

x = 50
y = 50
width = 50
height = 70

run = True

clicking_obj = {}

while run:
    win.fill((255, 255, 153))

    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if mult_orig[0] <= mx <= mult_orig[0] + 50 and \
                        mult_orig[1] <= my <= mult_orig[1] + 50:
                    new_mult = mult
                    signs.append([new_mult, mx, my, "*", False])
                    clicking_obj[len(signs) - 1] = True

                if minus_orig[0] <= mx <= minus_orig[0] + 50 and minus_orig[
                    1] <= my <= minus_orig[1] + 50:
                    new_minus = minus
                    signs.append([new_minus, mx, my, "-", False])
                    clicking_obj[len(signs) - 1] = True

                if plus_orig[0] <= mx <= plus_orig[0] + 50 and plus_orig[
                    1] <= my <= plus_orig[1] + 50:
                    new_plus = plus
                    signs.append([new_plus, mx, my, "+", False])
                    clicking_obj[len(signs) - 1] = True

                if divide_orig[0] <= mx <= divide_orig[0] + 50 and divide_orig[
                    1] <= my <= divide_orig[1] + 50:
                    new_divide = divide
                    signs.append([new_divide, mx, my, "/", False])
                    clicking_obj[len(signs) - 1] = True

                if mx >= 450 and my >= 450:
                    signs_placed.sort()
                    final_string = omited_string
                    for i in signs_placed:
                        final_string = final_string.replace("#", i[1], 1)
                    if "#" in final_string:
                        print("Put an operator in EVERY red box")
                    else:
                        print(final_string)

            for i in range(len(signs)):
                if signs[i][1] < mx < signs[i][1] + 50 and signs[i][2] < my < \
                        signs[i][2] + 50:
                    clicking_obj[i] = True
                    break

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for i in clicking_obj:
                    if clicking_obj[i]:
                        clicking_obj[i] = False
                        is_on_blank = False
                        for y in range(len(equation_display)):
                            if len(equation_display[y]) != 2:
                                blank_loc = (
                                    equation_display[y][0],
                                    equation_display[y][1])
                                if blank_loc[0] <= signs[i][1] <= blank_loc[
                                    0] + 30 and blank_loc[1] <= signs[i][2] <= \
                                        blank_loc[1] + 30:
                                    signs[i][1] = blank_loc[0]
                                    signs[i][2] = blank_loc[1]
                                    if signs[i][3] == '-':
                                        signs[i][2] += 12
                                    if signs[i][4]:
                                        for z in range(len(signs_placed)):
                                            if signs_placed[z][2] == i:
                                                signs_placed.pop(z)
                                                break
                                    signs_placed.append((y, signs[i][3], i))
                                    is_on_blank = True
                        if signs[i][4] and not is_on_blank:
                            signs[i][4] = False
                            for y in range(len(signs_placed)):
                                if signs_placed[y][2] == i:
                                    signs_placed.pop(y)
                                    break
                        signs[i][4] = is_on_blank
                        break

    for i in clicking_obj:
        if clicking_obj[i]:
            signs[i][1] = mx
            signs[i][2] = my

    for item in equation_display:
        if len(item) == 2:
            win.blit(item[0], item[1])
        else:
            pygame.draw.rect(win, (255, 0, 0), item)

    for i in range(len(signs)):
        if signs[i][3] == '*' or signs[i][3] == '/' or signs[i][3] == '+':
            win.blit(signs[i][0], (signs[i][1], signs[i][2]))
        elif signs[i][3] == '-':
            pygame.draw.rect(win, (0, 0, 0), (signs[i][1], signs[i][2], 30, 7))

    pygame.draw.rect(win, (0, 0, 0), (minus_x, minus_y, 30, 7))
    win.blit(plus, plus_l)
    win.blit(divide, divide_l)
    win.blit(mult, mult_l)

    # Check button
    pygame.draw.rect(win, (0, 0, 0), (450, 450, 50, 50))

    pygame.display.update()

pygame.quit()
