import pygame
from config import WIDTH, HEIGHT, WHITE, FPS

# Iniciar pygame
pygame.init
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road")
clock = pygame.time.Clock()

# Loop principal do pygame:

running = True
while running:
    clock.tick(FPS)

    # eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizacoes

    # Desenhos
    window.fill(WHITE)

    pygame.display.update()
pygame.quit()