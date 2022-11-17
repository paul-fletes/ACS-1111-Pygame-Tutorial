# import / initialize pygame
import pygame
pygame.init()

# configure screen size
screen = pygame.display.set_mode([500, 500])  # this call returns screen obj

# make a game object class that draws a rectangle


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):  # removed height/width params
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y

    # method drawing game object's surface to screen
    def render(self, screen):
        screen.bilt(self.surf, (self.x, self.y))


# make instance of game object
# box = GameObject(120, 300, 50, 50)
apple = GameObject(120, 300, 'apple.png')

# make instance of strawberry game object
strawberry = GameObject(400, 100, 'strawberry.png')

# create new instance of Surface
# surf = pygame.Surface((50, 50))
# surf.full((255, 111, 33))

# create game loop
running = True
while running:
    # looks for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if game quits by closing window
            running = False

    # clear screen
    screen.fill((255, 255, 255))  # using rgb values for white
    # draw the surface using 'blit' (copying pixel blocks onto other pixel blocks)
    # screen.blit(surf, (100, 120))

    # draw box
    # box.render(screen)

    # draw apple
    apple.render(screen)

    # challenge 1: draw a strawberry
    strawberry.render(screen)

    # update display
    pygame.display.flip()
