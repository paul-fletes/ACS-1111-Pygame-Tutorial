# import / initialize pygame
import pygame
pygame.init()

# configure screen size
screen = pygame.display.set_mode([500, 500])  # this call returns screen obj

# create game loop
running = True
while running:
    # looks for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if game quits by closing window
            running = False

    # clear screen
    screen.fill((255, 255, 255))  # using rgb values for white
    # draw a circle
    color = (255, 0, 255)
    position = (250, 250)  # center of screen object
    # this call draws a circle with above variable values with a radius of 75px
    pygame.draw.circle(screen, color, position, 75)
    # update display
    pygame.display.flip()
