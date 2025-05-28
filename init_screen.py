import pygame
from assets import assets
from config import WIDTH, HEIGHT, FPS

def show_start_screen(window, clock):
    """
    Exibe a tela inicial do jogo e espera interação do jogador.
    Retorna:
        bool: True se o jogo deve começar, False se o jogador sair.
    """
    window.blit(assets['tela_inicio'], (0, 0)) 
    pygame.display.flip()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False
