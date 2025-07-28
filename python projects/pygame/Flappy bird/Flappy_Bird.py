import random
import sys


import pygame
from pygame.locals import *

# global Variables for the game
FPS = 32
SCREENWIDTH=289
SCREENHEIGHT=511

SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.
GAME_SPRITES ={}
GAME_SOUND ={}
PLAYER ='resources/bird.png'
BACKGROUND = 'resources/background.png'
PIPE = 'resources/pipe.png'

def Welcome_Screen():

    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2
    messagex = int(SCREENWIDTH - GAME_SPRITES['message'].get_height())/2
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key ==K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key==K_SPACE or event.key==K_UP ):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0,0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx,playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex,messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex,GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score =0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0

    # create pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my list of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[0]['y']},
    ]

    # my list of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y':newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y':newPipe2[1]['y']},
    ]
    pipeVelx= -4

    playerVelY = -9
    playerMaxVely = -10
    playerMinVely = -8
    playerAccY = -1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # it is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type== QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUND['wing'].play()

        crashtest = iscollide(playerx, playery, upperPipes, lowerPipes) # THis function will return true if the player is crashed
        if crashtest:
            return

        #check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES[ 'pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos + 4:
                 score +=1
                 print(f'Your score is {score}')
                 GAME_SOUND['point'].play()

        if playerVelY < playerMaxVely and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery+ min(playerVelY, GROUNDY - playery - playerHeight)


        #move pipes to the left
        for upperPipes, lowerPipes in zip(upperPipes, lowerPipes):
            upperPipes['x'] += pipeVelx
            lowerPipes['x'] += pipeVelx

        # add a new pipe when the first is about to cross the leftmost part of the screen
        if 0< upperPipes[0]['x']<5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])


        # if the pipe is out of the screen, remove it
        if upperPipes[0]["x"] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # lets blit sprites now
        SCREEN.blit(GAME_SPRITES['background'],(0,0))
        for upperPipes, lowerPipes in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipes['x'], upperPipes['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],(upperPipes['x'], upperPipes['y']))

        SCREEN.blit(GAME_SPRITES['base'],(basex,GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))

        mydigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in mydigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        xoffset = (SCREENWIDTH - width)/2

        for digit in  mydigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit], (xoffset, SCREENHEIGHT*0.12))
            xoffset += GAME_SPRITES["numbers"][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def iscollide(playerx, palyery, upperPipes, lowerPipes):
    if palyery > GROUNDY - 25 or palyery < 0:
        GAME_SOUND["hit"].play()
        return  True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if (palyery< pipeHeight + pipe["y"] and abs(playerx - pipe['x'])< GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUND['hit'].play()
            return True


    for pipe in lowerPipes:
        if (palyery + GAME_SPRITES['player'].get_height() > pipe["y"]) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUND['hit'].play()
            return True


    return False













def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT / 3
    max_height = SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset

    # Ensure max_height is positive
    if max_height > 0:
        y2 = offset + random.randrange(0, int(max_height))
    else:
        y2 = offset  # or some default value

    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},  # upper pipe
        {'x': pipeX, 'y': y2}    # lower pipe
    ]
    return pipe


if __name__=="__main__":
    pygame.init() # Initialise pygame modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird Game')
    GAME_SPRITES['numbers'] = (
        pygame.image.load('Flappy bird/resources/0.png').convert_alpha(),
        pygame.image.load('Flappy bird/resources/1.png').convert_alpha(),
        pygame.image.load('Flappy bird/resources/2.png').convert_alpha(),
        pygame.image.load('Flappy bird/resources/3.png').convert_alpha(),
        pygame.image.load('Flappy bird/resources/4.png').convert_alpha(),
        pygame.image.load('Flappy bird/resources/5.png').convert_alpha(),
        pygame.image.load('Flappy bird/resources/6.png').convert_alpha(),
        pygame.image.load('Flappy bird/resources/7.png').convert_alpha(),
        pygame.image.load('Flappy bird/resources/8.png').convert_alpha(),
        pygame.image.load('Flappy bird/resources/9.png').convert_alpha(),


    )

    GAME_SPRITES['message'] = pygame.image.load('resources/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('resources/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                            pygame.image.load(PIPE).convert_alpha())


    # game sounds
    GAME_SOUND['die'] = pygame.mixer.Sound('resources/stranger-things-124008.mp3')
    GAME_SOUND['point'] = pygame.mixer.Sound('resources/stranger-things-124008.mp3')
    GAME_SOUND['hit'] = pygame.mixer.Sound('resources/stranger-things-124008.mp3')
    GAME_SOUND['swoosh'] = pygame.mixer.Sound('resources/stranger-things-124008.mp3')
    GAME_SOUND['wing'] = pygame.mixer.Sound('resources/stranger-things-124008.mp3')

    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert()

    while True:
        Welcome_Screen() #shows welcome screen to the user until he presses a button
        mainGame()













