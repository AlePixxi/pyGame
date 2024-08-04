import pygame
import sys
import random

from pygame.constants import *


pygame.init() # inizializazzione della libreria
 
FPS = 60 # salvioamo il valore che vogliamo di FPS
framePerSec = pygame.time.Clock() # creiamo un clock per poter dare un tempo sempre uguale al nostro game loop
 
# Colori di base
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Informazioni sulla finestra
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # creiamo effettivamente la finestra
DISPLAYSURF.fill(WHITE) # diamo un colore di sfondo
pygame.display.set_caption("Game") # impostiamo il titolo della finestra


'''
Di seguito andiamo a creare le classi per il player e per il nemico
'''

# Game Loop
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT: # se l'evento è quit, chiudiamo il gioco
            pygame.quit()
            sys.exit()

    # Metodi per aggiornare il giocatore e il nemico        
    P1.update()
    E1.move()
     
    DISPLAYSURF.fill(WHITE) # ricoloriamo la finestra di bianco
    P1.draw(DISPLAYSURF) # disegna il giocatore
    E1.draw(DISPLAYSURF) # disegna il nemico
         
    pygame.display.update()
    FramePerSec.tick(FPS)