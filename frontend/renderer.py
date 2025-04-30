import pygame
from common.config import TILE_SIZE

COLORS = {"John": (0, 0, 255), "Anna": (0, 255, 0), "Arun": (255, 0, 0)}

def draw_agent(screen, name, pos, status):
    x, y = pos
    pygame.draw.rect(screen, COLORS[name], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    font = pygame.font.Font(None, 24)
    screen.blit(font.render(name, True, (255, 255, 255)), (x * TILE_SIZE, y * TILE_SIZE))
    screen.blit(font.render(status, True, (200, 200, 200)), (x * TILE_SIZE, y * TILE_SIZE + 20))