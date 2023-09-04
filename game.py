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

# def checkNotCollition() -> bool:
#     if checkCollition() == False:
#         lives-=1
#         if lives == 0:
#             screen.fill("red")
#             score = "You lose!"


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                if checkCollition():
                    score += 1
                    circlePos = (random.randint(0, 1280),
                                 random.randint(0, 720))

    score_label = font.render(f'Score: {score}', True, "black")
    screen.fill('lightgreen')
    pygame.draw.circle(screen, "red", circlePos, 50)
    screen.blit(score_label, (25, 25))
    pygame.display.update()
