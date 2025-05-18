# Simple game example using Pygame
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Rain")

# Colors
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Player paddle
player_width, player_height = 100, 20
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - 50
player_speed = 10

# Raindrop
drop_size = 15
drop_x = random.randint(0, screen_width - drop_size)
drop_y = 0
drop_speed = 5

# Game variables
score = 0
clock = pygame.time.Clock()
game_font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed
    
    # Update raindrop
    drop_y += drop_speed
    
    # Check if raindrop was caught
    if (drop_y + drop_size >= player_y and
        drop_x + drop_size >= player_x and
        drop_x <= player_x + player_width):
        score += 1
        drop_x = random.randint(0, screen_width - drop_size)
        drop_y = 0
        drop_speed += 0.2  # Increase difficulty
    
    # Check if raindrop was missed
    if drop_y > screen_height:
        drop_x = random.randint(0, screen_width - drop_size)
        drop_y = 0
    
    # Drawing
    screen.fill((0, 0, 0))  # Clear screen
    
    # Draw player paddle
    pygame.draw.rect(screen, WHITE, 
                    (player_x, player_y, player_width, player_height))
    
    # Draw raindrop
    pygame.draw.circle(screen, BLUE, 
                      (drop_x + drop_size//2, drop_y + drop_size//2), 
                      drop_size//2)
    
    # Draw score
    score_text = game_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    # Update display
    pygame.display.flip()
    
    # Control game speed
    clock.tick(60)

pygame.quit()
