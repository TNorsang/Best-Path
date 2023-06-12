import pygame
import math

pygame.init()

width = 800
height = 800
cell_size = 35

screen = pygame.display.set_mode((width, height))

num_rows = height // cell_size
num_cols = width // cell_size

pygame.display.set_caption("Best Path")

white = (255,255,255)
blue = (0, 255, 255)
hover = (19, 177, 235)

game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    
    screen.fill(white)
        
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, blue, (x, 0), (x, height))
    
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, blue, (0, y), (width, y))
    
    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEMOTION:
        mouse_pos = pygame.mouse.get_pos()
        mouse_col = mouse_pos[0] // cell_size
        mouse_row = mouse_pos[1] // cell_size
        
        cell_rect = pygame.Rect(mouse_col * cell_size, mouse_row * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, hover, cell_rect)
        
        # print("Mouse Coordinate:", mouse_pos)    
    
    
    pygame.display.flip()
    
pygame.quit()
    