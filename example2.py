# import / initialize pygame
from random import randint
import pygame
pygame.init()


# get the clock
clock = pygame.time.Clock()

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

# class extending game object


class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, 'apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1  # sets speed of apple's mvmt
        self.reset()  # call restart method

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # check y position of apple
        if self.y > 500:
            self.reset()

    # add a new method to get apple back to top of screen
    def reset(self):
        self.x = randint(50, 400)
        self.y = -64


# make instance of game object
# box = GameObject(120, 300, 50, 50)
# apple = GameObject(120, 300, 'apple.png')
apple = Apple()

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
    apple.move()
    apple.render(screen)

    # challenge 1: draw a strawberry
    strawberry.render(screen)

    # update display
    pygame.display.flip()

    # tick the clock!
    clock.tick(60)  # updates applied in 1/30th of a sec.
