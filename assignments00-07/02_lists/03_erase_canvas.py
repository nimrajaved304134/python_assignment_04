import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
ERASER_SIZE = 40
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Eraser")

# Create the canvas grid
grid_width = WIDTH // CELL_SIZE
grid_height = HEIGHT // CELL_SIZE

# Initialize all cells to blue (1 represents blue, 0 represents white)
canvas = [[1 for _ in range(grid_width)] for _ in range(grid_height)]

# Eraser properties
eraser_rect = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)
dragging = False

def draw_canvas():
    """Draw the canvas grid"""
    for y in range(grid_height):
        for x in range(grid_width):
            color = BLUE if canvas[y][x] else WHITE
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def apply_eraser():
    """Turn all cells under the eraser white"""
    # Convert eraser rect to grid coordinates
    left = eraser_rect.left // CELL_SIZE
    right = (eraser_rect.right - 1) // CELL_SIZE
    top = eraser_rect.top // CELL_SIZE
    bottom = (eraser_rect.bottom - 1) // CELL_SIZE
    
    # Clamp to grid boundaries
    left = max(0, left)
    right = min(grid_width - 1, right)
    top = max(0, top)
    bottom = min(grid_height - 1, bottom)
    
    # Erase cells
    for y in range(top, bottom + 1):
        for x in range(left, right + 1):
            canvas[y][x] = 0

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                eraser_rect.center = event.pos
                dragging = True
                apply_eraser()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                eraser_rect.center = event.pos
                apply_eraser()
    
    # Draw everything
    screen.fill(WHITE)
    draw_canvas()
    
    # Draw the eraser (semi-transparent red)
    eraser_surface = pygame.Surface((ERASER_SIZE, ERASER_SIZE), pygame.SRCALPHA)
    pygame.draw.rect(eraser_surface, (*RED, 128), (0, 0, ERASER_SIZE, ERASER_SIZE))
    screen.blit(eraser_surface, eraser_rect)
    
    pygame.display.flip()
    clock.tick(60)