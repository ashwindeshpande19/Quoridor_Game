#Code for the game board
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the game board
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 9  # 9x9 grid for two-player Quoridor
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE  # Each cell will be square

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Quoridor Game Board")

def draw_grid():
    """Draws the grid lines on the game board."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Draw the borders of the cell

# def main():
#     """Main game loop."""
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         # Fill the background with grey color
#         screen.fill(GREY)

#         # Draw the grid
#         draw_grid()

#         # Update the display
#         pygame.display.update()

# if __name__ == "__main__":
#     main()


# Code for the game logic

# Constants
WIDTH, HEIGHT = 600, 600  # Window size
GRID_SIZE = 9  # 9x9 board
SQUARE_SIZE = WIDTH // GRID_SIZE  # Size of each square

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (169, 169, 169)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quoridor")

# Game Board
board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Player Positions
player1_pos = [0, 4]  # Player 1 starts at top center
player2_pos = [8, 4]  # Player 2 starts at bottom center

# Wall positions (horizontal and vertical walls)
horizontal_walls = []
vertical_walls = []

# Current player turn (Player 1 = True, Player 2 = False)
current_player = True

# Function to draw the board
def draw_board():
    screen.fill(WHITE)
    
    # Draw grid lines
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            pygame.draw.rect(screen, BLACK, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 1)
    
    # Draw players
    pygame.draw.circle(screen, BLUE, (player1_pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, player1_pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)
    pygame.draw.circle(screen, RED, (player2_pos[1] * SQUARE_SIZE + SQUARE_SIZE // 2, player2_pos[0] * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)

    # Draw walls
    for wall in horizontal_walls:
        pygame.draw.rect(screen, GREY, (wall[1] * SQUARE_SIZE, wall[0] * SQUARE_SIZE + SQUARE_SIZE - 5, SQUARE_SIZE * 2, 10))
    
    for wall in vertical_walls:
        pygame.draw.rect(screen, GREY, (wall[1] * SQUARE_SIZE + SQUARE_SIZE - 5, wall[0] * SQUARE_SIZE, 10, SQUARE_SIZE * 2))

# Check if movement is valid
def is_valid_move(player_pos, direction):
    x, y = player_pos
    if direction == 'UP' and x > 0:
        return True
    if direction == 'DOWN' and x < GRID_SIZE - 1:
        return True
    if direction == 'LEFT' and y > 0:
        return True
    if direction == 'RIGHT' and y < GRID_SIZE - 1:
        return True
    return False

# Move player
def move_player(player_pos, direction):
    if direction == 'UP':
        player_pos[0] -= 1
    elif direction == 'DOWN':
        player_pos[0] += 1
    elif direction == 'LEFT':
        player_pos[1] -= 1
    elif direction == 'RIGHT':
        player_pos[1] += 1

# Handle player turns
def handle_turn():
    global current_player
    
    # Get player input for movement or wall placement
    keys = pygame.key.get_pressed()

    if current_player:  # Player 1's turn
        if keys[pygame.K_w] and is_valid_move(player1_pos, 'UP'):
            move_player(player1_pos, 'UP')
            current_player = False
        elif keys[pygame.K_s] and is_valid_move(player1_pos, 'DOWN'):
            move_player(player1_pos, 'DOWN')
            current_player = False
        elif keys[pygame.K_a] and is_valid_move(player1_pos, 'LEFT'):
            move_player(player1_pos, 'LEFT')
            current_player = False
        elif keys[pygame.K_d] and is_valid_move(player1_pos, 'RIGHT'):
            move_player(player1_pos, 'RIGHT')
            current_player = False

    else:  # Player 2's turn
        if keys[pygame.K_UP] and is_valid_move(player2_pos, 'UP'):
            move_player(player2_pos, 'UP')
            current_player = True
        elif keys[pygame.K_DOWN] and is_valid_move(player2_pos, 'DOWN'):
            move_player(player2_pos, 'DOWN')
            current_player = True
        elif keys[pygame.K_LEFT] and is_valid_move(player2_pos, 'LEFT'):
            move_player(player2_pos, 'LEFT')
            current_player = True
        elif keys[pygame.K_RIGHT] and is_valid_move(player2_pos, 'RIGHT'):
            move_player(player2_pos, 'RIGHT')
            current_player = True

# Main game loop
# def main():
#     clock = pygame.time.Clock()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
        
#         handle_turn()
#         draw_board()
        
#         pygame.display.update()
#         clock.tick(60)

# if __name__ == '__main__':
#     main()

# Main game loop
def main():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        handle_turn()  # Handle player movements
        draw_board()   # Draw the board and players
        
        pygame.display.update()  # Update the display
        clock.tick(60)  # Maintain 60 frames per second

if __name__ == '__main__':
    main()

 