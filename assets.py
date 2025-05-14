import pygame
import random
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, WOOD_WIDTH, WOOD_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT

assets = {}
assets['player_image'] = pygame.image.load('assets/Armature_jumping_left_1.png').convert_alpha()
assets['player_image'] = pygame.transform.scale(assets['player_image'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['tree_log']=pygame.image.load('assets/the wood.png').convert_alpha()
assets['tree_log']=pygame.transform.scale(assets['tree_log'], (WOOD_WIDTH,WOOD_HEIGHT))
assets['background'] = pygame.image.load('assets/Game Level.png').convert_alpha()
assets['player_image'] = pygame.image.load('assets/Armature_jumping_right_1.png').convert_alpha()
assets['player_image'] = pygame.transform.scale(assets['player_image'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['car_black'] = pygame.image.load('assets/black car front.png').convert_alpha()
assets['car_black'] = pygame.transform.scale(assets['car_black'], (CAR_WIDTH, CAR_HEIGHT))
assets['car_blue'] = pygame.image.load('assets/blue car front.png').convert_alpha()
assets['car_blue'] = pygame.transform.scale(assets['car_blue'], (CAR_WIDTH, CAR_HEIGHT))
assets['car_brown'] = pygame.image.load('assets/brown car front.png').convert_alpha()
assets['car_brown'] = pygame.transform.scale(assets['car_brown'], (CAR_WIDTH, CAR_HEIGHT))
assets['car_red'] = pygame.image.load('assets/red car front.png').convert_alpha()
assets['car_red'] = pygame.transform.scale(assets['car_red'], (CAR_WIDTH, CAR_HEIGHT))
assets['grass'] = pygame.image.load('assets/Roads/Grass2.png').convert_alpha()
assets['grass'] = pygame.transform.scale(assets['grass'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['railway'] = pygame.image.load('assets/Roads/railway2.png').convert_alpha()
assets['railway'] = pygame.transform.scale(assets['railway'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['sidewalk'] = pygame.image.load('assets/Roads/sidewalk2.png').convert_alpha()
assets['sidewalk'] = pygame.transform.scale(assets['sidewalk'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['street'] = pygame.image.load('assets/Roads/Street1.2.png').convert_alpha()
assets['street'] = pygame.transform.scale(assets['street'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['street2'] = pygame.image.load('assets/Roads/Street2.2.png').convert_alpha()
assets['street2'] = pygame.transform.scale(assets['street2'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['water'] = pygame.image.load('assets/Roads/Water2.png').convert_alpha()
assets['water'] = pygame.transform.scale(assets['water'], (ROAD_WIDTH, ROAD_HEIGHT))

available_backgrounds = ['grass','railway', 'sidewalk', 'street', 'street2', 'water']

available_cars = ['car_black', 'car_blue', 'car_brown', 'car_red']

lista_backgrounds = ['grass', 'railway', 'sidewalk', 'street', 'street2', 'water']