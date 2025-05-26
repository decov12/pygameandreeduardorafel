import pygame
import random
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH, TRAIN_HEIGHT, GREEN2,TRAIN_HITBOX_WIDTH, TRAIN_HITBOX_HEIGHT, CAR_HITBOX_WIDTH, CAR_HITBOX_HEIGHT

# Iniciar pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Assets\Bit Quest.mp3')  
pygame.mixer.music.set_volume(0.5)  
pygame.mixer.music.play(-1)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road 2.0")
clock = pygame.time.Clock()

# Carregar assets (mantido igual)
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
assets['grass']=pygame.image.load('Assets/Roads/Grass.png').convert_alpha()
assets['grass'] = pygame.transform.scale(assets['grass'], (ROAD_WIDTH, ROAD_HEIGHT))

available_backgrounds = ['railway', 'street2','grass']
available_cars = ['car_black', 'car_blue', 'car_brown', 'car_red']

# Função para mostrar a tela inicial (modificada para ESC fechar)
def show_start_screen():
    window.blit(assets['tela_inicio'], (0, 0)) 
    pygame.display.flip()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

# Função para mostrar a tela de game over (modificada conforme pedido)
def show_game_over_screen():
    window.blit(assets['tela_fim'], (0, 0))
    font = pygame.font.SysFont(None, 48)

    text3 = font.render("R - Menu Inicial | ESC - Sair", True, (200, 200, 200))
    window.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT - 110))

    pygame.display.flip()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # voltar ao menu
                elif event.key == pygame.K_ESCAPE:
                    return False  # sair

# Restante do código mantido exatamente igual
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

class Carro(pygame.sprite.Sprite):
    def __init__(self, y, vel_x, vel_y, image):
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
        self.rect.x += self.vel_x
        self.pos += 1.5
        self.rect.y = self.pos
        self.hitbox.center = self.rect.center

class Train(pygame.sprite.Sprite):
    def __init__(self, y, vel_x, vel_y, image):
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
        self.rect.x += self.vel_x
        self.pos += 1.5
        self.rect.y = self.pos
        self.hitbox.center = self.rect.center

class Background(pygame.sprite.Sprite):
    def __init__(self, tipo, y, id):
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

def game():
    score = 0
    backgrounds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_cars = pygame.sprite.Group()
    all_trains = pygame.sprite.Group()

    last_move_time = pygame.time.get_ticks()
    INACTIVITY_TIMEOUT = 5000 

    ultimos_bg = []
    for i in range(-10, 10):
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
        
        # Restante da função game() mantido exatamente igual
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
        repetidos = set(ultimos_bg[-3:])
        if len(ultimos_bg) >= 3 and all(bg in ['street', 'street2'] for bg in ultimos_bg[-3:]):
            bg_image = 'grass'
        elif len(ultimos_bg) >= 3 and all(bg == 'grass' for bg in ultimos_bg[-3:]):
            bg_image = random.choice(['street', 'street2', 'railway'])
        elif len(ultimos_bg) >= 3 and all(bg == 'railway' for bg in ultimos_bg[-3:]):
            bg_image = 'grass'
        else:
            bg_image = random.choice(available_backgrounds)


        # Atualiza ultimos_bg
        backgrounds.add(bg)
        ultimos_bg.append(bg_image)
        if len(ultimos_bg) > 3:
            ultimos_bg.pop(0)


    # Corrige max_y (mínimo y entre backgrounds)
        max_y = min(back.rect.y for back in backgrounds)
        y = max_y - 75

        bg = Background(bg_image, y, "novo")

        if bg.tipo in ['street', 'street2']:
            car_image = random.choice(available_cars)
            carro = Carro(bg.rect.y, 5, 1, assets[car_image])
            all_sprites.add(carro)
            all_cars.add(carro)

        elif bg.tipo == 'railway':
            train = Train(bg.rect.y, 5, 1, assets['train'])
            all_sprites.add(train)
            all_trains.add(train)

        backgrounds.add(bg)
        
        all_cars.update()
        all_trains.update()
        backgrounds.update()
        player.update()

        hits = []
        for car in all_cars:
            if player.rect.colliderect(car.hitbox):
                hits.append(car)
                car.kill()
        hits2 = []
        for train in all_trains:
            if player.rect.colliderect(train.hitbox):
                hits2.append(train)
                train.kill()

        if hits or hits2:
            return True

        window.fill(GREEN2)
        backgrounds.draw(window)
        all_sprites.draw(window)
        pygame.display.update()
    
    return True

# Loop principal do jogo (modificado para remover recorde e pontos)
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