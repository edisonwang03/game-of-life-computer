import pygame
import GameOfLife

# Initialize pygame
pygame.init()


# Color constants
GRAY = (50,50,50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_RED = (155,0,0)


# Grid constants & initializing the grid
ROWS = 100
COLS = 100
TILE_WIDTH = 6
TILE_HEIGHT = 6
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

# NOT gate without input button
NOT_OFF_TEXT = BUTTON_FONT.render("Create a NOT Gate without input", True, BLACK)
NOT_OFF_X = 840
NOT_OFF_Y = 130
NOT_OFF_WIDTH = 220
NOT_OFF_HEIGHT = 20

# NOT gate with input button
NOT_ON_TEXT = BUTTON_FONT.render("Create a NOT Gate with input", True, BLACK)
NOT_ON_X = 840
NOT_ON_Y = 160
NOT_ON_WIDTH = 220
NOT_ON_HEIGHT = 20





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
            
            if x >= NOT_OFF_X and x <= NOT_OFF_X + NOT_OFF_WIDTH and y >= NOT_OFF_Y and y <= NOT_OFF_Y + NOT_OFF_HEIGHT:
                gol.makeNOTGateWithoutInput()
                
            if x >= NOT_ON_X and x <= NOT_ON_X + NOT_ON_WIDTH and y >= NOT_ON_Y and y <= NOT_ON_Y + NOT_ON_HEIGHT:
                gol.makeNOTGateWithInput()
      
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
    
    if x >= NOT_OFF_X and x <= NOT_OFF_X + NOT_OFF_WIDTH and y >= NOT_OFF_Y and y <= NOT_OFF_Y + NOT_OFF_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,(NOT_OFF_X,NOT_OFF_Y,NOT_OFF_WIDTH,NOT_OFF_HEIGHT))
    else:
        pygame.draw.rect(screen,RED,(NOT_OFF_X,NOT_OFF_Y,NOT_OFF_WIDTH,NOT_OFF_HEIGHT))
    screen.blit(NOT_OFF_TEXT,(NOT_OFF_X,NOT_OFF_Y))
    
    if x >= NOT_ON_X and x <= NOT_ON_X + NOT_ON_WIDTH and y >= NOT_ON_Y and y <= NOT_ON_Y + NOT_ON_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,(NOT_ON_X,NOT_ON_Y,NOT_ON_WIDTH,NOT_ON_HEIGHT))
    else:
        pygame.draw.rect(screen,RED,(NOT_ON_X,NOT_ON_Y,NOT_ON_WIDTH,NOT_ON_HEIGHT))
    screen.blit(NOT_ON_TEXT,(NOT_ON_X,NOT_ON_Y))
    
    if x >= CLEAR_GRID_X and x <= CLEAR_GRID_X + CLEAR_GRID_WIDTH and y >= CLEAR_GRID_Y and y <= CLEAR_GRID_Y + CLEAR_GRID_HEIGHT:
        pygame.draw.rect(screen,LIGHT_RED,(CLEAR_GRID_X,CLEAR_GRID_Y,CLEAR_GRID_WIDTH,CLEAR_GRID_HEIGHT))
    else:
        pygame.draw.rect(screen,RED,(CLEAR_GRID_X,CLEAR_GRID_Y,CLEAR_GRID_WIDTH,CLEAR_GRID_HEIGHT))
    screen.blit(CLEAR_GRID_TEXT,(CLEAR_GRID_X,CLEAR_GRID_Y))
    
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()

# if alive - two or three live neighbors - stays alive
# if exactly 3 neighbors, dead becomes alive
