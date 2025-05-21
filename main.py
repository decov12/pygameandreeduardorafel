import pygame
import random
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH, TRAIN_HEIGHT, GREEN2 
# Iniciar pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road 2.0")
clock = pygame.time.Clock()


import pygame
import random
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, WOOD_WIDTH, WOOD_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT

assets = {}
assets['player_image'] = pygame.image.load('Assets/Armature_jumping_left_1.png').convert_alpha()
assets['player_image'] = pygame.transform.scale(assets['player_image'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['tree_log']=pygame.image.load('Assets/objects/the wood.png').convert_alpha()
assets['tree_log']=pygame.transform.scale(assets['tree_log'], (WOOD_WIDTH,WOOD_HEIGHT))
assets['background'] = pygame.image.load('Assets/Game Level.png').convert_alpha()
assets['player_image'] = pygame.image.load('Assets/Armature_jumping_right_1.png').convert_alpha()
assets['player_image'] = pygame.transform.scale(assets['player_image'], (PLAYER_WIDTH, PLAYER_HEIGHT))
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
assets['street'] = pygame.transform.scale(assets['street'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['street2'] = pygame.image.load('Assets/Roads/Street2.2.png').convert_alpha()
assets['street2'] = pygame.transform.scale(assets['street2'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['water'] = pygame.image.load('Assets/Roads/Water2.png').convert_alpha()
assets['water'] = pygame.transform.scale(assets['water'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['train'] = pygame.image.load('Assets/train front.png').convert_alpha()
assets['train'] = pygame.transform.scale(assets['train'], (TRAIN_WIDTH, TRAIN_HEIGHT))

available_backgrounds = ['railway','street2', 'water', 'street2']

available_cars = ['car_black', 'car_blue', 'car_brown', 'car_red']

# classe do jogador:

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = assets['player_image']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

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
        
    def update(self):
        self.rect.y += 1


# classe carro:
class Carro(pygame.sprite.Sprite):
    def __init__(self, y, vel_x, vel_y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.vel_y = vel_y
        self.vel_x = vel_x
        self.pos = y * 1.0
        
        if self.vel_x > 0:
            self.rect.x = -self.rect.width  

        else:
            self.rect.x = WIDTH
    
    def update(self):
        self.rect.x += self.vel_x
        self.pos += 1.5
        self.rect.y = self.pos

class Train(pygame.sprite.Sprite):
    def __init__(self, y, vel_x, vel_y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.vel_y = vel_y
        self.vel_x = vel_x
        self.pos = y * 1.0
        
        if self.vel_x > 0:
            self.rect.x = -self.rect.width  

        else:
            self.rect.x = WIDTH
    
    def update(self):
        self.rect.x += self.vel_x
        self.pos += 1.5
        self.rect.y = self.pos

class Tree_log(pygame.sprite.Sprite):
    def __init__(self, y, vel_x, vel_y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.vel_y = vel_y
        self.vel_x = vel_x
        self.pos = y * 1.0
        
        if self.vel_x > 0:
            self.rect.x = -self.rect.width  

        else:
            self.rect.x = WIDTH
    
    def update(self):
        self.rect.x += self.vel_x
        self.pos += 1.5
        self.rect.y = self.pos

class Background(pygame.sprite.Sprite):
    def __init__ (self, tipo, y, id):
        super().__init__()
        self.image = assets[tipo]
        self.rect = self.image.get_rect()
        self.tipo = tipo
        self.rect.y = y
        self.rect.x = 0
        self.id = id
        self.scroll_speed = 1
    
    def update(self):
        self.rect.y += self.scroll_speed


backgrounds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_cars = pygame.sprite.Group()
all_trains = pygame.sprite.Group()
# all_treelog = pygame.sprite.Group()

for i in range(-10, 10):
    bg = Background(random.choice(available_backgrounds), i * 150 , i)

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

# Criação de objetos 

player = Player(assets['player_image'])
all_sprites.add(player)

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

    novo_bg = False
    for bg in backgrounds:
        if bg.rect.bottom > HEIGHT + 150:
            print("bg ",bg.rect.bottom, bg.tipo, bg.id)
            bg.kill()
            novo_bg = True  
    if novo_bg:
        novo_bg = False
        bg_image = random.choice(available_backgrounds)
        max_y = 0
        for back in backgrounds:
            if max_y > back.rect.y:
                max_y = back.rect.y
        y = max_y - 150
        bg = Background(random.choice(available_backgrounds), y , "novo")
        
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
    


    # Atualizações
    all_cars.update()
    all_trains.update()
    backgrounds.update()
    player.update()

    hits = pygame.sprite.spritecollide(player, all_cars, True)
    hits2= pygame.sprite.spritecollide(player, all_trains, True)

    if hits or hits2:
        running = False

    # Desenhos
    window.fill(GREEN2)
    backgrounds.draw(window)
    all_sprites.draw(window)
    pygame.display.update()

    
pygame.quit()