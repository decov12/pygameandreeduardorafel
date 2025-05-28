import pygame
from config import WIDTH, HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH, TRAIN_HEIGHT

pygame.init()
pygame.mixer.init()

assets = {}

assets['player_image'] = pygame.image.load('Assets/Armature_jumping_left_1.png')
assets['player_image_right'] = pygame.image.load('Assets/Armature_jumping_right_1.png')
assets['player_dead'] = pygame.image.load('Assets/player_dead.png')
assets['background'] = pygame.image.load('Assets/Game Level.png')
assets['tela_inicio'] = pygame.image.load('Assets/tela_inicial.png')
assets['tela_fim'] = pygame.image.load('Assets/tela_game_over2.png')

assets['car_black'] = pygame.image.load('Assets/black car front.png')
assets['car_blue'] = pygame.image.load('Assets/blue car front.png')
assets['car_brown'] = pygame.image.load('Assets/brown car front.png')
assets['car_red'] = pygame.image.load('Assets/red car front.png')

assets['railway'] = pygame.image.load('Assets/Roads/railway2.png')
assets['street'] = pygame.image.load('Assets/Roads/Street1.2.png')
assets['street2'] = pygame.image.load('Assets/Roads/Street2.2.png')
assets['grass'] = pygame.image.load('Assets/Roads/Grass.png')

assets['train'] = pygame.image.load('Assets/train front.png')

# Sons
assets['car crash'] = pygame.mixer.Sound("Assets/car-crash_A_minor.wav")
