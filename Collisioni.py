import pygame

''' in ogni gioco bisogna gestire dei condini ai nostri oggetti,
in modo da avere un modo per gestire eventuali collisioni o interazioni varie tra due o più
elementi del nostro gioco. Esempio, il giocatore che raccoglie un oggetto o che attacca un nemico.

Esistono diversi modi per controllare questo tipo di eventi, vediamone alcuni '''

# collisione tra due rettangoli
# creiamo due rettangoli. 
# Il costruttore di rect vuole due tuple, la prima èmla posizione (left, top), la seconda è la dimensione (w, h)
object1 = pygame.Rect((20, 50), (50, 100))
object2 = pygame.Rect((10, 10), (100, 100))

# funzione della classe Rect che restituisce True se il Rect collide con un altro Rect
print(object1.colliderect(object2))

# Collisione tra un rettangolo e una coordinata
object1 = pygame.Rect((20, 50), (50, 100))
 
print(object1.collidepoint(50, 75)) # basta passare la coordinata del punto da controllare