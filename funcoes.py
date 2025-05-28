import pygame
import random
import os
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH, TRAIN_HEIGHT, GREEN2,TRAIN_HITBOX_WIDTH, TRAIN_HITBOX_HEIGHT, CAR_HITBOX_WIDTH, CAR_HITBOX_HEIGHT

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.init()

pygame.mixer.music.load('Assets/Bit Quest.mp3')  
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)
pygame.display.set_caption("Crossy Road 2.0")
clock = pygame.time.Clock()

from assets import *
from classes import *
import assets

available_backgrounds = ['railway', 'street2','grass']
available_cars = ['car_black', 'car_blue', 'car_brown', 'car_red']

# Funções do jogo

def eh_rua(bg):
    """
    Verifica se o tipo de background corresponde a uma rua.

    Args:
        bg (str): tipo do terreno.

    Returns:
        bool: True se for uma rua, False caso contrário.
    """

    return bg in ['street', 'street2']

def eh_perigoso(bg):
    """
    Verifica se o tipo de background representa perigo ao jogador.

    Args:
        bg (str): tipo do terreno.

    Returns:
        bool: True se for rua ou trilho, False se for seguro.
    """

    return bg in ['street', 'street2', 'railway']

def game():
    """
    Executa a lógica principal do jogo em uma única rodada.

    Controla o jogador, gera terrenos, obstáculos (carros e trens),
    verifica colisões e trata o encerramento da partida por inatividade
    ou por batida. Também atualiza e desenha os elementos na tela.
    
    Returns:
        bool: True se o jogo terminou com Game Over, False se o jogador sair diretamente.
    """

    score = 0
    backgrounds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_cars = pygame.sprite.Group()
    all_trains = pygame.sprite.Group()

    last_move_time = pygame.time.get_ticks()
    INACTIVITY_TIMEOUT = 6000 

    ultimos_bg = []
    for i in range(-10, 10):
        if -1 <= i <= 1:
            tipo = 'grass'  # força os 3 terrenos centrais a serem seguros
        else:
            tipo = random.choice(available_backgrounds)
        bg = Background(tipo, i * 75, i)

        if bg.tipo in ['street', 'street2']:
            car_image = random.choice(available_cars)
            carro = Carro(bg.rect.y, 5, 1, assets[car_image])
            all_sprites.add(carro)
            all_cars.add(carro)
        
        if bg.tipo in ['railway']:
            train_image = assets['train']
            train = Train(bg.rect.y, 5, 1, train_image)
            all_sprites.add(train)
            all_trains.add(train)

        backgrounds.add(bg)
        if len(ultimos_bg) < 3:
            ultimos_bg.append(tipo)
        else:
            ultimos_bg.append(tipo)
            ultimos_bg.pop(0)

    player = Player(assets['player_image'])
    player.rect.centery = 1 * 75 + 37.5
    all_sprites.add(player)

    running = True
    while running:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()
        if current_time - last_move_time > INACTIVITY_TIMEOUT:
            player.image = assets['player_dead']
    
    # desenha a tela parada com o cachorro caído
            window.fill(GREEN2)
            backgrounds.draw(window)
            all_sprites.draw(window)
            pygame.display.update()
    
            pygame.time.delay(1000)
            return True 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    last_move_time = pygame.time.get_ticks()  # Reset timer
                    player.move_by(+10, -37.5)
                elif event.key == pygame.K_LEFT:
                    last_move_time = pygame.time.get_ticks()  # Reset timer
                    player.move_by(-30, -5)
                elif event.key == pygame.K_RIGHT:
                    last_move_time = pygame.time.get_ticks()  # Reset timer
                    player.move_by(+30, +5)
                elif event.key == pygame.K_DOWN:
                    last_move_time = pygame.time.get_ticks()  # Reset timer
                    player.move_by(-10, +37.5)
                
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit() 
        
        novo_carro = False
        kill_cars = False
        for car in all_cars:
            if car.rect.left > WIDTH:
                kill_cars = True
                novo_carro = True
        if kill_cars:
            for car in all_cars:
                car.kill()
            kill_cars = False
        if novo_carro:
            novo_carro = False
            for bg in backgrounds:
                if bg.tipo in ['street', 'street2']:
                    car_image = random.choice(available_cars)
                    carro = Carro(bg.rect.y, 5, 1, assets[car_image])
                    all_sprites.add(carro)
                    all_cars.add(carro)
        
        novo_train = False
        kill_trains = False
        for train in all_trains:
            if train.rect.left > WIDTH:
                kill_trains = True
                novo_train = True
        if kill_trains:
            for train in all_trains:
                train.kill()
            kill_trains = False
        if novo_train:
            novo_train = False    
            for bg in backgrounds:
                if bg.tipo in ['railway']:
                    train_image = assets['train']
                    train = Train(bg.rect.y, 5, 1, train_image)
                    all_sprites.add(train)
                    all_trains.add(train)
            novo_train = False

        novo_bg = False
        for bg in backgrounds:
            if bg.rect.bottom > HEIGHT + 150:
                bg.kill()
                novo_bg = True  
        if novo_bg:
            novo_bg = False
        # Determina tipo do próximo background com base nos últimos 3
        ultimos_tipos = ultimos_bg[-3:]

        ruas_seguidas = all(eh_rua(bg) for bg in ultimos_tipos)
        perigo_extremo = all(eh_perigoso(bg) for bg in ultimos_tipos)
        trilhos_seguidos = all(bg == 'railway' for bg in ultimos_tipos)
        gramas_seguidas = all(bg == 'grass' for bg in ultimos_tipos)

        if len(ultimos_tipos) >= 3 and ruas_seguidas:
            bg_image = 'grass' #define que o proximo é grama
        elif len(ultimos_tipos) >= 3 and perigo_extremo:
            bg_image = 'grass' #define que o proximo é grama
        elif len(ultimos_tipos) >= 3 and trilhos_seguidos:
            bg_image = 'grass' #define que o proximo é grama
        elif len(ultimos_tipos) >= 3 and gramas_seguidas:
            bg_image = random.choice(['street', 'street2', 'railway']) #define que o proximo é rua ou trem
        else:
            bg_image = random.choice(available_backgrounds)


        max_y = min(back.rect.y for back in backgrounds)
        y = max_y - 75
        bg = Background(bg_image, y, "novo")
        backgrounds.add(bg)

        if bg.tipo in ['street', 'street2']:
            car_image = random.choice(available_cars)
            carro = Carro(bg.rect.y, 5, 1, assets[car_image])
            all_sprites.add(carro)
            all_cars.add(carro)

        elif bg.tipo == 'railway':
            train = Train(bg.rect.y, 5, 1, assets['train'])
            all_sprites.add(train)
            all_trains.add(train)
        
        ultimos_bg.append(bg_image)
        if len(ultimos_bg) > 3:
            ultimos_bg.pop(0)

        backgrounds.add(bg)
        
        all_cars.update()
        all_trains.update()
        backgrounds.update()
        player.update()

        # colisao com o carro
        hits = []
        for car in all_cars:
            if player.rect.colliderect(car.hitbox):
                hits.append(car)
                car.kill()

        # colisao com o trem
        hits2 = []
        for train in all_trains:
            if player.rect.colliderect(train.hitbox):
                hits2.append(train)
                train.kill()

        # animacao para quando morre
        if hits or hits2:
            assets['car crash'].play()
            player.image = assets['player_dead']
            window.fill(GREEN2)
            backgrounds.draw(window)
            all_sprites.draw(window)
            pygame.display.update()
            pygame.time.delay(1000)  # espera 1 segundo
            return True

        window.fill(GREEN2)
        backgrounds.draw(window)
        all_sprites.draw(window)
        pygame.display.update()
    
    return True