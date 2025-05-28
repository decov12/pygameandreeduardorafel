import pygame
from assets import assets
from classes import *
from funcoes import *

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.init()

pygame.mixer.music.load('Assets/Bit Quest.mp3')  
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)
pygame.display.set_caption("Crossy Road 2.0")
clock = pygame.time.Clock()

# Função para mostrar a tela de game over (modificada conforme pedido)
def show_game_over_screen():

    """
    Exibe a tela de Game Over por tempo indefinido até que o jogador decida.

    Retorna:
        bool: 
            - True se o jogador pressionar 'R' para retornar ao menu inicial.
            - False se o jogador pressionar 'ESC' ou fechar a janela.
    """

    window.blit(assets['tela_fim'], (0, 0))
    font = pygame.font.SysFont(None, 48)

    text3 = font.render("R - Menu Inicial | ESC - Sair", True, (200, 200, 200))
    window.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT - 110))

    pygame.display.flip()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # voltar ao menu
                elif event.key == pygame.K_ESCAPE:
                    return False  # sair