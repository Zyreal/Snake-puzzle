import pygame
import time
# opens application
pygame.init()
display_width = 500
display_height = 400
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake game puzzle')
white = (0,0,0)

level = 1

def game():
    hasPlaced = False
    white = (255,255,255)
    red = (255,0,0)
    black = (0,0,0)

    x = 0
    move_x = 0
    # 0 none 1 left 2 right
    horizontal = False
    y = 0
    move_y = 0
    # 0 none 1 up 2 down
    vertical = False
    game_over = False
    
    # different map levels
    def level(curr_level, color):
        if curr_level == 1:
            #rectangles are items player must collect
            pygame.draw.rect(display, color, [20, 20, 10, 10])
            pygame.draw.rect(display, color, [420, 320, 10, 10])
            pygame.draw.rect(display, color, [20, 320, 10, 10])
        elif curr_level == 2:
            pygame.draw.rect(display, color, [60, 30, 10, 10])
            pygame.draw.rect(display, color, [60, 100, 10, 10])
            pygame.draw.rect(display, color, [300, 100, 10, 10])
            pygame.draw.rect(display, color, [300, 320, 10, 10])
            pygame.draw.rect(display, color, [30, 320, 10, 10])
            pygame.draw.rect(display, color, [30, 60, 10, 10])
            pygame.draw.rect(display, color, [420, 60, 10, 10])
        elif curr_level == 3:
            pygame.draw.rect(display, color, [100, 50, 10, 10])
            pygame.draw.rect(display, color, [150, 50, 10, 10])
            pygame.draw.rect(display, color, [150, 220, 10, 10])
            pygame.draw.rect(display, color, [20, 220, 10, 10])
            pygame.draw.rect(display, color, [20, 100, 10, 10])
            pygame.draw.rect(display, color, [400, 100, 10, 10])
            pygame.draw.rect(display, color, [400, 150, 10, 10])
            pygame.draw.rect(display, color, [100, 150, 10, 10])
            pygame.draw.rect(display, color, [100, 10, 10, 10])
            pygame.draw.rect(display, color, [400, 10, 10, 10])
            pygame.draw.rect(display, color, [400, 320, 10, 10])
            pygame.draw.rect(display, color, [20, 320, 10, 10])
        pygame.display.update()

    while not game_over:
        # checks every command/movement user does
        for event in pygame.event.get():
            # checks if player has clicked the x icon
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if hasPlaced == False:
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x,mouse_y = pygame.mouse.get_pos()
                    x = mouse_x
                    y = mouse_y
                    # draw.rect() takes display, color, [positionX, positionY, sizeX, sizeY]
                    pygame.draw.rect(display,red,[mouse_x,mouse_y,10,10])
                    hasPlaced = True
            else:
                # check key direction
                if event.type==pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and horizontal == False:
                        move_x = -10
                        move_y = 0
                        horizontal = True
                        vertical = False
                    elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and horizontal == False:
                        move_x = 10
                        move_y = 0
                        horizontal = True
                        vertical = False
                    elif (event.key == pygame.K_UP or event.key == pygame.K_w) and vertical == False:
                        move_x = 0
                        move_y = -10
                        horizontal = False
                        vertical = True
                    elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and vertical == False:
                        move_x = 0
                        move_y = 10
                        horizontal = False
                        vertical = True
        # only draw if block has been placed
        if hasPlaced == True:
            x += move_x
            y += move_y
            pygame.draw.rect(display,red,[x,y,10,10])
            pygame.display.update()
            # changes tick rate of pygame (frames per second)
            pygame.time.Clock().tick(20)
        # game ends if out of bounds
        if x < 0 or x > display_width or y < 0 or y > display_height:
            game_over = True
game()
font_style = pygame.font.SysFont(None, 50)
msg = font_style.render("Game Over", True, white)

# creates a rectangle the size of the msg text and puts its coordinates in the center of screen
msg_rect = msg.get_rect(center=(display_width / 2, display_height / 2) )

display.blit(msg, msg_rect)


pygame.display.update()
time.sleep(1)

# closes application
pygame.quit()

# stops code
quit()