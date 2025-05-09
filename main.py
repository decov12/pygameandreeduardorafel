import pygame
from config import WIDTH, HEIGHT, WHITE, FPS

# Iniciar pygame
pygame.init
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

# Criação de objetos 
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Loop principal do pygame:

running = True
while running:
    clock.tick(FPS)

    # eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizacoes

    # Desenhos
    window.fill(WHITE)

    pygame.display.update()
pygame.quit()