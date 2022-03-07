import random
import sys
import os
import pygame
import time
from pygame.locals import *

# Global Variables
FPS = 32
SCREENWIDTH = 1200
SCREENHEIGHT = 675
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 0
BACKGROUND = 0
PIPE = 0
BASE = 0

# Font Specification
pygame.font.init()
font = pygame.font.SysFont(None , 60 , italic=True , bold=True)
def text_screen(text , color , x , y):
    screen_text = font.render(text , True , color)
    SCREEN.blit(screen_text , [x,y])

# Welcome Screen
def welcomeScreen():
    while True:
        SCREEN.blit(GAME_SPRITES['mode1'], (0, 0))
        SCREEN.blit(GAME_SPRITES['message'], (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                mode1()
                return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# MODE 1
def mode1():
    while True:
        SCREEN.blit(GAME_SPRITES['mode1'], (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and event.key == K_RIGHT:
                mode2()
                return

            elif event.type == KEYDOWN and (event.key == K_RETURN):
                mode1ms()
                return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# Mode Message 1
def mode1ms():
    while True:
        SCREEN.blit(GAME_SPRITES['mode1ms'], (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE):
                PLAYER = 'Sprites/player1.png'
                GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
                BACKGROUND = 'Sprites/bg1.png'
                GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
                BASE = 'Sprites/base1.png'
                GAME_SPRITES['base'] = pygame.image.load(BASE).convert_alpha()
                PIPE = 'Sprites/pipe1.png'
                GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                                        pygame.image.load(PIPE).convert_alpha())
                return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# MODE 2
def mode2():
    while True:
        SCREEN.blit(GAME_SPRITES['mode2'], (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and event.key == K_LEFT:
                mode1()
                return

            elif event.type == KEYDOWN and event.key == K_RIGHT:
                mode3()
                return

            elif event.type == KEYDOWN and (event.key == K_RETURN):
                mode2ms()
                return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# Mode Message 2
def mode2ms():
    while True:
        SCREEN.blit(GAME_SPRITES['mode2ms'], (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE):
                PLAYER = 'Sprites/player2.png'
                GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
                BACKGROUND = 'Sprites/bg2.jpg'
                GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
                BASE = 'Sprites/base2.png'
                GAME_SPRITES['base'] = pygame.image.load(BASE).convert_alpha()
                PIPE = 'Sprites/pipe2.png'
                GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                                        pygame.image.load(PIPE).convert_alpha())
                return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# MODE 3
def mode3():
    while True:
        SCREEN.blit(GAME_SPRITES['mode3'], (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type ==KEYDOWN and event.key == K_LEFT:
                mode2()
                return

            elif event.type == KEYDOWN and event.key == K_RIGHT:
                mode4()
                return

            elif event.type == KEYDOWN and (event.key == K_RETURN):
                mode3ms()
                return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# Mode Message 3
def mode3ms():
    while True:
        SCREEN.blit(GAME_SPRITES['mode3ms'], (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE):
                PLAYER = 'Sprites/player3.png'
                GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
                BACKGROUND = 'Sprites/bg3.jfif'
                GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
                BASE = 'Sprites/base3.png'
                GAME_SPRITES['base'] = pygame.image.load(BASE).convert_alpha()
                PIPE = 'Sprites/pipe3.png'
                GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                                        pygame.image.load(PIPE).convert_alpha())
                return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# MODE 4
def mode4():
    while True:
        SCREEN.blit(GAME_SPRITES['mode4'], (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and event.key == K_LEFT:
                mode3()
                return

            elif event.type == KEYDOWN and (event.key == K_RETURN):
                mode4ms()
                return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# Mode Message 4
def mode4ms():
    while True:
        SCREEN.blit(GAME_SPRITES['mode4ms'], (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN and (event.key == K_SPACE):
                PLAYER = 'Sprites/player4.png'
                GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
                BACKGROUND = 'Sprites/bg4.png'
                GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
                BASE = 'Sprites/base4.png'
                GAME_SPRITES['base'] = pygame.image.load(BASE).convert_alpha()
                PIPE = 'Sprites/pipe4.png'
                GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                                        pygame.image.load(PIPE).convert_alpha())
                return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# Game Over Screen
def GameOver():
    flag = 0
    GAME_SOUNDS['die'].play()
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    with open("score.txt", "r") as fs:
        score = fs.read()
    while True:
        SCREEN.blit(GAME_SPRITES['GameOver'],(0,0))
        if int(score) > int(highscore):
            flag = 1
            highscore = score
            with open("highscore.txt", "w") as fh:
                fh.write(str(highscore))

        if flag == 1:
            text_screen("Hurray !   NEW HIGHSCORE", (255, 255, 255), 270, 290)
        text_screen(f"{score}", (255, 255, 255) , 675 , 168)
        text_screen(f"{highscore}", (255, 255, 255), 725, 230)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# MAIN GAME
def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/4)
    playery = int(SCREENHEIGHT/2)
    basex = 0

    # Creating new pipes
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()
    newPipe3 = getRandomPipe()
    newPipe4 = getRandomPipe()

    # List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH/2, 'y': newPipe1[0]['y']},
        {'x': (SCREENWIDTH/2)+(SCREENWIDTH/4), 'y': newPipe2[0]['y']},
        {'x': SCREENWIDTH, 'y': newPipe3[0]['y']},
        {'x': SCREENWIDTH+(SCREENWIDTH/4), 'y': newPipe4[0]['y']}
    ]

    # List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH/2, 'y': newPipe1[1]['y']},
        {'x': (SCREENWIDTH/2)+(SCREENWIDTH/4), 'y': newPipe2[1]['y']},
        {'x': SCREENWIDTH, 'y': newPipe3[1]['y']},
        {'x': SCREENWIDTH + (SCREENWIDTH / 4), 'y': newPipe4[1]['y']}
    ]

    pipeVelX = -4
    pipeMaxVelX = -12
    rng = 5

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccVel = -8  # velocity while flapping
    playerFlapped = False  # flag variable

    # check if highsore file exist
    if not os.path.exists("highscore.txt"):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    if not os.path.exists("score.txt"):
        with open("score.txt", "w") as fs:
            fs.write("0")

    while True:
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        if crashTest:
            with open("score.txt","w") as fs:
                fs.write(str(score))
            return

        else:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    if playery > 0:
                        playerVelY = playerFlapAccVel
                        playerFlapped = True
                        GAME_SOUNDS['wing'].play()

            # score
            playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
            for pipe in upperPipes:
                pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
                if pipeMidPos <= playerMidPos < pipeMidPos + rng - 1:
                    score += 1
                    GAME_SOUNDS['point'].play()

                    if pipeVelX > pipeMaxVelX :
                        if score % 5 == 0:
                            pipeVelX -= 1
                            rng += 1

            if playerVelY < playerMaxVelY and not playerFlapped:
                playerVelY += playerAccY

            if playerFlapped:
                playerFlapped = False
            playerHeight = GAME_SPRITES['player'].get_height()
            playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

            # move pipes to the left
            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                upperPipe['x'] += pipeVelX
                lowerPipe['x'] += pipeVelX

            # Adding a new pipe when the first is about to cross the leftmost part of the screen
            if 0 < upperPipes[0]['x'] < rng:
                newpipe = getRandomPipe()
                upperPipes.append(newpipe[0])
                lowerPipes.append(newpipe[1])

            # Removing the pipes which are out of screen
            if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
                upperPipes.pop(0)
                lowerPipes.pop(0)

            # blitting sprites
            SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
                SCREEN.blit(GAME_SPRITES['pipe'][0],
                            (upperPipe['x'], upperPipe['y']))
                SCREEN.blit(GAME_SPRITES['pipe'][1],
                            (lowerPipe['x'], lowerPipe['y']))

            SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
            SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))

            # Score Blitting
            myDigits = [int(x) for x in list(str(score))]
            width = 0
            for digit in myDigits:
                width += GAME_SPRITES['numbers'][digit].get_width()
            Xoffset = (SCREENWIDTH - width)/2

            for digit in myDigits:
                SCREEN.blit(GAME_SPRITES['numbers'][digit],
                            (Xoffset, SCREENHEIGHT*0.12))
                Xoffset += GAME_SPRITES['numbers'][digit].get_width()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    pygame.quit()
    quit()

# Colliding
def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > (GROUNDY - 55) or playery < 0:
        GAME_SOUNDS['hit'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

# For Getting Random Pipes
def getRandomPipe():
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = 50 + SCREENHEIGHT/3
    y2 = (offset) + random.randint(0, int(SCREENHEIGHT - GAME_SPRITES['base'].get_height() - 1.2* offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset - 50
    pipe = [
        {'x': pipeX, 'y': -y1},  # upper Pipe
        {'x': pipeX, 'y': y2}  # lower Pipe
    ]
    return pipe

# Main Function
if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flapping Mads')

    # GAME SPRITES
    GAME_SPRITES['message'] = pygame.image.load('Sprites/welcome.png').convert_alpha()

    GAME_SPRITES['mode1'] = pygame.image.load('Sprites/mode1.png').convert_alpha()
    GAME_SPRITES['mode2'] = pygame.image.load('Sprites/mode2.png').convert_alpha()
    GAME_SPRITES['mode3'] = pygame.image.load('Sprites/mode3.png').convert_alpha()
    GAME_SPRITES['mode4'] = pygame.image.load('Sprites/mode4.png').convert_alpha()

    GAME_SPRITES['mode1ms'] = pygame.image.load('Sprites/mode1_ms.png').convert_alpha()
    GAME_SPRITES['mode2ms'] = pygame.image.load('Sprites/mode2_ms.png').convert_alpha()
    GAME_SPRITES['mode3ms'] = pygame.image.load('Sprites/mode3_ms.png').convert_alpha()
    GAME_SPRITES['mode4ms'] = pygame.image.load('Sprites/mode4_ms.png').convert_alpha()

    GAME_SPRITES['numbers'] = (
        pygame.image.load('Sprites/0.png').convert_alpha(),
        pygame.image.load('Sprites/1.png').convert_alpha(),
        pygame.image.load('Sprites/2.png').convert_alpha(),
        pygame.image.load('Sprites/3.png').convert_alpha(),
        pygame.image.load('Sprites/4.png').convert_alpha(),
        pygame.image.load('Sprites/5.png').convert_alpha(),
        pygame.image.load('Sprites/6.png').convert_alpha(),
        pygame.image.load('Sprites/7.png').convert_alpha(),
        pygame.image.load('Sprites/8.png').convert_alpha(),
        pygame.image.load('Sprites/9.png').convert_alpha(),
    )

    GAME_SPRITES['GameOver'] = pygame.image.load('Sprites/gameover.png').convert_alpha()

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('Audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('Audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('Audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('Audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('Audio/wing.wav')

    while True:
        welcomeScreen()
        mainGame()
        time.sleep(3)
        GameOver()