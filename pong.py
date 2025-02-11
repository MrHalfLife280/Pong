import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle dimensions
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Ball dimensions
BALL_SIZE = 10

# Speeds
PADDLE_SPEED = 6
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Initialize paddles and ball positions
player1_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Ball velocity
ball_vel_x = BALL_SPEED_X
ball_vel_y = BALL_SPEED_Y

# Scores
player1_score = 0
player2_score = 0

# Font for displaying scores
font = pygame.font.Font(None, 74)

def reset_ball():
    global ball_vel_x, ball_vel_y
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_vel_x *= -1
    ball_vel_y = BALL_SPEED_Y if ball_vel_y > 0 else -BALL_SPEED_Y

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys
    keys = pygame.key.get_pressed()

    # Player 1 controls
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_paddle.bottom < HEIGHT:
        player1_paddle.y += PADDLE_SPEED

    # Player 2 controls
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_paddle.bottom < HEIGHT:
        player2_paddle.y += PADDLE_SPEED

    # Move ball
    ball.x += ball_vel_x
    ball.y += ball_vel_y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_vel_y *= -1

    # Ball collision with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_vel_x *= -1

    # Ball goes out of bounds
    if ball.left <= 0:
        player2_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        player1_score += 1
        reset_ball()

    # Drawing everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1_paddle)
    pygame.draw.rect(screen, WHITE, player2_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    screen.blit(player1_text, (WIDTH // 4, 20))
    screen.blit(player2_text, (WIDTH // 4 * 3, 20))

    # Update display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

pygame.quit()
sys.exit() 