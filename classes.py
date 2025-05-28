import pygame
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH, TRAIN_HEIGHT, GREEN2,TRAIN_HITBOX_WIDTH, TRAIN_HITBOX_HEIGHT, CAR_HITBOX_WIDTH, CAR_HITBOX_HEIGHT

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
pygame.mixer.init()
import random
import os
from assets import assets



class Player(pygame.sprite.Sprite):

    """
    Classe que representa o jogador (cachorro).
    Controla movimentação, limites da tela e atualização da posição.
    """
    
    def __init__(self, image):
        super().__init__()
        self.image = assets['player_image']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
        self.pontos = 0

    def move_by(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # Mantém dentro da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT



        
    def update(self):
        self.rect.y += 1

class Carro(pygame.sprite.Sprite):

    """
    Classe que representa um carro no jogo.

    Um carro se move horizontalmente (da esquerda para a direita ou vice-versa) 
    e possui uma hitbox reduzida para colisões mais precisas com o jogador.

    Atributos:
        image (Surface): imagem escalada do carro.
        rect (Rect): retângulo de posição do sprite.
        hitbox (Rect): hitbox menor que o retângulo do sprite para colisões.
        vel_x (int): velocidade horizontal.
        vel_y (int): velocidade vertical (pode ser usada para rolagem).
        pos (float): posição vertical usada para atualização suave.
    """

    def __init__(self, y, vel_x, vel_y, image):

        """
        Inicializa um carro com imagem, posição e velocidade.

        Args:
            y (int): posição vertical inicial.
            vel_x (int): velocidade horizontal (positiva ou negativa).
            vel_y (int): velocidade vertical (geralmente 1, para scroll).
            image (Surface): imagem do carro a ser renderizada.
        """

        super().__init__()
        self.image = pygame.transform.scale(image, (CAR_WIDTH, CAR_HEIGHT))
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(0, 0, CAR_HITBOX_WIDTH, CAR_HITBOX_HEIGHT)
        self.rect.y = y
        self.vel_y = vel_y
        self.vel_x = vel_x
        self.pos = y * 1.0
        self.rect.x = -self.rect.width if self.vel_x > 0 else WIDTH

    def update(self):

        """
        Atualiza a posição do carro na tela.

        Move o carro horizontalmente com base na velocidade
        e atualiza a posição vertical simulando o scroll do mapa.
        Também reposiciona a hitbox para acompanhar o carro.
        """

        self.rect.x += self.vel_x
        self.pos += 1.5
        self.rect.y = self.pos
        self.hitbox.center = self.rect.center

class Train(pygame.sprite.Sprite):
    def __init__(self, y, vel_x, vel_y, image):

        """
    Classe que representa um trem no jogo.

    O trem se move horizontalmente com velocidade definida
    e possui uma hitbox específica para detectar colisões.
    """
        super().__init__()
        self.image = pygame.transform.scale(image, (TRAIN_WIDTH, TRAIN_HEIGHT))
        self.rect = self.image.get_rect()
        self.hitbox = pygame.Rect(0, 0, TRAIN_HITBOX_WIDTH, TRAIN_HITBOX_HEIGHT)
        self.rect.y = y
        self.vel_y = vel_y
        self.vel_x = vel_x
        self.pos = y * 1.0
        
        if self.vel_x > 0:
            self.rect.x = -self.rect.width  
        else:
            self.rect.x = WIDTH
    
    def update(self):
        """Atualiza a posição do trem e da hitbox."""
        self.rect.x += self.vel_x
        self.pos += 1.5
        self.rect.y = self.pos
        self.hitbox.center = self.rect.center

class Background(pygame.sprite.Sprite):
    """
    Classe que representa uma faixa do terreno (background) no jogo.

    Pode ser grama, rua ou trilho. Serve de base para definir o tipo de
    obstáculo ou segurança da linha, e se move verticalmente com o mapa.
    """

    def __init__(self, tipo, y, id):
        """
        Inicializa a faixa de background com o tipo, posição e identificador.

        Args:
            tipo (str): tipo do terreno ('grass', 'street', 'street2' ou 'railway').
            y (int): posição vertical inicial no mapa.
            id (int or str): identificador único da linha (pode ser o índice no mapa).
        """

        super().__init__()
        self.image = assets[tipo]
        self.rect = self.image.get_rect()
        self.tipo = tipo
        self.rect.y = y
        self.rect.x = 0
        self.id = id
        self.scroll_speed = 1
    
    def update(self):
        """
        Atualiza a posição vertical do terreno, simulando movimento do mundo.
        """

        self.rect.y += self.scroll_speed