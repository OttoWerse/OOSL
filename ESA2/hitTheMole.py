# Import
import pygame
from pygame.locals import *
import random

# Initialization
pygame.init()

# Display
size_x = 640
size_y = 480
size = (size_x, size_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Hit the Mole')


#
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        # Super
        pygame.sprite.Sprite.__init__(self)
        # Sizes
        self.size_x = 100
        self.size_y = 100
        # Load Image
        self.image = pygame.image.load('mole.png')
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        # Create Hit-Box
        self.rect = self.image.get_rect()
        # Assign sound
        self.sound = pygame.mixer.Sound('hit.wav')
        # Randomize position
        self.rect.left = random.randint(0, size_x - self.size_x / 2)
        self.rect.top = random.randint(0, size_y - self.size_y / 2)

    def flee(self):
        self.rect.left = random.randint(0, size_x - self.size_x / 2)
        self.rect.top = random.randint(0, size_y - self.size_y / 2)

    def cry(self):
        self.sound.play()

    def hit(self, pos):
        return self.rect.collidepoint(pos)


class Shovel(pygame.sprite.Sprite):
    def __init__(self):
        # Super
        pygame.sprite.Sprite.__init__(self)
        # Sizes
        self.size_x = 50
        self.size_y = 50
        # Load Image
        self.image = pygame.image.load('shovel.png')
        self.image = pygame.transform.scale(self.image, (self.size_x, self.size_y))
        # Create Hit-Box
        self.rect = self.image.get_rect()
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


mole = Mole()
shovel = Shovel()

sprite_group = pygame.sprite.Group()
sprite_group.add(mole)
sprite_group.add(shovel)

bg = pygame.image.load('background.png')
bg = pygame.transform.scale(bg, (size))

bg_hit = pygame.Surface(size)
bg_hit = bg_hit.convert()
bg_hit.fill((255, 0, 0))

font_size = 25
font = pygame.font.Font(None, font_size)

# Action --> Alter
# Variables
keepGoing = True
hitCounter = 0
clock = pygame.time.Clock()
moveTime = 1000
pygame.time.set_timer(USEREVENT, 200)
text = font.render(f'Moles: {hitCounter}', True, Color('white'))

# Loop
while keepGoing:
    # Timer
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
            break
        elif event.type == MOUSEBUTTONDOWN:
            if mole.hit(pygame.mouse.get_pos()):
                mole.cry()
                hitCounter += 1
                screen.blit(bg_hit, (0, 0))
                break
        elif event.type == USEREVENT:
            mole.flee()
            pygame.time.set_timer(USEREVENT, moveTime)
            screen.blit(bg, (0, 0))
            sprite_group.update()
            sprite_group.draw(screen)
            text = font.render(f'WLAN Probleme: {hitCounter}', True, Color('white'))
            screen.blit(text, (10, (size_y - font_size) / 2))


    pygame.display.flip()

    screen.blit(bg, (0, 0))
    sprite_group.update()
    sprite_group.draw(screen)
    screen.blit(text, (10, (size_y - font_size) / 2))

    # Redisplay
