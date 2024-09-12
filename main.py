import pygame
import random
import time

pygame.init()

#  экран
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Monsters")

# изображений
rocket_img = pygame.image.load('kisspng-rocket-spacecraft-clip-art-paper-firework-5ac68db91609a0.0154008115229618490903 — копия.png')
rocket_img = pygame.transform.scale(rocket_img, (50, 50))  # Изменяем размер ракеты
monster_img = pygame.image.load('d822390713090ba1a6e94b9e35f4381f — копия.png')
monster_img = pygame.transform.scale(monster_img, (50, 50))  # Изменяем размер монстра
background_img = pygame.image.load('backround.jpg')
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))  # Фон под экран

# Переменные 
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

block_width = 50
block_height = 50
block_speed = 5
blocks = []

score = 0
font = pygame.font.Font(None, 36) 

#  монстры
def create_block():
    block_x = random.randint(0, WIDTH - block_width)
    block_y = -block_height
    return [block_x, block_y]

# текст
def display_text(text, duration=2, font_size=36):
    font = pygame.font.Font(None, font_size)
    text_surf = font.render(text, True, (255, 255, 255))
    text_rect = text_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(background_img, (0, 0))  #  фон
    screen.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(duration)

display_text("Разработчик: Ифтихор Хайдаралиев", duration=3, font_size=36)

# Основа цыкллл
running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Упрв ракетой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < WIDTH - player_size:
        player_x += player_speed

    # движение монстров
    if random.randint(1, 20) == 1:
        blocks.append(create_block())

    for block in blocks[:]:
        block[1] += block_speed
        if block[1] > HEIGHT:
            blocks.remove(block)
            score += 1

    # проверка столкновени
    for block in blocks:
        if (player_x < block[0] < player_x + player_size or player_x < block[0] + block_width < player_x + player_size) and \
           (player_y < block[1] < player_y + player_size or player_y < block[1] + block_height < player_y + player_size):
            running = False
            break

    # Экран
    screen.blit(background_img, (0, 0))  #  фон

    # Ракеты
    screen.blit(rocket_img, (player_x, player_y))

    # Монстр
    for block in blocks:
        screen.blit(monster_img, (block[0], block[1]))

    # Счёт
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()

