import pygame
import sys
import random
import time

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
SPEED = 5

SCORE = 0

# Impostazione del font
## creiamo due tipi di font, uno più grande e uno più piccolo
font = pygame.font.SysFont("Verdana", 60) 
font_small = pygame.font.SysFont("Verdana", 20)
# andiamo a renderizzare il nostro font, sostanzialmente creando una Surface, con una stringa che rappresenta la scritta, l'antialiasing e il colore
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png") # carichiamo l'immagine di sfondo
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # creiamo effettivamente la finestra
DISPLAYSURF.fill(WHITE) # diamo un colore di sfondo
pygame.display.set_caption("Game") # impostiamo il titolo della finestra


'''
Di seguito andiamo a creare le classi per il player e per il nemico
'''

class Enemy(pygame.sprite.Sprite):
    def __init__(self,) -> None:
        super().__init__()
        self.image = pygame.image.load("Enemy.png") # quando si chiama il costruttore del nemico, si carica anche lo sprite
        self.rect = self.image.get_rect() # prendiamo il rect (per le collisioni) ottenendolo dall'immagine
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)  # impostiamo il centro del rettangolo in una posizione X random
    
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) # muovi il rettangolo del nemico sull'asse y di 10

        # se il bordo inferiore del rettangolo arriva al limite inferiore della finestra, torna in cima e dai una nuova posizione X random
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect) # disegna la superficie, con quella imagine, nella posizione del rettangolo


class Player(pygame.sprite.Sprite):
    def __init__(self,) -> None:
        super().__init__()
        self.image = pygame.image.load("Player.png") # quando si chiama il costruttore del giocatore, si carica anche lo sprite
        self.rect = self.image.get_rect() # prendiamo il rect (per le collisioni) ottenendolo dall'immagine
        self.rect.center = (SCREEN_WIDTH/2, 520) # impostiamo il centro del rettangolo in una possizione X random

    def move(self): # prima si chiamava update, con move lo uniformiamo al nemico, per muoverli in gruppo
        pressed_keys = pygame.key.get_pressed() # prendiamo la lista di tasti premuti

        if (self.rect.left > 0): # se il rect del player non sta sul bordo sinsitro della finestra
            if (pressed_keys[K_LEFT]): # se tra i tasti premuti c'è left
                self.rect.move_ip(-5, 0) # muovi di 5 a sinsitra il rettangolo

        if (self.rect.right < SCREEN_WIDTH): # se il rect del player non sta sul bordo destro della finestra    
            if (pressed_keys[K_RIGHT]): # se tra i tasti premuti c'è right
                self.rect.move_ip(5, 0) # muovi il rect di 5 verso destra
    
    def draw(self, surface: pygame.surface.Surface):
        surface.blit(self.image, self.rect) # disegna la superficie


# istanze di giocatore e nemico
P1 = Player()
E1 = Enemy()

# Creiamo due sprite group
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# creiamo un nuovo evento utente
INC_SPEED = pygame.USEREVENT + 1  # aumentiamo di 1 la variabile che conta il numero di eventi utente in modo che possiamo associare il nostro evento ad un numero
pygame.time.set_timer(INC_SPEED, 1000) # settiamo un timer per far eseguire l'evento ogni 1000 millisecondi

# Game Loop
while True:     
    for event in pygame.event.get():

        if event.type == INC_SPEED: # se l'evento è INC_SPEED, quindi quello creato da noi che parte ogni secondo
            SPEED += 2 # aumenta di 2 la velocità (del nemico)

        if event.type == QUIT: # se l'evento è quit, chiudiamo il gioco
            pygame.quit()
            sys.exit()

    #  vecchi Metodi per aggiornare il giocatore e il nemico        
    # P1.update()
    # E1.move()
    
    '''
    è importante disegnare le cose sullo schermo in un determinato ordine in modo da non sovrapporle
    nel modo sbagliato (es.: prima disegnamo lo sfondo e sopra ci disegnamo il punteggio)
    '''
    DISPLAYSURF.blit(background, (0,0)) # disegna l'immagine ad una certa posizione
    scores = font_small.render(str(SCORE), True, BLACK)  # crea una nuova surface con il punteggio
    DISPLAYSURF.blit(scores, (10,10)) # mostra sullo schermo il punteggio
    
    # vecchi metodo per ridisegnare  gli sprtites
    # P1.draw(DISPLAYSURF) # disegna il giocatore
    # E1.draw(DISPLAYSURF) # disegna il nemico

    # Muovere e ridisegnare tutti gli sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Controlliamo le collisioni tra il player e il nemico
    if pygame.sprite.spritecollideany(P1, enemies): # controlla se lo srte collida con un Group e ritorna la lista di ogni sprite con il quale collide
        pygame.mixer.Sound('crash.wav').play()
        DISPLAYSURF.fill(RED) # schermo rosso
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update() # aggiorna lo schermo

        # riuovi tutti gli sprite dal gioco
        for entity in all_sprites:
            entity.kill()
        
        time.sleep(2) # attendi due secondi
        # chiudi tutto
        pygame.quit()
        sys.exit()
         
    pygame.display.update() # aggiorna la finestra
    framePerSec.tick(FPS) # fai un tick del clock, questo permette di ridurre il nuemro di cicli sguendo un determinato timing