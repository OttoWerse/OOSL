import pygame
from pygame.locals import *

pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
pygame.display.set_caption('Paint Brush')

brush = pygame.image.load('brush.png')
brush = pygame.transform.scale(brush, (64, 64))
rect = brush.get_rect()

# Action --> ALTER
# Variables
keepGoing = True
paint = False
clock = pygame.time.Clock()
speed = [2,2]

# Loop
while keepGoing:
    # Timer
    clock.tick(120)

    # Events
    for event in pygame.event.get():
        if event.type == QUIT:
            keepGoing = False
            break
        elif event.type == MOUSEBUTTONDOWN:
            paint = True
        elif event.type == MOUSEBUTTONUP:
            paint = False

    rect = rect.move(speed)
    if rect.left < 0 or rect.right > size[0]:
        speed[0] = -speed[0]
    if rect.top < 0 or rect.bottom > size[1]:
        speed[1] = -speed[1]


    if paint:
        x, y = pygame.mouse.get_pos()
        screen.blit(brush, (x - 32, y - 32))

    # Redisplay
    screen.blit(brush, rect)
    pygame.display.update()
