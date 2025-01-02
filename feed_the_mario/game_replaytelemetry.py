# Import necessary modules!
import os
import time
import pygame
import random

# Modules required for logging everything about your game
import zlib
import requests
import getpass

# CD into the working directory, with all the assets
os.chdir(os.path.dirname(__file__))

# Initalize pygame
# SCALE_WIDTH and SCALE_HEIGHT allow for you to play this game at any resolution.
# However, you should play this game at a 2:1 (W:H) pixel ratio.
pygame.init()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
SCALE_WIDTH = (WINDOW_WIDTH // 600)
SCALE_HEIGHT = (WINDOW_HEIGHT // 300)
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed Mario!")

FPS = 60
clock = pygame.time.Clock()

MARIO_VELOCITY = 6 * SCALE_HEIGHT
COIN_VELOCITY = 2 * SCALE_WIDTH

# Load images and initalize inital placements for said images
mario_image = pygame.image.load("./Assets/Images/mario.png")
mario_image = pygame.transform.scale(mario_image, (40 * SCALE_WIDTH, 60 * SCALE_HEIGHT))
mario_rect = mario_image.get_rect()
mario_rect.center = (WINDOW_WIDTH * 0.1, WINDOW_HEIGHT*0.165 + WINDOW_HEIGHT*0.4175)

luigi_image = pygame.image.load("./Assets/Images/luigi.png")
luigi_image = pygame.transform.scale(luigi_image, (40 * SCALE_WIDTH, 60 * SCALE_HEIGHT))
luigi_rect = luigi_image.get_rect()
luigi_rect.center = (WINDOW_WIDTH * 0.1, WINDOW_HEIGHT*0.165 + WINDOW_HEIGHT*0.6175)

coin_image = pygame.image.load("./Assets/Images/coin.png")
coin_image = pygame.transform.scale(coin_image, (28 * SCALE_WIDTH, 32 * SCALE_HEIGHT))
coin_rect = coin_image.get_rect()
coin_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

bg_overworld = pygame.image.load("./Assets/Backgrounds/overworld.png")
bg_overworld = pygame.transform.scale(bg_overworld, (WINDOW_WIDTH, WINDOW_HEIGHT))
bg_underground = pygame.image.load("./Assets/Backgrounds/underground.png")
bg_underground = pygame.transform.scale(bg_underground, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Initalize colors to be used throughout the game
DEFAULT_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initalize fonts
attack_font = pygame.font.Font('./Assets/Fonts/SuperMario.ttf', 32 * SCALE_WIDTH)
big_attack_font = pygame.font.Font('./Assets/Fonts/SuperMario.ttf', 48 * SCALE_WIDTH)
small_attack_font = pygame.font.Font('./Assets/Fonts/SuperMario.ttf', 24 * SCALE_WIDTH)

main_text = attack_font.render("Coins...", True, DEFAULT_COLOR)
main_text_rect = main_text.get_rect()
main_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.9)

# Initalize starting variables
score = 0
lives = 5

collect_coin = pygame.mixer.Sound("./Assets/SFX/coin.mp3")
collect_coin.set_volume(0.1)
damage = pygame.mixer.Sound("./Assets/SFX/damage.mp3")
going_underground = pygame.mixer.Sound("./Assets/SFX/going_underground.mp3")
pygame.mixer.music.load("./Assets/BGM/overworld.mp3")
pygame.mixer.music.play(-1, 0.0)

# Initalize the text for the splash screen
splash_text = big_attack_font.render("Feed the Mario!", True, DEFAULT_COLOR)
splash_text_rect = splash_text.get_rect()
splash_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Display the splash screen, along with the option for 2 players.
players = 1
splash_screen = True
while splash_screen:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            raise SystemExit
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        splash_screen = False

    display_surface.fill(BLACK)

    menuOption = 1
    if menuOption == 1:
        if keys[pygame.K_LEFT] and players == 2:
            players = 1
        if keys[pygame.K_RIGHT] and players == 1:
            players = 2
        description_text = small_attack_font.render(f"< # Players: {players} >", True, DEFAULT_COLOR)
        description_text_rect = description_text.get_rect()
        description_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT * 0.7)

    display_surface.blit(splash_text, splash_text_rect)
    display_surface.blit(description_text, description_text_rect)
    pygame.display.update()
MARIO_VELOCITY = MARIO_VELOCITY // players
COIN_VELOCITY = COIN_VELOCITY * players

# Initalize text using the fonts above
lives_text = small_attack_font.render(f"Lives: {lives}", True, DEFAULT_COLOR)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.95)

score_text = small_attack_font.render(f"Score: {score}", True, DEFAULT_COLOR)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (WINDOW_WIDTH - WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.95)

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
running = True
in_underground = False
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            raise SystemExit
    
    # If Mario (P1) collides with a coin, increase the score
    if mario_rect.colliderect(coin_rect):
        score += 1
        collect_coin.play()
        score_text = small_attack_font.render(f"Score: {score}", True, DEFAULT_COLOR)

        coin_rect.x = WINDOW_WIDTH - 32
        coin_rect.y = random.randint(round(WINDOW_HEIGHT * 0.165), round(WINDOW_HEIGHT * 0.75))
        COIN_VELOCITY += round(0.2 * SCALE_HEIGHT, 1) * players
    
    # If Luigi (P2) collides with a coin AND there are actually 2 players, increase the score
    # Change the player count by pressing the Left/Right arrow keys on the main menu!
    if coin_rect.colliderect(luigi_rect) and players == 2:
        score += 1
        collect_coin.play()
        score_text = small_attack_font.render(f"Score: {score}", True, DEFAULT_COLOR)

        coin_rect.x = WINDOW_WIDTH - 32
        coin_rect.y = random.randint(round(WINDOW_HEIGHT * 0.165), round(WINDOW_HEIGHT * 0.75))
        COIN_VELOCITY += round(0.2 * SCALE_HEIGHT, 1) * players

    # Move Mario (P1) based on keyboard inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and mario_rect.top > WINDOW_HEIGHT * 0.165 and mario_rect.top > WINDOW_HEIGHT * 0.165:
        mario_rect.y -= MARIO_VELOCITY
    if in_underground:
        if keys[pygame.K_DOWN] and mario_rect.bottom < WINDOW_HEIGHT * 0.92:
            mario_rect.y += MARIO_VELOCITY
    else:
        if keys[pygame.K_DOWN] and mario_rect.bottom < WINDOW_HEIGHT * 0.9:
            mario_rect.y += MARIO_VELOCITY

    # Move Luigi (P2) based on keyboard inputs
    if keys[pygame.K_w] and luigi_rect.top > WINDOW_HEIGHT * 0.165:
        luigi_rect.y -= MARIO_VELOCITY
    if in_underground:
        if keys[pygame.K_s] and luigi_rect.bottom < WINDOW_HEIGHT * 0.92:
            luigi_rect.y += MARIO_VELOCITY
    else:
        if keys[pygame.K_s] and luigi_rect.bottom < WINDOW_HEIGHT * 0.9:
            luigi_rect.y += MARIO_VELOCITY

    # If the coin touches the edge, the player loses a life
    if coin_rect.x <= 0:
        lives -= 1
        damage.play()
        lives_text = small_attack_font.render(f"Lives: {lives}", True, DEFAULT_COLOR)
        coin_rect.x = WINDOW_WIDTH - 32
        coin_rect.y = random.randint(round(WINDOW_HEIGHT * 0.165), round(WINDOW_HEIGHT * 0.75))
    else:
        coin_rect.x -= COIN_VELOCITY

    # If you have no lives, display the game over screen
    if lives == 0:
        running = False

        lives_text = small_attack_font.render(f"Lives: {lives}", True, RED)
        score_text = small_attack_font.render(f"Score: {score}", True, RED)
        if in_underground:
            main_text = attack_font.render("Game Over!", True, RED)
            main_text_rect = main_text.get_rect()
            main_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.935)
        else:
            main_text = attack_font.render("Game Over!", True, RED)
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
    
    if lives > 0:
        display_surface.blit(coin_image, coin_rect)

    display_surface.blit(main_text, main_text_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(lives_text, lives_text_rect)

    pygame.display.update()
    clock.tick(FPS)

    if lives == 0:
        pygame.mixer.music.load("./Assets/SFX/game_over.mp3")
        pygame.mixer.music.play(-1, 0.0)
        time.sleep(3)

    # If you reach 50 coins, you will be taken to a new world...
    # New assets are loaded to fit the underground theme.
    if score == 50 and not in_underground:
        display_surface.fill(BLACK)
        pygame.mixer.music.stop()
        pygame.display.update()
        going_underground.play()
        pygame.time.delay(3000)
        in_underground = True

        DEFAULT_COLOR = (235, 185, 47)
        main_text = attack_font.render("Collect em!", True, DEFAULT_COLOR)
        main_text_rect = main_text.get_rect()
        main_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.935)

        lives_text = small_attack_font.render(f"Lives: {lives}", True, DEFAULT_COLOR)
        lives_text_rect.topright = (WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.98)

        score_text = small_attack_font.render(f"Score: {score}", True, DEFAULT_COLOR)
        score_text_rect.topleft = (WINDOW_WIDTH - WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.98)

        coin_image = pygame.image.load("./Assets/Images/coin_underground.png")
        coin_image = pygame.transform.scale(coin_image, (28 * SCALE_WIDTH, 32 * SCALE_HEIGHT))
        coin_rect = coin_image.get_rect()
        coin_rect.x = WINDOW_WIDTH - 32
        coin_rect.y = random.randint(round(WINDOW_HEIGHT * 0.165), round(WINDOW_HEIGHT * 0.75))

        pygame.mixer.music.load("./Assets/BGM/underground.mp3")
        pygame.mixer.music.play(-1, 0.0)

    telemetry["data"].append({
        "mario_pos": (mario_rect.x, mario_rect.y),
        "luigi_pos": (luigi_rect.x, mario_rect.y),
        "coin_pos": (coin_rect.x, coin_rect.y)
    })

# If you somehow lose due to a skill issue, the pygame window actually closes.
pygame.quit()

from io import BytesIO

print("You died! Sending your score to the leaderboard...")
telemetry = zlib.compress(str(telemetry).encode())
if len(str(telemetry)) > 1024 ** 2 * 8:
    telemetry = "Telemetry too large to send."
open("game.log", "w").write(str(telemetry))
file_buffer = BytesIO(open(f"game.log", "rb").read())

# Your scores and your entire run are sent to a Discord channel via a Discord webhook.
# I'd be impressed if you get a score of 200 in this game!
data = {
    "content": f"Name: {getpass.getuser()}\nScore: {score}"
}
files = {
    "file": (
        "game.log",
        file_buffer
    )
}
post_score_request = requests.post("https://discord.com/api/webhooks/1313650038802616330/o6XopbjI1xuvnFNzObqs4Xtq9PuxmwaSqRpVMNHSIdKB1ceLyYfjUo6J36nJ-_AI-y6V", data=data, files=files)

if post_score_request.ok:
    print("Score successfully sent.")
else:
    print("Failed to send your score.")