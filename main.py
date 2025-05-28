import pygame
import random
from os import path
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH, TRAIN_HEIGHT, GREEN2, TRAIN_HITBOX_WIDTH, TRAIN_HITBOX_HEIGHT, CAR_HITBOX_WIDTH, CAR_HITBOX_HEIGHT
from final_screen import *
from init_screen import *
from assets import assets
from classes import *
from funcoes import *

# Inicializações
pygame.init()
pygame.mixer.init()

# Criar janela
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road 2.0")
clock = pygame.time.Clock()

# Música de fundo
pygame.mixer.music.load('Assets/Bit Quest.mp3')  
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)

# Pós-processamento dos assets (convert_alpha e scale)
assets['player_image'] = pygame.transform.scale(assets['player_image'], (PLAYER_WIDTH, PLAYER_HEIGHT)).convert_alpha()
assets['player_image_right'] = pygame.transform.scale(assets['player_image_right'], (PLAYER_WIDTH, PLAYER_HEIGHT)).convert_alpha()
assets['player_dead'] = pygame.transform.scale(assets['player_dead'], (PLAYER_WIDTH + 50, PLAYER_HEIGHT + 20)).convert_alpha()
assets['background'] = assets['background'].convert_alpha()
assets['tela_inicio'] = pygame.transform.scale(assets['tela_inicio'], (WIDTH, HEIGHT)).convert_alpha()
assets['tela_fim'] = pygame.transform.scale(assets['tela_fim'], (WIDTH, HEIGHT)).convert_alpha()

for cor in ['car_black', 'car_blue', 'car_brown', 'car_red']:
    assets[cor] = pygame.transform.scale(assets[cor], (CAR_WIDTH, CAR_HEIGHT)).convert_alpha()

for nome in ['railway', 'street', 'street2', 'grass']:
    assets[nome] = pygame.transform.scale(assets[nome], (ROAD_WIDTH, ROAD_HEIGHT)).convert_alpha()

assets['train'] = pygame.transform.scale(assets['train'], (TRAIN_WIDTH, TRAIN_HEIGHT)).convert_alpha()

# Loop principal do jogo
playing = True
while playing:
    if show_start_screen(window, clock):
        game_over = game()
        if not game_over:
            playing = False  
        else:
            continuar = show_game_over_screen()
            if not continuar:
                playing = False  
            while continuar:
                if show_start_screen(window, clock):
                    game_over = game()
                    if not game_over:
                        playing = False  
                        continuar = False
                    else:
                        continuar = show_game_over_screen(window, clock)
                        if not continuar:
                            playing = False  
                else:
                    continuar = False
                    playing = False  
    else:
        playing = False  

pygame.quit()
