import pygame
import random
from assets import *
from classes import *
from funcoes import *
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH, TRAIN_HEIGHT, GREEN2,TRAIN_HITBOX_WIDTH, TRAIN_HITBOX_HEIGHT, CAR_HITBOX_WIDTH, CAR_HITBOX_HEIGHT

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.init()

pygame.mixer.music.load('Assets/Bit Quest.mp3')  
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)
pygame.display.set_caption("Crossy Road 2.0")
clock = pygame.time.Clock()


def show_start_screen():

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