import pygame
import random
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH,TRAIN_HEIGHT

def load_assets():
    assets = {}

    assets['player_image'] = pygame.image.load('Assets/Armature_jumping_left_1.png').convert_alpha()
    assets['player_image'] = pygame.transform.scale(assets['player_image'], (PLAYER_WIDTH, PLAYER_HEIGHT))

    assets['background'] = pygame.image.load('Assets/Game Level.png').convert_alpha()

    assets['player_image_right'] = pygame.image.load('Assets/Armature_jumping_right_1.png').convert_alpha()
    assets['player_image_right'] = pygame.transform.scale(assets['player_image_right'], (PLAYER_WIDTH, PLAYER_HEIGHT))

    assets['car_black'] = pygame.image.load('Assets/black car front.png').convert_alpha()
    assets['car_black'] = pygame.transform.scale(assets['car_black'], (CAR_WIDTH, CAR_HEIGHT))

    assets['car_blue'] = pygame.image.load('Assets/blue car front.png').convert_alpha()
    assets['car_blue'] = pygame.transform.scale(assets['car_blue'], (CAR_WIDTH, CAR_HEIGHT))

    assets['car_brown'] = pygame.image.load('Assets/brown car front.png').convert_alpha()
    assets['car_brown'] = pygame.transform.scale(assets['car_brown'], (CAR_WIDTH, CAR_HEIGHT))

    assets['car_red'] = pygame.image.load('Assets/red car front.png').convert_alpha()
    assets['car_red'] = pygame.transform.scale(assets['car_red'], (CAR_WIDTH, CAR_HEIGHT))

    assets['railway'] = pygame.image.load('Assets/Roads/railway2.png').convert_alpha()
    assets['railway'] = pygame.transform.scale(assets['railway'], (ROAD_WIDTH, ROAD_HEIGHT))

    assets['street'] = pygame.image.load('Assets/Roads/Street1.2.png').convert_alpha()
    assets['street'] = pygame.transform.scale(assets['street'], (ROAD_WIDTH, ROAD_HEIGHT))

    assets['street2'] = pygame.image.load('Assets/Roads/Street2.2.png').convert_alpha()
    assets['street2'] = pygame.transform.scale(assets['street2'], (ROAD_WIDTH, ROAD_HEIGHT))

    assets['train'] = pygame.image.load('Assets/train front.png').convert_alpha()
    assets['train'] = pygame.transform.scale(assets['train'], (TRAIN_WIDTH, TRAIN_HEIGHT))

    assets['tela_inicio'] = pygame.image.load('Assets/tela_inicial.png').convert_alpha()
    assets['tela_inicio'] = pygame.transform.scale(assets['tela_inicio'], (WIDTH, HEIGHT))

    assets['tela_fim'] = pygame.image.load('Assets/tela_game_over2.png').convert_alpha()
    assets['tela_fim'] = pygame.transform.scale(assets['tela_fim'], (WIDTH, HEIGHT))

    assets['grass'] = pygame.image.load('Assets/Roads/Grass.png').convert_alpha()
    assets['grass'] = pygame.transform.scale(assets['grass'], (ROAD_WIDTH, ROAD_HEIGHT))

    assets['car crash'] = pygame.mixer.Sound("Assets/car-crash_A_minor.wav")

    assets['player_dead'] = pygame.image.load('Assets/player_dead.png').convert_alpha()
    assets['player_dead'] = pygame.transform.scale(assets['player_dead'], (PLAYER_WIDTH + 50, PLAYER_HEIGHT + 20))

    return assets
