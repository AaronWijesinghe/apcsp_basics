import os
import time
import pygame
import random

os.chdir(os.path.dirname(__file__))

# Initalize pygame
pygame.init()
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Steve!")

# Set FPS
FPS = 60
clock = pygame.time.Clock()
   
# Load images
heart_image = pygame.image.load("./Assets/Images/heart.png")
heart_image = pygame.transform.scale(heart_image, (40, 40))
heart_rect = heart_image.get_rect()
heart_rect.center = (WINDOW_WIDTH * 0.92, WINDOW_HEIGHT * 0.06)

steve_image = pygame.image.load("./Assets/Images/steve.png")
steve_image = pygame.transform.scale(steve_image, (64, 64))
steve_rect = steve_image.get_rect()
steve_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Load teacher jumpscares :D
teacher_images = [
    "./Assets/Images/goyco.jpg",
    "./Assets/Images/henriques.jpg",
    "./Assets/Images/peterson.jpg",
    "./Assets/Images/chu.jpg"
]
teacher = pygame.image.load(teacher_images[random.randint(0, len(teacher_images) - 1)])
teacher_rect = teacher.get_rect()
teacher_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# Load background image
bg = pygame.image.load("./Assets/Backgrounds/background.png")
bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Initalize colors
DEFAULT_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initalize starting variables
score = 0
lives = 5
steve_velocity = 1
game_rect = pygame.Rect(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

# Initalize fonts and text using said fonts
big_font = pygame.font.Font("./Assets/Fonts/minecraft.ttf", 75)
font = pygame.font.Font("./Assets/Fonts/minecraft.ttf", 35)

main_text = font.render("Catch The Steve!", True, DEFAULT_COLOR)
main_text_rect = main_text.get_rect()
main_text_rect.center = (WINDOW_WIDTH // 1.87, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.93)

score_text = font.render(f"Score: {score}", True, DEFAULT_COLOR)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (WINDOW_WIDTH - WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.98)

lives_text = font.render(f"{lives}", True, DEFAULT_COLOR)
lives_text_rect = lives_text.get_rect()
lives_text_rect.topright = (WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.98)

click_sound = pygame.mixer.Sound("./Assets/SFX/click.mp3")
click_sound.set_volume(0.05)
miss_sound = pygame.mixer.Sound("./Assets/SFX/miss.mp3")
miss_sound.set_volume(0.1)
die = pygame.mixer.Sound("./Assets/SFX/game_over.mp3")
die.set_volume(0.5)

pygame.mixer.music.load("./Assets/BGM/background_music.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(1.0)

# This is my implementation of determining the direction of Steve.
# This function also makes sure that Steve doesn't go out-of-bounds.
dx, dy = 0, 0
def set_direction():
    global dx, dy
    global steve_velocity
    global steve_rect
    global game_rect
    global FPS

    FPS = 600
    dx = [-1, 1][random.randint(0, 1)] * steve_velocity
    dy = [-1, 1][random.randint(0, 1)] * steve_velocity
    if not game_rect.contains(steve_rect):
        if steve_rect.left <= 0 or steve_rect.right >= WINDOW_WIDTH:
            dx = -dx
        if steve_rect.top <= 0 or steve_rect.bottom >= WINDOW_HEIGHT:
            dy = -dy
    FPS = 60
set_direction()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            raise SystemExit
        
        # If the player clicks on Steve, they gain a point and Steve gets faster
        # Otherwise, the player LOSES a life!
        if event.type == pygame.MOUSEBUTTONDOWN:
            if steve_rect.collidepoint(pygame.mouse.get_pos()):
                click_sound.play()
                steve_velocity += 0.25
                score += 1
                steve_rect.center = (random.randint(64, WINDOW_WIDTH - 64), random.randint(64, WINDOW_HEIGHT - 64))
                score_text = font.render(f"Score: {score}", True, DEFAULT_COLOR)
            else:
                lives -= 1
                if lives > 0:
                    miss_sound.play()
                else:
                    die.play()
                lives_text = font.render(f"{lives}", True, DEFAULT_COLOR)
            set_direction()

    # Making sure Steve stays in frame...
    if not game_rect.contains(steve_rect):
        set_direction()
    steve_rect.x += dx
    steve_rect.y += dy
    
    display_surface.fill(BLACK)
    display_surface.blit(bg, (0, 0))

    # Display the text and player
    display_surface.blit(main_text, main_text_rect)
    display_surface.blit(score_text, score_text_rect)
    display_surface.blit(lives_text, lives_text_rect)

    display_surface.blit(heart_image, heart_rect)
    display_surface.blit(steve_image, steve_rect)

    pygame.display.update()
    clock.tick(FPS)

    # Jumpscare + game over screen loop
    if lives == 0:
        display_surface.fill(BLACK)
        display_surface.blit(bg, (0, 0))
        teacher_image_default = teacher

        # A jumpscare is shown to the user.
        # This uses everyone's favorite teachers!
        start_jumpscare = time.time()
        for _ in range(1, 200):
            if time.time() - start_jumpscare >= 1:
                break

            teacher_image = pygame.transform.scale_by(teacher_image_default, _/50)
            teacher_rect = teacher_image.get_rect()
            teacher_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

            display_surface.blit(teacher_image, teacher_rect)
            pygame.display.update()

        game_over_text = big_font.render("Game Over!", True, DEFAULT_COLOR)
        game_over_rect = game_over_text.get_rect()
        game_over_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        restart_text = font.render("Press ENTER to restart.", True, DEFAULT_COLOR)
        restart_rect = restart_text.get_rect()
        restart_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.2)
    
        # Display game over screen, and the option to restart the game
        game_over = True
        while game_over:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    raise SystemExit
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        score = 0
                        lives = 5
                        steve_velocity = 1
                        game_over = False
                        set_direction()

                        teacher = pygame.image.load(teacher_images[random.randint(0, len(teacher_images) - 1)])
                        teacher_rect = teacher.get_rect()
                        teacher_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

                        score_text = font.render(f"Score: {score}", True, DEFAULT_COLOR)
                        score_text_rect = score_text.get_rect()
                        score_text_rect.topleft = (WINDOW_WIDTH - WINDOW_WIDTH * 0.98, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.98)

                        lives_text = font.render(f"{lives}", True, DEFAULT_COLOR)
                        lives_text_rect = lives_text.get_rect()
                        lives_text_rect.topright = (WINDOW_WIDTH * 0.985, WINDOW_HEIGHT - WINDOW_HEIGHT * 0.98)
                    else:
                        raise SystemExit
            
            display_surface.fill(BLACK)
            display_surface.blit(game_over_text, game_over_rect)
            display_surface.blit(restart_text, restart_rect)
            pygame.display.update()

pygame.quit()