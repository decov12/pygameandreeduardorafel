import pygame
import random
from os import path
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH, TRAIN_HEIGHT, GREEN2,TRAIN_HITBOX_WIDTH, TRAIN_HITBOX_HEIGHT, CAR_HITBOX_WIDTH, CAR_HITBOX_HEIGHT
from final_screen import *
from init_screen import *

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
pygame.mixer.init()

from assets import *
from classes import *
from funcoes import *
import assets


# Loop principal do jogo (definindo quando é tela de ínicio, a de jogo e o fim)
playing = True
while playing:
    if show_start_screen():
        game_over = game()
        if not game_over:
            playing = False  
        else:
            continuar = show_game_over_screen()
            if not continuar:
                playing = False  
            while continuar:
                if show_start_screen():
                    game_over = game()
                    if not game_over:
                        playing = False  
                        continuar = False
                    else:
                        continuar = show_game_over_screen()
                        if not continuar:
                            playing = False  
                else:
                    continuar = False
                    playing = False  
    else:
        playing = False  

pygame.quit()


# import pygame
# from assets import *
# from classes import *
# from funcoes import *
# from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH, TRAIN_HEIGHT, GREEN2,TRAIN_HITBOX_WIDTH, TRAIN_HITBOX_HEIGHT, CAR_HITBOX_WIDTH, CAR_HITBOX_HEIGHT

# pygame.init()
# window = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.mixer.init()

# pygame.mixer.music.load('Assets/Bit Quest.mp3')  
# pygame.mixer.music.set_volume(0.5)  
# pygame.mixer.music.play(-1)
# pygame.display.set_caption("Crossy Road 2.0")
# clock = pygame.time.Clock()