import pygame
import random
from config import WIDTH, HEIGHT, WHITE, FPS

# Iniciar pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road")
clock = pygame.time.Clock()

# classe do jogador:

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0))
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
    def __init__(self, y, velocidade):
        super().__init__()
        self.image = pygame.Surface((60, 40)) 
        self.image.fill((255, 0, 0)) 
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
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Criacao carros:

carros = pygame.sprite.Group()

# Criar 5 carros em faixas diferentes
for i in range(5):
    y = 100 + i * 80  
    velocidade = random.choice([3, 4, 5])  
    carro = Carro(y, velocidade)
    all_sprites.add(carro)
    carros.add(carro)

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
    carros.update()

    # Desenhos
    window.fill(WHITE)
    all_sprites.draw(window)
    pygame.display.update()

pygame.quit()