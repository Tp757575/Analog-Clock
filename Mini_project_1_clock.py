# Først importeres de nødvendige biblioteker
import pygame 
import math
import datetime as datetime

# Aktivere pygame (initialize)
pygame.init()

# Der defineres en skærm med størrelse 640x480 og baggrundsfarven sættes til hvid
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
pygame.display.set_caption("Analog Clock")  # Vinduet får navnet "Analog Clock"

# Her defineres nogle konstanter for at gøre de fremtidige funktioner mere overskuelige
CENTER = (320, 240) 
RADIUS = 210 
hvid = (255, 255, 255) 
sort = (0, 0, 0) 
orange = (255, 156, 10)  
grøn = (10, 155, 10)  
blå = (10, 10, 255)  

# EEt loop for at holde programmet kørende
while True:
    screen.fill((255, 255, 255))
    
    # Tegner den ydre cirkel for uret
    pygame.draw.circle(screen, sort, CENTER, RADIUS, 4)

    # Skriftstørrelse for tallene
    font = pygame.font.SysFont(None, 40)  

    # Timemarkeringer tegnes på urskiven med fokus på den rette placering
    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(-90)))  
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(-90)))
    screen.blit(font.render("12", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(30 - 90))) 
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(30 - 90)))
    screen.blit(font.render("1", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(60 - 90)))  
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(60 - 90)))
    screen.blit(font.render("2", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(90 - 90)))  
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(90 - 90)))
    screen.blit(font.render("3", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(120 - 90)))  
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(120 - 90)))
    screen.blit(font.render("4", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(150 - 90))) 
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(150 - 90)))
    screen.blit(font.render("5", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(180 - 90)))  
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(180 - 90)))
    screen.blit(font.render("6", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(210 - 90)))  
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(210 - 90)))
    screen.blit(font.render("7", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(240 - 90)))
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(240 - 90)))
    screen.blit(font.render("8", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(270 - 90))) 
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(270 - 90)))
    screen.blit(font.render("9", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(300 - 90)))  
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(300 - 90)))
    screen.blit(font.render("10", True, sort), (x - 10, y - 10))

    x = CENTER[0] + int((RADIUS - 30) * math.cos(math.radians(330 - 90)))  
    y = CENTER[1] + int((RADIUS - 30) * math.sin(math.radians(330 - 90)))
    screen.blit(font.render("11", True, sort), (x - 10, y - 10))

    # Henter aktuelle timer, minutter og sekunder fra systemets eget ur
    s = datetime.datetime.now().second
    m = datetime.datetime.now().minute
    h = datetime.datetime.now().hour

    # Tegner sekundviseren
    angle = 360 / 60 * s + 270  # Beregner vinkel for sekundviseren
    new_position = [RADIUS * math.cos(math.radians(angle)), RADIUS * math.sin(math.radians(angle))]
    end_position = (CENTER[0] + new_position[0] * 0.8, CENTER[1] + new_position[1] * 0.8) # Viseren forkortes lidt for at fremstå pænere på uret
    pygame.draw.line(screen, blå, CENTER, end_position, 3)  # Tegner sekundviseren

    # Det der gøres for skeundviseren gentages for både minut- og timeviseren

    # Tegner minutviser
    angle = 360 / 60 * m + 270 
    new_position = [RADIUS * math.cos(math.radians(angle)), RADIUS * math.sin(math.radians(angle))]
    end_position = (CENTER[0] + new_position[0] * 0.7, CENTER[1] + new_position[1] * 0.7)  
    pygame.draw.line(screen, grøn, CENTER, end_position, 3) 

    # Tegner timeviser
    angle = h % 12 * 30 - 90 + m * 0.5  # (inkluderer minutter for præcis vinkel)
    new_position = [RADIUS * math.cos(math.radians(angle)), RADIUS * math.sin(math.radians(angle))]
    end_position = (CENTER[0] + new_position[0] * 0.6, CENTER[1] + new_position[1] * 0.6)  
    pygame.draw.line(screen, orange, CENTER, end_position, 8) 

    # Opdaterer skærmen med de nye elementer
    pygame.display.flip()

    # Gør det muligt at lukke programmet ved at trykke på krydset
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
