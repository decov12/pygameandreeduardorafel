import pygame
import random
from config import WIDTH, HEIGHT, WHITE, FPS

# Iniciar pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road 2.0")
clock = pygame.time.Clock()

# Imagem do carro
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 70
CAR_WIDTH = 80
CAR_HEIGHT = 90

assets = {}
assets['player_image'] = pygame.image.load('assets/Armature_jumping_left_1.png').convert_alpha()
assets['player_image'] = pygame.transform.scale(assets['player_image'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['car_image'] = pygame.image.load('assets/black car front.png').convert_alpha()
assets['car_image'] = pygame.transform.scale(assets['car_image'], (CAR_WIDTH, CAR_HEIGHT))
assets['background'] = pygame.image.load('assets/Game Level.png').convert_alpha()

# classe do jogador:

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = assets['player_image']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10

    def update (self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # manter na tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# classe carro:
class Carro(pygame.sprite.Sprite):
    def __init__(self, y, velocidade, image):
        super().__init__()
        self.image = assets['car_image']
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.velocidade = velocidade
        
        if self.velocidade > 0:
            self.rect.x = -self.rect.width  
        else:
            self.rect.x = WIDTH
    
    def update(self):
        self.rect.x += self.velocidade

        # Se o carro saiu da tela, reposiciona
        if self.velocidade > 0 and self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.velocidade < 0 and self.rect.right < 0:
            self.rect.left = WIDTH

# Criação de objetos 
all_sprites = pygame.sprite.Group()

player = Player(assets['player_image'])
all_sprites.add(player)

# Criacao carros:
all_cars = pygame.sprite.Group()

# Criar 5 carros em faixas diferentes
for i in range(5):
    y = 100 + i * 80  
    velocidade = random.randint(2,8)
    carro = Carro(y, velocidade, assets['car_image'])
    all_sprites.add(carro)
    all_cars.add(carro)

# Loop principal do pygame:

running = True
while running:
    clock.tick(FPS)

    # eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizacoes

    

    keys = pygame.key.get_pressed()
    player.update(keys)
    all_cars.update()

    hits = pygame.sprite.spritecollide(player, all_cars, True)

    if hits:
        running = False

    # Desenhos
    window.fill(WHITE)
    all_sprites.draw(window)
    pygame.display.update()

pygame.quit()