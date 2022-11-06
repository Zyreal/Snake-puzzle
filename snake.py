import pygame
# opens application
pygame.init()
display_width = 500
display_height = 400
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake game puzzle')
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
curr_level = 1
# stores position of food items
food = []

continue_screen = False

# different map levels
def level(curr_level):
    global food
    if curr_level == 1:
        food = [(20,20),(420,320),(20,320)]
    elif curr_level == 2:
        food = [(60,30),(60,100),(300,100),(300,320),(30,320),(30,60),(420,60)]
    elif curr_level == 3:
        food = [(100,50),(150,50),(150,220),(20,220),(20,100),(400,100),(400,150),(100,150),(100,10),(400,10),(400,320),(20,320)]

def draw(color):
    global food
    display.fill(black)
    for i in food:
        x, y = i
        # rectangles is food player must eat
        pygame.draw.rect(display, color, [x, y, 10, 10])
    pygame.display.update()

# checks if position of food matches player position
def eaten(player_x, player_y, food = []):
    for i in food:
        x, y = i
        # between width and length of food square
        if ((x - 10 <= player_x <= x + 10) and (y - 10 <= player_y <= y + 10)):
            food.remove(i)
            return True
    return False
def game():
    global curr_level
    global continue_screen
    hasPlaced = False

    x = 0
    move_x = 0
    y = 0
    move_y = 0

    game_over = False

    action = False
    level(curr_level)

    draw(white)

    while not game_over:
        # let player give up or restart level
        while continue_screen == True:
            display.fill(black)
            font_style = pygame.font.SysFont(None, 30)
            if curr_level > 3:
                msg = font_style.render("You have Won!", True, white)
                msg2 = font_style.render("Press p to play again or q to quit", True, white)
            else:
                msg = font_style.render("Game Over!", True, white)
                # create another variable for a new line
                msg2 = font_style.render("Press r to restart level or q to quit", True, white)

            # creates a rectangle the size of the msg text and puts its center coordinates in the center of screen
            msg_rect = msg.get_rect(center=(display_width / 2, display_height / 2))
            msg2_rect = msg2.get_rect(center=(display_width / 2, display_height / 2 + msg_rect.height))
            display.blit(msg, msg_rect)
            display.blit(msg2, msg2_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if curr_level > 3:
                        if event.key==pygame.K_p:
                            curr_level = 1
                            continue_screen = False
                            game()
                    else:
                        if event.key==pygame.K_r:
                            continue_screen = False
                            game()
                    if event.key==pygame.K_q:
                        # closes application
                        pygame.quit()

                        # stops code
                        quit()
            pygame.display.update()
        # checks every command/movement user does
        for event in pygame.event.get():
            # checks if player has clicked the x icon
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if hasPlaced == False:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                # draw rectangle at the tip of the cursor
                mouse_x-=10
                mouse_y-=10
                display.fill(black)
                draw(white)
                pygame.draw.rect(display,red,[mouse_x,mouse_y,10,10])
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP:
                    # draw.rect() takes display, color, [positionX, positionY, sizeX, sizeY]
                    x = mouse_x
                    y = mouse_y
                    pygame.draw.rect(display,red,[mouse_x,mouse_y,10,10])
                    hasPlaced = True
            else:
                # check key direction
                if event.type==pygame.KEYDOWN:
                    if action == False:
                        if (event.key == pygame.K_LEFT or event.key == pygame.K_a):
                            move_x = -10
                            move_y = 0
                            action = True
                        elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                            move_x = 10
                            move_y = 0
                            action = True
                        elif (event.key == pygame.K_UP or event.key == pygame.K_w):
                            move_x = 0
                            move_y = -10
                            action = True
                        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                            move_x = 0
                            move_y = 10
                            action = True
        # only draw if first block has been placed
        if hasPlaced == True:
            x += move_x
            y += move_y
            if eaten(x, y, food):
                if food == []:
                    curr_level+=1
                    # player has finished all levels
                    if curr_level > 3:
                        continue_screen = True
                    level(curr_level)
                    game()
                move_x = 0
                move_y = 0
                action = False
            draw(white)
            # player has finished all levels
            if curr_level > 3:
                continue_screen = True
            pygame.draw.rect(display,red,[x,y,10,10])
            pygame.display.update()
            # changes tick rate of pygame (frames per second)
            pygame.time.Clock().tick(20)
        # game ends if out of bounds
        if x < 0 or x > display_width or y < 0 or y > display_height:
            continue_screen = True
game()
