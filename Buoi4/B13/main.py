import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fruit Picker")

# Load images (replace with your actual image files)
background = pygame.image.load("background.png").convert()
basket_img = pygame.image.load("basket.png").convert_alpha()
fruit_imgs = [
    pygame.image.load("apple.png").convert_alpha(),
    pygame.image.load("banana.png").convert_alpha(),
    pygame.image.load("orange.png").convert_alpha(),
    # Add more fruit images...
]


# Basket class
class Basket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = basket_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed


# Fruit class
class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom > screen_height:
            self.kill()  # Remove fruit from all sprite groups


# Sprite groups
all_sprites = pygame.sprite.Group()
fruits = pygame.sprite.Group()
basket = Basket(screen_width // 2 - basket_img.get_width() // 2, screen_height - 100)
all_sprites.add(basket)


# Game loop
running = True
clock = pygame.time.Clock()
fruit_spawn_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Spawn fruits
    fruit_spawn_timer += clock.get_time()
    if fruit_spawn_timer > 1000:  # Spawn a fruit every 1000 milliseconds (1 second)
        fruit_spawn_timer = 0
        fruit = Fruit(random.randint(0, screen_width - fruit_imgs[0].get_width()), 0, random.choice(fruit_imgs))
        all_sprites.add(fruit)
        fruits.add(fruit)

    # Update game objects
    all_sprites.update()

    # Check for collisions (add your collision detection logic here)
    collisions = pygame.sprite.spritecollide(basket, fruits, True)  # Remove fruits on collision


    # Draw everything
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)  # 60 FPS

pygame.quit()