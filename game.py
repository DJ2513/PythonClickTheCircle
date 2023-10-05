import pygame
import sys
import math
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))

circlePos = (1280/2, 720/2)

font = pygame.font.Font(None, 30)

score = 0
lives = 3


def checkCollition() -> bool:
    mousePos = pygame.mouse.get_pos()

    if math.sqrt((mousePos[0] - circlePos[0])**2 + (mousePos[1] - circlePos[1])**2) <= 50:
        return True
    return False

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                if checkCollition():
                    score += 1
                    circlePos = (random.randint(0, 1280), random.randint(0, 720))
                else:
                    lives -= 1

    score_label = font.render(f'Score: {score}', True, "black")
    lives_label = font.render(f'Lives: {lives} ', True, "black")
    overalScore_label = font.render(f'Your score was: {score} points!', True, 'white')
    gameOver_label = font.render(f'GAME OVER!', True, 'white')
    screen.fill('lightgreen')
    pygame.draw.circle(screen, "red", circlePos, 50)
    screen.blit(score_label, (25, 25))
    screen.blit(lives_label, (1100, 25))
    if lives <= 0:
        screen.fill('black')
        screen.blit(gameOver_label, (570, 350))
        screen.blit(overalScore_label, (520, 400))
    pygame.display.update()
