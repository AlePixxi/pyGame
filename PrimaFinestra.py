import pygame # importiamo la libreria 
from pygame.locals import *  # importiamo delle variabili comuni che faranno comodo nel corso dello sviluppo
import sys


pygame.init() # inizializza la libreria. Obbligatoria, prima di tutto

DISPLAY_SURF = pygame.display.set_mode((600,600)) # andiamo a definire la superficie della nostra finestra

# Andiamo a crearci dei colori di base che ci faranno comodo nel corso dello sviluppo
color1 = pygame.Color(0, 0, 0)         # Black
color2 = pygame.Color(255, 255, 255)   # White
color3 = pygame.Color(128, 128, 128)   # Grey
color4 = pygame.Color(255, 0, 0)       # Red

# Game Loop, qui è dove avviene l'intero ciclo di vita del gioco
while True:

    # codice vario
    # ...

    '''Un "Evento" Pygame si verifica quando l'utente esegue un'azione specifica, 
    come cliccare con il mouse o premere un pulsante della tastiera. 
    Pygame registra ogni singolo evento che si verifica. 
    Tuttavia, non farà davvero nulla con queste informazioni perché quella parte spetta a noi.'''
    for event in pygame.event.get(): # itera su tutti gli eventi in corso di pygame
        # se l'evento è QUIT allora chiudi il gioco
        if event.type == QUIT:
            pygame.quit() # chiudi la finestra pygame
            sys.exit() # interrompi lo script

    ''' Questo ci permette di avere un limite al numero di cicli al secondo che il nostro
     gioco andrebbe a fare, abbiamo impostato 60 tick al secondo. 
     Sostanzialmente andiamo a defini il numeor di fps masssimo che il nostro gioco potrà raggiungere'''
    FPS = pygame.time.Clock()
    FPS.tick(60)

    pygame.display.update() # questa funzione è responsabile dell'aggiornamento della finestra, senza di questa non si vedrebbero le modifiche
