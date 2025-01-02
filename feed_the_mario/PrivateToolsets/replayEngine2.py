import os
import zlib
import time
import pygame
import random

import pyperclip

os.system("cls || clear")
telemetry = eval(zlib.decompress(eval(pyperclip.paste())).decode())
print("[FtM Replay Engine BETA]")
print("This replay engine runs on the game, Feed the Mario.")
print("The engine still uses some logic to keep the game event log size low.")
print("\nThe engine is, however, NOT an exact replica of FtM. Movement is disabled.")
print("The original game assets are still required for the replay engine.")
print("Be warned - data from older clients WON'T work with this engine!")
input("\nTelemetry loaded. Press ENTER to start replaying.")

os.chdir(os.path.dirname(__file__))
pygame.init()

WINDOW_WIDTH = telemetry["window_width"]
WINDOW_HEIGHT = telemetry["window_height"]
SCALE_WIDTH = (WINDOW_WIDTH // 600)
SCALE_HEIGHT = (WINDOW_HEIGHT // 300)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("FtM | Replay Engine")

FPS = telemetry["fps"]
clock = pygame.time.Clock()

MARIO_VELOCITY = 6 * SCALE_HEIGHT
COIN_VELOCITY = 2 * SCALE_WIDTH

# Load images and initalize inital placements for said images
mario_image = pygame.image.load("mario.png")
mario_image = pygame.transform.scale(mario_image, (40 * SCALE_WIDTH, 60 * SCALE_HEIGHT))
mario_rect = mario_image.get_rect()
mario_rect.center = (WINDOW_WIDTH * 0.1, WINDOW_HEIGHT*0.165 + WINDOW_HEIGHT*0.4175)

luigi_image = pygame.image.load("luigi.png")
luigi_image = pygame.transform.scale(luigi_image, (40 * SCALE_WIDTH, 60 * SCALE_HEIGHT))
luigi_rect = luigi_image.get_rect()
luigi_rect.center = (WINDOW_WIDTH * 0.1, WINDOW_HEIGHT*0.165 + WINDOW_HEIGHT*0.6175)

coin_image = pygame.image.load("coin.png")
coin_image = pygame.transform.scale(coin_image, (28 * SCALE_WIDTH, 32 * SCALE_HEIGHT))
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

bg_overworld = pygame.image.load("overworld.png")
bg_overworld = pygame.transform.scale(bg_overworld, (WINDOW_WIDTH, WINDOW_HEIGHT))
bg_underground = pygame.image.load("underground.png")
bg_underground = pygame.transform.scale(bg_underground, (WINDOW_WIDTH, WINDOW_HEIGHT))

'''
pipe_image = pygame.image.load("pipe.png")
pipe_image = pygame.transform.scale(pipe_image, (48 * SCALE_WIDTH, 32 * SCALE_HEIGHT))
pipe_rect = pipe_image.get_rect()
pipe_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
'''

#DEFAULT_COLOR = (235, 185, 47)
#DEFAULT_COLOR = (168, 82, 50)
DEFAULT_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initalize fonts
attack_font = pygame.font.Font('SuperMario.ttf', 32 * SCALE_WIDTH)
big_attack_font = pygame.font.Font('SuperMario.ttf', 48 * SCALE_WIDTH)
small_attack_font = pygame.font.Font('SuperMario.ttf', 24 * SCALE_WIDTH)

main_text = attack_font.render("Replaying...", True, DEFAULT_COLOR)
main_text_rect = main_text.get_rect()
main_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.9)

# Initalize starting variables
score = 0
lives = telemetry["lives"]
players = telemetry["players"]

collect_coin = pygame.mixer.Sound("coin.mp3")
collect_coin.set_volume(0.1)
damage = pygame.mixer.Sound("damage.mp3")
pygame.mixer.music.load("overworld.mp3")
pygame.mixer.music.play(-1, 0.0)

# Initalize the text for the splash screen
splash_text = big_attack_font.render("Feed the Mario!", True, DEFAULT_COLOR)
splash_text_rect = splash_text.get_rect()
splash_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Initalize text using the fonts above
lives_text = small_attack_font.render(f"Lives: {lives}", True, DEFAULT_COLOR)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.95)

score_text = small_attack_font.render(f"Score: {score}", True, DEFAULT_COLOR)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (WINDOW_WIDTH - WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.95)

'''
telemetry = {
    "window_width": WINDOW_WIDTH,
    "window_height": WINDOW_HEIGHT,
    "fps": FPS,
    "lives": lives,
    "players": players,
    "coin_velocity": COIN_VELOCITY,
    "player_velocity": MARIO_VELOCITY,
    "data": []
}
'''
running = True
in_underground = False
for tick in telemetry["data"]:
    mario_rect.x = tick["mario_pos"][0]
    mario_rect.y = tick["mario_pos"][1]

    coin_rect.x = tick["coin_pos"][0]
    coin_rect.y = tick["coin_pos"][1]

    if telemetry["players"] == 2:
        luigi_rect.x = tick["luigi_pos"][0]
        luigi_rect.y = tick["luigi_pos"][1]

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            raise SystemExit

    if coin_rect.colliderect(mario_rect):
        score += 1
        collect_coin.play()
        score_text = small_attack_font.render(f"Score: {score}", True, DEFAULT_COLOR)

        COIN_VELOCITY += round(0.2 * SCALE_HEIGHT, 1)
    
    if coin_rect.colliderect(luigi_rect) and players == 2:
        score += 1
        collect_coin.play()
        score_text = small_attack_font.render(f"Score: {score}", True, DEFAULT_COLOR)

        COIN_VELOCITY += round(0.2 * SCALE_HEIGHT, 1)

    if coin_rect.x <= 0:
        lives -= 1
        damage.play()
        lives_text = small_attack_font.render(f"Lives: {lives}", True, DEFAULT_COLOR)
    else:
        coin_rect.x -= COIN_VELOCITY    

    if lives == 0:
        lives_text = small_attack_font.render(f"Lives: {lives}", True, RED)
        score_text = small_attack_font.render(f"Score: {score}", True, RED)
        main_text = attack_font.render("Game Over D:", True, RED)
        main_text_rect = main_text.get_rect()
        main_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.9)

    display_surface.fill(BLACK)
    if in_underground:
        display_surface.blit(bg_underground, (0, 0))
    else:
        display_surface.blit(bg_overworld, (0, 0))

    display_surface.blit(mario_image, mario_rect)
    if players == 2:
        display_surface.blit(luigi_image, luigi_rect)
    display_surface.blit(coin_image, coin_rect)

    display_surface.blit(main_text, main_text_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(lives_text, lives_text_rect)

    pygame.draw.rect(display_surface, (0, 255, 0), mario_rect, 1)
    pygame.draw.rect(display_surface, (0, 255, 0), coin_rect, 1)

    pygame.display.update()
    clock.tick(FPS)

    if lives == 0:
        enter_underground = False
        pygame.display.update()
        pygame.mixer.music.load("GameOver.mp3")
        pygame.mixer.music.play(-1, 0.0)
        time.sleep(3)
        raise SystemExit

    if score == 50 and not in_underground:
        in_underground = True

        DEFAULT_COLOR = (235, 185, 47)
        main_text = attack_font.render("Replaying...", True, DEFAULT_COLOR)
        main_text_rect = main_text.get_rect()
        main_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.9)

        lives_text = small_attack_font.render(f"Lives: {lives}", True, DEFAULT_COLOR)
        score_text = small_attack_font.render(f"Score: {score}", True, DEFAULT_COLOR)

        coin_image = pygame.image.load("coin_underground.png")
        coin_image = pygame.transform.scale(coin_image, (28 * SCALE_WIDTH, 32 * SCALE_HEIGHT))
        coin_rect = coin_image.get_rect()
        coin_rect.x = WINDOW_WIDTH - 32
        coin_rect.y = random.randint(round(WINDOW_HEIGHT * 0.165), round(WINDOW_HEIGHT * 0.75))

        pygame.mixer.music.stop()
        pygame.mixer.music.load("underground.mp3")
        pygame.mixer.music.play(-1, 0.0)

pygame.quit()