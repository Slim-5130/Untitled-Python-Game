import pygame, sys, myutils
from pygame.locals import *
from myutils import *
FPS = 12

WINWIDTH = 800
WINHEIGHT = 608
CELLSIZE = 32

CELLWIDTH = int(WINWIDTH / CELLSIZE)
CELLHEIGHT = int(WINHEIGHT / CELLSIZE)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
STOP = 'stop'


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Curse of the Grey Order')

    showStartScreen()

    while True:
        runGame()
        showGameOverScreen()


def runGame():
    # player spawn point
    startx = 400
    starty = 500
    playerCoords = {'x' : startx, 'y' : starty}

    while True:
        direction = STOP

        # event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_d:
                    direction = RIGHT
                elif event.key == K_a:
                    direction = LEFT
                elif event.key == K_s:
                    direction = DOWN
                elif event.key == K_w:
                    direction = UP
                elif event.key == K_ESCAPE:
                    terminate()
            else:
                direction = STOP
        # collision detection
        step = collisionDetection(playerCoords, 32, direction)

        # moving the avatar
        if direction == UP:
            playerCoords = {'x' : (playerCoords['x']), 'y' : (playerCoords['y'] - step)}
        elif direction == DOWN:
            playerCoords = {'x': (playerCoords['x']), 'y': (playerCoords['y'] + step)}
        elif direction == LEFT:
            playerCoords = {'x': (playerCoords['x'] - step), 'y': (playerCoords['y'])}
        elif direction == RIGHT:
            playerCoords = {'x': (playerCoords['x'] + step), 'y': (playerCoords['y'])}

        # updating the screen
        DISPLAYSURF.fill((255, 255, 255))
        drawPlayer(playerCoords)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 50)
    titleSurf = titleFont.render('Curse of the Grey Order', True, (0, 125, 200))
    titleRect = titleSurf.get_rect()
    titleRect.center = (400, 400)

    while True:
        DISPLAYSURF.fill((0, 0, 0))
        DISPLAYSURF.blit(titleSurf, titleRect)

        pressKeySurf = titleFont.render('Press a key to play.', True, (60, 60, 60))
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (WINWIDTH - 470, WINHEIGHT - 50)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)


# Come fix this later
def showGameOver():
    return 0


def drawPlayer(playerCoords):
        playerSprite = pygame.image.load('EogertBasic.png')
        DISPLAYSURF.blit(playerSprite, (playerCoords['x'], playerCoords['y']))

main()