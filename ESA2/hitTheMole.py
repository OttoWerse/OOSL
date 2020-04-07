# Import
import pygame
from pygame.locals import *
import random

# Initialization
pygame.init()

# Display
size_x = 1280
size_y = 720
size = (size_x, size_y)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Fix the bug!')


#
class Mole(pygame.sprite.Sprite):
    def __init__(self):
        # Super
        pygame.sprite.Sprite.__init__(self)
        # Sizes
        self.size_x = 50
        self.size_y = 50
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

bg_hit = pygame.image.load('hit-background.png')
bg_hit = pygame.transform.scale(bg_hit, (size))

font_size = 25
font = pygame.font.Font(None, font_size)

# Action --> Alter
# Variables
# Program escape variable
keepGoing = True
# Variable to prevent double hits
isHit = False
# Hit counter
hitCounter = 0
# Move timer (decrease to increase difficulty)
moveTime = 2000
# New clock
clock = pygame.time.Clock()
# Initialize update loop
pygame.time.set_timer(USEREVENT, 200)
# Set initial text
text = font.render(f'Bugfixes: {hitCounter}', True, Color('white'))
# Display initial text

# Loop
while keepGoing:
    # Timer
    clock.tick(60)

    # Events
    for event in pygame.event.get():
        # Exit the program
        if event.type == QUIT:
            keepGoing = False
            break
        # On mouse click
        elif event.type == MOUSEBUTTONDOWN:
            # If the mole is hit
            if mole.hit(pygame.mouse.get_pos()):
                # and the mole hasn't been hit already
                if not isHit:
                    # Mark mole as hit (un-hittable)
                    isHit = True
                    # Play hit sound
                    mole.cry()
                    # Increase hit counter and difficulty
                    hitCounter += 1
                    moveTime = int(moveTime // 1.01)
                    # Show hit image
                    screen.blit(bg_hit, (0, 0))
                    pygame.display.flip()
                    # Wait a bit
                    pygame.time.delay(250)
                    # Update text to show new counter
                    text = font.render(f'Bugfixes: {hitCounter}', True, Color('white'))
                    # Break
                    break
        elif event.type == USEREVENT:
            # change mole position
            mole.flee()
            # Mark mole as hittable
            isHit = False
            # restart timer
            pygame.time.set_timer(USEREVENT, moveTime)

    # Refresh
    pygame.display.flip()

    # Update Screen
    screen.blit(bg, (0, 0))
    # update sprites
    sprite_group.update()
    sprite_group.draw(screen)
    # Update text
    screen.blit(text, (10, 10))

    # Redisplay
