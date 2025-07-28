import random
import sys
import pygame
from pygame.locals import *

# Global settings
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
GROUNDY = SCREENHEIGHT * 0.8

PLAYER = 'resources/bird.png'
BACKGROUND = 'resources/background.png'
PIPE = 'resources/pipe.png'

GAME_SPRITES = {}
GAME_SOUNDS = {}

def welcomeScreen():
    playerx = int(SCREENWIDTH / 5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height()) / 2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width()) / 2)
    messagey = int(SCREENHEIGHT * 0.13)
    while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN) and event.key in (K_ESCAPE,):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key in (K_SPACE, K_UP):
                return
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
        SCREEN.blit(GAME_SPRITES['base'], (0, GROUNDY))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(SCREENWIDTH / 5)
    playery = int(SCREENWIDTH / 2)
    pipeVelX = -4
    playerVelY = -9
    playerAccY = 1
    playerFlapAccv = -8
    playerFlapped = False

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    upperPipes = [{'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
                  {'x': SCREENWIDTH + 200 + SCREENWIDTH//2, 'y': newPipe2[0]['y']}]
    lowerPipes = [{'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
                  {'x': SCREENWIDTH + 200 + SCREENWIDTH//2, 'y': newPipe2[1]['y']}]

    while True:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN) and event.key in (K_ESCAPE,):
                pygame.quit(); sys.exit()
            if event.type == KEYDOWN and event.key in (K_SPACE, K_UP) and playery > 0:
                playerVelY = playerFlapAccv
                playerFlapped = True
                GAME_SOUNDS['wing'].play()

        if isCollide(playerx, playery, upperPipes, lowerPipes):
            return

        # Score logic
        playerMidPos = playerx + GAME_SPRITES['player'].get_width() / 2
        for pipe in upperPipes:
            pipeMid = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
            if pipeMid + 2 >= playerMidPos >= pipeMid - 2 and not pipe.get('scored'):
                score += 1
                pipe['scored'] = True
                GAME_SOUNDS['point'].play()

        if playerVelY < 10 and not playerFlapped:
            playerVelY += playerAccY
        if playerFlapped:
            playerFlapped = False

        playerHeight = GAME_SPRITES['player'].get_height()
        playery += min(playerVelY, GROUNDY - playery - playerHeight)

        for up, lp in zip(upperPipes, lowerPipes):
            up['x'] += pipeVelX
            lp['x'] += pipeVelX

        if 0 < upperPipes[0]['x'] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0]); lowerPipes.append(newpipe[1])
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0); lowerPipes.pop(0)

        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for up, lp in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0], (up['x'], up['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (lp['x'], lp['y']))
        SCREEN.blit(GAME_SPRITES['base'], (0, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

        digits = [int(d) for d in str(score)]
        totalWidth = sum(GAME_SPRITES['numbers'][d].get_width() for d in digits)
        offset = (SCREENWIDTH - totalWidth) / 2
        for d in digits:
            SCREEN.blit(GAME_SPRITES['numbers'][d], (offset, SCREENHEIGHT*0.12))
            offset += GAME_SPRITES['numbers'][d].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperPipes, lowerPipes):
    player_rect = GAME_SPRITES['player'].get_rect(topleft=(playerx, playery))
    if playery > GROUNDY - player_rect.height or playery < 0:
        GAME_SOUNDS['hit'].play()
        return True
    for up, lp in zip(upperPipes, lowerPipes):
        up_rect = GAME_SPRITES['pipe'][0].get_rect(topleft=(up['x'], up['y']))
        lp_rect = GAME_SPRITES['pipe'][1].get_rect(topleft=(lp['x'], lp['y']))
        if player_rect.colliderect(up_rect) or player_rect.colliderect(lp_rect):
            GAME_SOUNDS['hit'].play()
            return True
    return False

def getRandomPipe():
    offset = SCREENHEIGHT / 3
    pipe_h = GAME_SPRITES['pipe'][0].get_height()
    y2 = offset + random.randrange(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2 * offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipe_h - y2 + offset
    return [{'x': pipeX, 'y': -y1}, {'x': pipeX, 'y': y2}]

if __name__ == "__main__":
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))  # Must be before loading
    pygame.display.set_caption('Flappy Bird')
    FPSCLOCK = pygame.time.Clock()

    GAME_SPRITES['player'] = pygame.transform.scale(
        pygame.image.load(PLAYER).convert_alpha(), (34, 30)
    )
    GAME_SPRITES['numbers'] = tuple(
        pygame.image.load(f'resources/{i}_cleaned.png').convert_alpha() for i in range(10)
    )
    GAME_SPRITES['message'] = pygame.image.load('resources/message.png').convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load('resources/base.png').convert_alpha()
    GAME_SPRITES['pipe'] = (
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
        pygame.image.load(PIPE).convert_alpha()
    )
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()

    GAME_SOUNDS['hit'] = pygame.mixer.Sound('resources/Swoosh.mp3')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('resources/Swoosh.mp3')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('resources/Swoosh.mp3')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('resources/Swoosh.mp3')

    while True:
        welcomeScreen()
        mainGame()
