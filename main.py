import pygame
from config import WIDTH, HEIGHT, WHITE, FPS

# Iniciar pygame
pygame.init
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road")
clock = pygame.time.Clock()
