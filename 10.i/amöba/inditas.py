import pygame

# inicializáljuk a Pygame modult
pygame.init()

# beállítjuk a képernyő méretét
screen_width = 640
screen_height = 480

# létrehozzuk az ablakot
screen = pygame.display.set_mode((screen_width, screen_height))

# beállítjuk az ablak címét
pygame.display.set_caption("Gombok")

# beállítjuk a háttér színét
background_color = (255, 255, 255)
screen.fill(background_color)

# beállítjuk a gombok színét és méretét
button_color = (0, 0, 255)
button_width = 100
button_height = 50

# létrehozzuk a gombokat
button1 = pygame.draw.rect(screen, button_color, (50, 50, button_width, button_height))
button2 = pygame.draw.rect(screen, button_color, (250, 50, button_width, button_height))
button3 = pygame.draw.rect(screen, button_color, (450, 50, button_width, button_height))

# frissítjük az ablakot
pygame.display.flip()

# fő ciklus
running = True
while running:
    # eseménykezelés
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # ellenőrizzük, hogy az egér a gombokon van-e
            mouse_pos = pygame.mouse.get_pos()
            if button1.collidepoint(mouse_pos):
                print("Első gomb megnyomva!")
            elif button2.collidepoint(mouse_pos):
                print("Második gomb megnyomva!")
                #from amöba.twoplayer import *
            elif button3.collidepoint(mouse_pos):
                print("Harmadik gomb megnyomva!")

    # frissítjük az ablakot
    pygame.display.flip()

# kilépés a Pygame-ből
pygame.quit()
