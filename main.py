import pygame
import random
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT

# Iniciar pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road 2.0")
clock = pygame.time.Clock()

assets = {}
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

assets['background'] = pygame.image.load('assets/Game Level.png').convert_alpha()
assets['background'] = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))

assets['grass'] = pygame.image.load('assets/Grass2').convert_alpha()
assets['grass'] = pygame.transform.scale(assets['grass'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['railway'] = pygame.image.load('assets/railway2').convert_alpha()
assets['railway'] = pygame.transform.scale(assets['railway'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['sidewalk'] = pygame.image.load('assets/sidewalk2').convert_alpha()
assets['sidewalk'] = pygame.transform.scale(assets['sidewalk'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['street'] = pygame.image.load('assets/Street1.2').convert_alpha()
assets['street'] = pygame.transform.scale(assets['street'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['street2'] = pygame.image.load('assets/Street2.2').convert_alpha()
assets['street2'] = pygame.transform.scale(assets['street2'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['water'] = pygame.image.load('assets/Water2').convert_alpha()
assets['water'] = pygame.transform.scale(assets['water'], (ROAD_WIDTH, ROAD_HEIGHT))


available_cars = ['car_black', 'car_blue', 'car_brown', 'car_red']

lista_backgrounds = ['grass', 'railway', 'sidewalk', 'street', 'street2', 'water']

# for background in lista_backgrounds:


# classe do jogador:

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = assets['player_image']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10

    def move_by(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # manter dentro da tela
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
    def __init__(self, y, vel_x, vel_y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.vel_y = vel_y
        self.vel_x = vel_x
        
        if self.vel_x > 0:
            self.rect.x = -self.rect.width  

        else:
            self.rect.x = WIDTH
    
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


        # Se o carro saiu da tela, reposiciona
        if self.vel_x > 0 and self.rect.left > WIDTH:
            self.rect.right = 0
        elif self.vel_x < 0 and self.rect.right < 0:
            self.rect.left = WIDTH

scroll_speed = 2

class Background(pygame.sprite.Sprite):
    def __init__ (self, tipo, y):
        self.image = assets[tipo]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = 0
        scroll_speed = 2
    
    def update(self):
        self.rect.y += scroll_speed
        


    

# Criação de objetos 
all_sprites = pygame.sprite.Group()

player = Player(assets['player_image'])
all_sprites.add(player)

# Criacao carros:
all_cars = pygame.sprite.Group()

# Criar 5 carros em faixas diferentes
faixas_y = [420, 430]

# Loop principal do pygame:

last_car_emitido = 0
intervalo_cars_emitidos = 2000

running = True
while running:
    clock.tick(FPS)

    # eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_by(+15, -40)
            elif event.key == pygame.K_LEFT:
                player.move_by(-30, -5)
            elif event.key == pygame.K_RIGHT:
                player.move_by(+30, +5)
            elif event.key == pygame.K_DOWN:
                player.move_by(-15, +40)
        
        now = pygame.time.get_ticks()

        if now - last_car_emitido > intervalo_cars_emitidos:
            y = random.choice(faixas_y)
            vel_x = 5
            vel_y = 0.5
            car_image = random.choice(available_cars)
            carro = Carro(y, vel_x, vel_y, assets[car_image])
            all_sprites.add(carro)
            all_cars.add(carro)
            last_car_emitido = now


    # Atualizações
    all_cars.update()

    hits = pygame.sprite.spritecollide(player, all_cars, True)
    if hits:
        running = False

    # Desenhos
    window.fill(WHITE)
    window.blit(assets['background'], (0, 0))
    all_sprites.draw(window)
    pygame.display.update()

pygame.quit()
