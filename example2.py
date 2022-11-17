# import / initialize pygame
from random import randint, choice
import pygame
pygame.init()


# get the clock
clock = pygame.time.Clock()

# configure screen size
screen = pygame.display.set_mode([500, 500])  # this call returns screen obj

lanes = ['93, 218, 343']
# make a game object class that draws a rectangle


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):  # removed height/width params
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        # this call returns a rectangular object w/ surf dimensions
        self.rect = self.surf.get_rect()

    # method drawing game object's surface to screen
    def render(self, screen):
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))

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
        # self.x = randint(50, 400)
        # self.y = -64
        self.x = choice(lanes)
        self.y = -64

# strawberry moves horizontally


class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500:
            self.reset()

    def reset(self):
        self.x = -64
        self.y = choice(lanes)


# make instance of game object
# box = GameObject(120, 300, 50, 50)
# apple = GameObject(120, 300, 'apple.png')
apple = Apple()

# make instance of strawberry game object
# strawberry = GameObject(400, 100, 'strawberry.png')
strawberry = Strawberry()

# player instance will inherit from game object

# make bomb class


class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'bomb.png')
        self.dx = 0
        self.dy = 0
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
            self.reset()

    def reset(self):
        direction = randint(1, 4)
        if direction == 1:  # left
            self.x = -64
            self.y = choice(lanes)
            self.dx = (randint(0, 200) / 100) + 1
            self.dy = 0
        elif direction == 2:  # right
            self.x = 500
            self.y = choice(lanes)
            self.dx = ((randint(0, 200) / 100) + 1) * -1
            self.dy = 0
        elif direction == 3:  # down
            self.x = choice(lanes)
            self.y = -64
            self.dx = 0
            self.dy = (randint(0, 200) / 100) + 1
        else:
            self.x = choice(lanes)
            self.y = 500
            self.dx = 0
            self.dy = ((randint(0, 200) / 100) + 1) * -1


bomb = Bomb()


class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png')
        # player adds dx/dy attributes
        self.dx = 0
        self.dy = 0
        self.pos_x = 1
        self.pos_y = 1
        self.reset()

    # movement methods that update player position upon keypress

    def left(self):
        # self.dx -= 100
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        # self.dx += 100
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def up(self):
        # self.dy -= 100
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    def down(self):
        # self.dx += 100
        if self.pos_y < len(lanes) - 1:
            self.pos_1 += 1
            self.update_dx_dy()

    # updates player position in each frame
    def move(self):
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    # moves player to center of screen
    def reset(self):
        # self.x = 250 - 32
        # self.y = 250 - 32
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]


# make instance of player
player = Player()

# create new instance of Surface
# surf = pygame.Surface((50, 50))
# surf.full((255, 111, 33))

# groups = class managing a collection of sprites
# make a group
all_sprites = pygame.sprite.Group()

# add all sprites to group
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)

# make a fruits Group
fruit_sprites = pygame.sprite.Group()

fruit_sprites.add(apple)
fruit_sprites.add(strawberry)


# create game loop
running = True
while running:
    # looks for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if game quits by closing window
            running = False
        # check for event type KEYBOARD
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame .K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # clear screen
    screen.fill((255, 255, 255))  # using rgb values for white
    # draw the surface using 'blit' (copying pixel blocks onto other pixel blocks)
    # screen.blit(surf, (100, 120))

    # draw box
    # box.render(screen)

    # draw apple
    # apple.move()
    # apple.render(screen)

    # challenge 1: draw a strawberry
    # strawberry.render(screen)

    # draw player
    # player.move()
    # player.render(screen)

    # move and render sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    # Check collisions
    # this call returns a sprite from group that collided w/ test sprite
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        friut.reset()
    # check collision player & bomb
    if pygame.sprite.collide_rect(player, bomb):
        running = False

    # update display
    pygame.display.flip()

    # tick the clock!
    clock.tick(60)  # updates applied in 1/30th of a sec.
