import os
import zlib
import time
import pygame
import pyperclip

os.chdir(os.path.dirname(__file__))
pygame.init()

telemetry = eval(pyperclip.paste())
telemetry = eval(zlib.decompress(telemetry).decode())

WINDOW_WIDTH = telemetry["window_width"]
WINDOW_HEIGHT = telemetry["window_height"]
SCALE_WIDTH = (WINDOW_WIDTH // 600)
SCALE_HEIGHT = (WINDOW_HEIGHT // 300)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Replay Engine")

FPS = telemetry["fps"]
clock = pygame.time.Clock()

MARIO_VELOCITY = 6 * SCALE_HEIGHT
COIN_VELOCITY = 2 * SCALE_WIDTH

# Load images and initalize inital placements for said images
mario_image = pygame.image.load("mario.png")
mario_image = pygame.transform.scale(mario_image, (64 * SCALE_WIDTH, 54 * SCALE_HEIGHT))
mario_rect = mario_image.get_rect()
mario_rect.topleft = (32, 48)

coin_image = pygame.image.load("coin.png")
coin_image = pygame.transform.scale(coin_image, (32 * SCALE_WIDTH, 32 * SCALE_HEIGHT))
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

YELLOW = (235, 185, 47)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initalize fonts
attack_font = pygame.font.Font('SuperMario.ttf', 32 * SCALE_WIDTH)
small_attack_font = pygame.font.Font('SuperMario.ttf', 24 * SCALE_WIDTH)

main_text = attack_font.render("Replaying...", True, YELLOW)
main_text_rect = main_text.get_rect()
main_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.9)

# Initalize text using the fonts above, alongside other variables
score = 0
score_text = small_attack_font.render(f"Score: {score}", True, YELLOW)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (WINDOW_WIDTH - WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.95)

lives = 5
lives_text = small_attack_font.render(f"Lives: {lives}", True, YELLOW)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.95)

collect_coin = pygame.mixer.Sound('coin.mp3')
pygame.mixer.music.load("overworld.mp3")
pygame.mixer.music.play(-1, 0.0)

for tick in telemetry["data"]:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

    coin_rect.x = tick["coinPos"][0]
    coin_rect.y = tick["coinPos"][1]

    mario_rect.x = tick["marioPos"][0]
    mario_rect.y = tick["marioPos"][1]

    if mario_rect.colliderect(coin_rect):
        collect_coin.play()
        score += 1
        score_text = small_attack_font.render(f"Score: {score}", True, YELLOW)

        COIN_VELOCITY += 0.2 * SCALE_HEIGHT
        COIN_VELOCITY = round(COIN_VELOCITY, 1)

    if coin_rect.x <= 0:
        lives -= 1
        lives_text = small_attack_font.render(f"Lives: {lives}", True, YELLOW)
    else:
        coin_rect.x -= COIN_VELOCITY
    
    if lives == 0:
        lives_text = small_attack_font.render(f"Lives: {lives}", True, RED)
        score_text = small_attack_font.render(f"Score: {score}", True, RED)
        main_text = attack_font.render("Game Over D:", True, RED)
        main_text_rect = main_text.get_rect()
        main_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.9)

    display_surface.fill(BLACK)

    display_surface.blit(mario_image, mario_rect)
    display_surface.blit(coin_image, coin_rect)

    display_surface.blit(main_text, main_text_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(lives_text, lives_text_rect)

    pygame.display.update()
    clock.tick(FPS)

    if lives == 0:
        pygame.mixer.music.load("GameOver.mp3")
        pygame.mixer.music.play(-1, 0.0)
        time.sleep(3)
        break

pygame.quit()