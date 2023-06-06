import pygame

# Definiáljuk a színeket
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Definiáljuk a képernyő méretét
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

# Definiáljuk a cellák méretét és számát
CELL_SIZE = 100
ROWS = 3
COLS = 3

# Inicializáljuk a Pygame könyvtárat
pygame.init()

def game_over(board):
    """Meghatározza, hogy a játék véget ért-e."""
    for row in board:
        if None in row:
            return False
    return True

def get_winner(board):
    """Meghatározza a győztest, ha van. Ha nincs győztes, None-t ad vissza."""
    # Sorok ellenőrzése
    for row in board:
        if row[0] is not None and all(cell == row[0] for cell in row):
            return row[0]
    # Oszlopok ellenőrzése
    for col in range(COLS):
        if board[0][col] is not None and all(board[row][col] == board[0][col] for row in range(ROWS)):
            return board[0][col]
    # Átlók ellenőrzése
    if board[1][1] is not None and ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])):
        return board[1][1]
    # Ha nincs győztes
    return None


# Létrehozzuk a képernyőt
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Címet adunk az ablakunknak
pygame.display.set_caption("Amőba")

# Az X és O textúrák betöltése
x_texture = pygame.image.load('amöba\\x.png')
o_texture = pygame.image.load('amöba\\o.png')

# Az X és O textúrák átméretezése a cella méretére
x_texture = pygame.transform.scale(x_texture, (CELL_SIZE, CELL_SIZE))
o_texture = pygame.transform.scale(o_texture, (CELL_SIZE, CELL_SIZE))

# A játékmező inicializálása
board = [[None] * COLS for _ in range(ROWS)]

# A játékosok inicializálása
player1_turn = True
player1_color = BLUE
player2_color = RED

# A játék ciklusa
running = True
while running:
    # Eseménykezelés
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # Meghatározzuk a kattintás helyét a rácson
            pos = pygame.mouse.get_pos()
            col = pos[0] // CELL_SIZE
            row = pos[1] // CELL_SIZE
            # Ha az adott cella üres, és a játék még nem ért véget
            if board[row][col] is None and not game_over(board):
                # Az adott cella feltöltése az aktuális játékos által
                board[row][col] = 'X' if player1_turn else 'O'
                player1_turn = not player1_turn
    
    # A háttérszín beállítása
    screen.fill(WHITE)
    
    # A játéktábla kirajzolása
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)
            if board[row][col] == 'X':
                screen.blit(x_texture, rect)
            elif board[row][col] == 'O':
                screen.blit(o_texture, rect)

    # Ellenőrizzük, hogy van-e győztes
    winner = get_winner(board)
    if winner is not None:
        # A győztes színének beállítása
        winner_color = player1_color if winner == 'X' else player2_color
        # A győztes üzenet kirajzolása
        font = pygame.font.Font(None, 36)
        text = font.render(f"{winner} nyert!", True, winner_color)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)
    
    # Ha nincs győztes és a játék véget ért
    if game_over(board) and winner is None:
        # Az eredmény üzenet kirajzolása
        font = pygame.font.Font(None, 36)
        text = font.render("TIE GAME!", True, GRAY)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)

    # A frissítés és az újrarajzolás
    pygame.display.flip()

# Pygame leállítása
pygame.quit()
