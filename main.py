import pygame
import random
from config import WIDTH, HEIGHT, WHITE, FPS, PLAYER_WIDTH, PLAYER_HEIGHT, CAR_WIDTH, CAR_HEIGHT, ROAD_WIDTH, ROAD_HEIGHT, TRAIN_WIDTH, TRAIN_HEIGHT, GREEN2, TREE_LOG_WIDTH, TREE_LOG_HEIGHT,TRAIN_HITBOX_WIDTH, TRAIN_HITBOX_HEIGHT, CAR_HITBOX_WIDTH, CAR_HITBOX_HEIGHT

# Iniciar pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Crossy Road 2.0")
clock = pygame.time.Clock()

# Carregar assets
assets = {}
assets['player_image'] = pygame.image.load('Assets/Armature_jumping_left_1.png').convert_alpha()
assets['player_image'] = pygame.transform.scale(assets['player_image'], (PLAYER_WIDTH, PLAYER_HEIGHT))
assets['tree_log'] = pygame.image.load('Assets/objects/the wood.png').convert_alpha()
assets['tree_log'] = pygame.transform.scale(assets['tree_log'], (TREE_LOG_WIDTH, TREE_LOG_HEIGHT))
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
assets['water'] = pygame.image.load('Assets/Roads/Water2.png').convert_alpha()
assets['water'] = pygame.transform.scale(assets['water'], (ROAD_WIDTH, ROAD_HEIGHT))
assets['train'] = pygame.image.load('Assets/train front.png').convert_alpha()
assets['train'] = pygame.transform.scale(assets['train'], (TRAIN_WIDTH, TRAIN_HEIGHT))
assets['tela_inicio'] = pygame.image.load('Assets/tela_inicial.png').convert_alpha()
assets['tela_inicio'] = pygame.transform.scale(assets['tela_inicio'], (WIDTH, HEIGHT))
assets['tela_fim'] = pygame.image.load('Assets/tela_game_over2.png').convert_alpha()
assets['tela_fim'] = pygame.transform.scale(assets['tela_fim'], (WIDTH, HEIGHT))

available_backgrounds = ['railway', 'street2', 'water']
available_cars = ['car_black', 'car_blue', 'car_brown', 'car_red']

# Função para mostrar a tela inicial
def show_start_screen():
    window.blit(assets['tela_inicio'], (0, 0)) 
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                    return True

# Função para mostrar a tela de game over
def show_game_over_screen(score, recorde):
    window.blit(assets['tela_fim'], (0, 0))
    font = pygame.font.SysFont(None, 48)

    text = font.render(f"Pontos: {score}", True, (255, 255, 255))
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 210))

    text2 = font.render(f"Recorde: {recorde}", True, (255, 255, 0))
    window.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT - 160))

    text3 = font.render("R - Reiniciar | ESC - Sair", True, (200, 200, 200))
    window.blit(text3, (WIDTH // 2 - text3.get_width() // 2, HEIGHT - 110))

    pygame.display.flip()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # reiniciar
                elif event.key == pygame.K_ESCAPE:
                    return False  # sair
# Classe do jogador
class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = assets['player_image']
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2
        self.is_jumping = False
        self.jump_velocity_y = -(ROAD_HEIGHT/10)
        self.jump_velocity_x = 0
        self.gravity = 1.2
        self.vel_y = 0
        self.vel_x = 0
        self.ground_y = self.rect.y
    
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

    def jump(self):

        if not self.is_jumping:
            self.is_jumping = True
            self.vel_y = self.jump_velocity_y
            self.vel_x = self.jump_velocity_x
            scroll_speed = 10

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
        if self.is_jumping:
            self.rect.y += self.vel_y
            self.rect.x += self.vel_x
            self.vel_y += self.gravity

            if self.rect.y >= self.ground_y:
                self.rect.y = self.ground_y
                self.is_jumping = False
                self.vel_y = 0
                self.vel_x = 0

# Classe carro
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
        # Crie um retângulo de colisão menor que a imagem
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
        # Atualize a posição do hitbox para acompanhar o trem
        self.hitbox.center = self.rect.center

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
    def __init__(self, tipo, y, id):
        super().__init__()
        self.image = assets[tipo]
        self.rect = self.image.get_rect()
        self.tipo = tipo
        self.rect.y = y
        self.rect.x = 0
        self.id = id
        self.scroll_speed = 1.2
    
    def update(self):
        self.rect.y += self.scroll_speed

# Função principal do jogo
def game():
    score = 0
    start_ticks = pygame.time.get_ticks()
    backgrounds = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_cars = pygame.sprite.Group()
    all_trains = pygame.sprite.Group()
    all_tree_log = pygame.sprite.Group()

    for i in range(-10, 10):
        bg = Background(random.choice(available_backgrounds), i * 150, i)

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
        
        if bg.tipo in ['water']:
            tree_log_image = assets['tree_log']
            tree_log = Tree_log(bg.rect.y, 5, 1, tree_log_image)
            all_sprites.add(tree_log)
            all_tree_log.add(tree_log)

        backgrounds.add(bg)

    # Criação de objetos 
    player = Player(assets['player_image'])
    all_sprites.add(player)

    running = True
    while running:
        clock.tick(FPS)

        # eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                elif event.key == pygame.K_LEFT:
                    player.move_by(-30, -5)
                elif event.key == pygame.K_RIGHT:
                    player.move_by(+30, +5)
                elif event.key == pygame.K_DOWN:
                    player.move_by(-15, +40)
                elif event.key == pygame.K_ESCAPE:
                    return True  # Voltar ao menu
            
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        score = int(seconds * 2)
        
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

        novo_tree_log = False
        kill_tree_log = False
        for tree_log in all_tree_log:
            if tree_log.rect.left > WIDTH:
                kill_tree_log = True
                novo_tree_log = True
        if kill_tree_log:
            for tree_log in all_tree_log:
                tree_log.kill()
            kill_tree_log = False
        if novo_tree_log:
            novo_tree_log = False    
            for bg in backgrounds:
                if bg.tipo in ['water']:
                    tree_log_image = assets['tree_log']
                    tree_log = Tree_log(bg.rect.y, 5, 1, tree_log_image)
                    all_sprites.add(tree_log)
                    all_tree_log.add(tree_log)

        novo_bg = False
        for bg in backgrounds:
            if bg.rect.bottom > HEIGHT + 150:
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
            bg = Background(random.choice(available_backgrounds), y, "novo")
            
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
            
            if bg.tipo in ['water']:
                tree_log_image = assets['tree_log']
                tree_log = Tree_log(bg.rect.y, 5, 1, tree_log_image)
                all_sprites.add(tree_log)
                all_tree_log.add(tree_log)

            backgrounds.add(bg)
        
        # Atualizações
        all_cars.update()
        all_trains.update()
        all_tree_log.update()
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
            score = abs(player.rect.y // 40)  # exemplo de score com base na subida
            return score

        # Desenhos
        fonte = pygame.font.SysFont("Arial", 36)
        texto_score = fonte.render(f"Pontos: {score}", True, (255, 255, 255))
        window.fill(GREEN2)
        backgrounds.draw(window)
        all_sprites.draw(window)
        window.blit(texto_score, (10, 10))

        pygame.display.update()


    return True

# Loop principal do jogo
recorde = 0
playing = True
while playing:
    if show_start_screen():
        score = game()
        if score > recorde:
            recorde = score
        continuar = show_game_over_screen(score, recorde)
        while continuar:
            score = game()
            if score > recorde:
                recorde = score
            continuar = show_game_over_screen(score, recorde)
    else:
        playing = False


pygame.quit()
