import pygame, sys
from pygame.locals import *


def terminate():
    pygame.quit()
    sys.exit()


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
STOP = 'stop'

def collisionDetection(playerCoords, step, direction):
    if (direction == UP) and (playerCoords['y'] - step <= 0):
        return collisionDetection(playerCoords, (step - 1), direction)
    elif (direction == DOWN) and (playerCoords['y'] + step >= 575):
        return collisionDetection(playerCoords, (step - 1), direction)
    elif (direction == LEFT) and (playerCoords['x'] - step <= 0):
        return collisionDetection(playerCoords, (step - 1), direction)
    elif (direction == RIGHT) and (playerCoords['x'] + step >= 768):
        return collisionDetection(playerCoords, (step - 1), direction)
    else:
        return step


