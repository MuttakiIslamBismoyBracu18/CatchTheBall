import pip

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player
player_size = 50
player_x = (WIDTH - player_size) // 2
player_y = HEIGHT - player_size - 20
player_speed = 10

# Ball
ball_size = 30
ball_x = random.randint(0, WIDTH - ball_size)
ball_y = 0
ball_speed = 5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Move the ball
    ball_y += ball_speed
    if ball_y > HEIGHT:
        ball_y = 0
        ball_x = random.randint(0, WIDTH - ball_size)

    # Check for collision
    if (
        player_x < ball_x < player_x + player_size
        and player_y < ball_y < player_y + player_size
    ):
        ball_y = 0
        ball_x = random.randint(0, WIDTH - ball_size)

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.ellipse(screen, RED, (ball_x, ball_y, ball_size, ball_size))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)
