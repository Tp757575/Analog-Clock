# Først importeres de nødvendige libraies
import pygame 
import math
import datetime as datetime

# Aktivere pygame (initialize)
pygame.init()

# Der defineres en skærm
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
pygame.display.set_caption("Clock")

# Her defineres nogle konstanter
CENTER = (320, 240)

# Tegner ydresiden af cirklen
pygame.draw.circle(screen, (0, 0, 0), (CENTER), (220), (4))

# Tegner tallene langs den ydrestecirkel
font = pygame.font.SysFont(None, 30)

# Tegner pilene til sekund-, minut- og timeviser.
end_x = CENTER[0] + int(140 * math.sin(270))
end_y = CENTER[1] - int(140 * math.cos(270))
pygame.draw.line(screen, (0, 180, 100), CENTER, (end_x, end_y), 6)

# Står for at holde programmet kørende og mulig gøre det at lukke fanen ned.
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()