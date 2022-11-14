import pygame
import GameOfLife

# Initialize pygame
pygame.init()


# Color constants
GRAY = (50,50,50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_RED = (255,100,100)


# Grid constants & initializing the grid
ROWS = 80
COLS = 150
TILE_WIDTH = 4
TILE_HEIGHT = 4
MARGIN_SIZE = 1
gol = GameOfLife.gameoflifegrid(ROWS,COLS)



# Initialize the screen
WIDTH = 1200
HEIGHT = 600
WINDOW_SIZE = [WIDTH,HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game of Life +")

# Initialize button constants

HEADER_FONT = pygame.font.SysFont("Tahoma",30)
TITLE_TEXT = HEADER_FONT.render("GAME OF LIFE +", True, WHITE)
TITLE_X = 840
TITLE_Y = 30

BUTTON_FONT = pygame.font.SysFont("Tahoma",15)
# Clear grid button
CLEAR_GRID_TEXT = BUTTON_FONT.render("Clear Grid", True, BLACK)
CLEAR_GRID_X = 840
CLEAR_GRID_Y = 80
CLEAR_GRID_WIDTH = 220
CLEAR_GRID_HEIGHT = 20

# NOT gate button (0)
NOT_0_TEXT = BUTTON_FONT.render("Create a NOT Gate (0)", True, BLACK)
NOT_0_X = 840
NOT_0_Y = 130
NOT_0_WIDTH = 220
NOT_0_HEIGHT = 20

# NOT gate button (1)
NOT_1_TEXT = BUTTON_FONT.render("Create a NOT Gate with (1)", True, BLACK)
NOT_1_X = 840
NOT_1_Y = 160
NOT_1_WIDTH = 220
NOT_1_HEIGHT = 20

# AND gate button (00)
AND_00_TEXT = BUTTON_FONT.render("Create an AND Gate with (00)", True, BLACK)
AND_00_X = 840
AND_00_Y = 210
AND_00_WIDTH = 220
AND_00_HEIGHT = 20

# AND gate button (01)
AND_01_TEXT = BUTTON_FONT.render("Create an AND Gate with (01)", True, BLACK)
AND_01_X = 840
AND_01_Y = 240
AND_01_WIDTH = 220
AND_01_HEIGHT = 20

# AND gate button (10)
AND_10_TEXT = BUTTON_FONT.render("Create an AND Gate with (10)", True, BLACK)
AND_10_X = 840
AND_10_Y = 270
AND_10_WIDTH = 220
AND_10_HEIGHT = 20

# AND gate button (11)
AND_11_TEXT = BUTTON_FONT.render("Create an AND Gate with (11)", True, BLACK)
AND_11_X = 840
AND_11_Y = 300
AND_11_WIDTH = 220
AND_11_HEIGHT = 20





done = False
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
running = False
while not done:
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False
            # Change the x/y screen coordinates to grid coordinates
            column = x // (TILE_WIDTH + MARGIN_SIZE)
            row = y // (TILE_HEIGHT + MARGIN_SIZE)
            
            if x >= CLEAR_GRID_X and x <= CLEAR_GRID_X + CLEAR_GRID_WIDTH and y >= CLEAR_GRID_Y and y <= CLEAR_GRID_Y + CLEAR_GRID_HEIGHT:
                gol.clearGrid()
            
            if x >= NOT_0_X and x <= NOT_0_X + NOT_0_WIDTH and y >= NOT_0_Y and y <= NOT_0_Y + NOT_0_HEIGHT:
                gol.spawnNOTGate(False)
            if x >= NOT_1_X and x <= NOT_1_X + NOT_1_WIDTH and y >= NOT_1_Y and y <= NOT_1_Y + NOT_1_HEIGHT:
                gol.spawnNOTGate(True)
            
            if x >= AND_00_X and x <= AND_00_X + AND_00_WIDTH and y >= AND_00_Y and y <= AND_00_Y + AND_00_HEIGHT:
                gol.spawnANDGate(False,False)     
            if x >= AND_01_X and x <= AND_01_X + AND_01_WIDTH and y >= AND_01_Y and y <= AND_01_Y + AND_01_HEIGHT:
                gol.spawnANDGate(True,False)
            if x >= AND_10_X and x <= AND_10_X + AND_10_WIDTH and y >= AND_10_Y and y <= AND_10_Y + AND_10_HEIGHT:
                gol.spawnANDGate(False,True)
            if x >= AND_11_X and x <= AND_11_X + AND_11_WIDTH and y >= AND_11_Y and y <= AND_11_Y + AND_11_HEIGHT:
                gol.spawnANDGate(True,True)

      
            # Set that location to one
            if column in range(COLS) and row in range(ROWS):
                if gol.grid[row][column] == 1:
                    gol.grid[row][column] = 0
                    print("self.grid[" + str(row) + "][" + str(column) + "] = 0")
                else:
                    gol.grid[row][column] = 1
                    print("self.grid[" + str(row) + "][" + str(column) + "] = 1")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                running = False
                gol.nextstep()
            if event.key == pygame.K_SPACE:
                running = not running

    if running:
        gol.nextstep()
    # Set the screen background
    screen.fill(GRAY)
    # Draw the grid
    for row in range(ROWS):
        for column in range(COLS):
            color = WHITE
            if gol.grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN_SIZE + TILE_WIDTH) * column + MARGIN_SIZE,
                              (MARGIN_SIZE + TILE_HEIGHT) * row + MARGIN_SIZE,
                              TILE_WIDTH,
                              TILE_HEIGHT])

    # Limit to 60 frames per second
    clock.tick(30)

    # Draw UI
    screen.blit(TITLE_TEXT,(TITLE_X,TITLE_Y))
    
    if x >= CLEAR_GRID_X and x <= CLEAR_GRID_X + CLEAR_GRID_WIDTH and y >= CLEAR_GRID_Y and y <= CLEAR_GRID_Y + CLEAR_GRID_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,(CLEAR_GRID_X,CLEAR_GRID_Y,CLEAR_GRID_WIDTH,CLEAR_GRID_HEIGHT))
    else:
        pygame.draw.rect(screen,RED,(CLEAR_GRID_X,CLEAR_GRID_Y,CLEAR_GRID_WIDTH,CLEAR_GRID_HEIGHT))
    screen.blit(CLEAR_GRID_TEXT,(CLEAR_GRID_X,CLEAR_GRID_Y))
    
    
    if x >= NOT_0_X and x <= NOT_0_X + NOT_0_WIDTH and y >= NOT_0_Y and y <= NOT_0_Y + NOT_0_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,(NOT_0_X,NOT_0_Y,NOT_0_WIDTH,NOT_0_HEIGHT))
    else:
        pygame.draw.rect(screen,RED,(NOT_0_X,NOT_0_Y,NOT_0_WIDTH,NOT_0_HEIGHT))
    screen.blit(NOT_0_TEXT,(NOT_0_X,NOT_0_Y))
    if x >= NOT_1_X and x <= NOT_1_X + NOT_1_WIDTH and y >= NOT_1_Y and y <= NOT_1_Y + NOT_1_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,(NOT_1_X,NOT_1_Y,NOT_1_WIDTH,NOT_1_HEIGHT))
    else:
        pygame.draw.rect(screen,RED,(NOT_1_X,NOT_1_Y,NOT_1_WIDTH,NOT_1_HEIGHT))
    screen.blit(NOT_1_TEXT,(NOT_1_X,NOT_1_Y))
    
    
    
    if x >= AND_00_X and x <= AND_00_X + AND_00_WIDTH and y >= AND_00_Y and y <= AND_00_Y + AND_00_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,(AND_00_X,AND_00_Y,AND_00_WIDTH,AND_00_HEIGHT))
    else:
        pygame.draw.rect(screen,RED,(AND_00_X,AND_00_Y,AND_00_WIDTH,AND_00_HEIGHT))
    screen.blit(AND_00_TEXT,(AND_00_X,AND_00_Y))
    if x >= AND_01_X and x <= AND_01_X + AND_01_WIDTH and y >= AND_01_Y and y <= AND_01_Y + AND_01_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,(AND_01_X,AND_01_Y,AND_01_WIDTH,AND_01_HEIGHT))
    else:
        pygame.draw.rect(screen,RED,(AND_01_X,AND_01_Y,AND_01_WIDTH,AND_01_HEIGHT))
    screen.blit(AND_01_TEXT,(AND_01_X,AND_01_Y))
    if x >= AND_10_X and x <= AND_10_X + AND_10_WIDTH and y >= AND_10_Y and y <= AND_10_Y + AND_10_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,(AND_10_X,AND_10_Y,AND_10_WIDTH,AND_10_HEIGHT))
    else:
        pygame.draw.rect(screen,RED,(AND_10_X,AND_10_Y,AND_10_WIDTH,AND_10_HEIGHT))
    screen.blit(AND_10_TEXT,(AND_10_X,AND_10_Y))
    if x >= AND_11_X and x <= AND_11_X + AND_11_WIDTH and y >=AND_11_Y and y <= AND_11_Y + AND_11_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,(AND_11_X,AND_11_Y,AND_11_WIDTH,AND_11_HEIGHT))
    else:
        pygame.draw.rect(screen,RED,(AND_11_X,AND_11_Y,AND_11_WIDTH,AND_11_HEIGHT))
    screen.blit(AND_11_TEXT,(AND_11_X,AND_11_Y))
    
    

    
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()

# if alive - two or three live neighbors - stays alive
# if exactly 3 neighbors, dead becomes alive
