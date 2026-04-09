import pygame
from sys import exit
import random

def dispaly_score():
    result_surf = result_font.render(f"RESULT: {p1_score}:{p2_score}", True, "grey")
    result_rect = result_surf.get_rect(center=((screen_x / 2), 20))
    screen.blit(result_surf, result_rect)

# pygame setup
pygame.init()
running = True
clock = pygame.time.Clock()
dt = 0

# Display
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pinball")

screen_x, screen_y = pygame.display.get_window_size()

# Points
p1_score = 0
p2_score = 0

# Fonts
result_font = pygame.font.Font(None, 30)

# Paddles
paddle_size_x, paddle_size_y = (20, 80)
paddle_surf = pygame.Surface((paddle_size_x, paddle_size_y))
paddle_surf.fill("white")
paddle_speed = 300

paddle1_rect = paddle_surf.get_rect(center=(paddle_size_x + 5, screen_y / 2))
paddle2_rect = paddle_surf.get_rect(center=(screen_x - (paddle_size_x + 5), screen_y / 2))

# Ball
ball_surf = pygame.image.load("img/ball.png").convert_alpha()
ball_rect = ball_surf.get_rect(center=(screen_x/2, screen_y/2))

ball_h_speed = 400 
ball_v_speed = (random.randint(100, 400))

while running:

    # Close game on [x]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render elements
    screen.fill("black")
    dispaly_score()
    pygame.draw.line(screen, "grey", (screen_x/2, 30), (screen_x/2, screen_y - 5))
    screen.blit(ball_surf, ball_rect)
    screen.blit(paddle_surf, paddle1_rect)
    screen.blit(paddle_surf, paddle2_rect)

    print(f"Result: {p2_score}")

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if paddle1_rect.top >= 0:
            paddle1_rect.top -= paddle_speed * dt
    if keys[pygame.K_s]:
        if (paddle1_rect.bottom) <= screen_y:
            paddle1_rect.bottom += paddle_speed * dt

    if keys[pygame.K_UP]:
        if paddle2_rect.top >= 0:
            paddle2_rect.top -= paddle_speed * dt
    if keys[pygame.K_DOWN]:
        if (paddle2_rect.bottom) <= screen_y:
            paddle2_rect.bottom += paddle_speed * dt

    # Move ball
    ball_rect.x += ball_h_speed * dt
    ball_rect.y += ball_v_speed * dt

    # Change direction to oppsite  if end of screen
    if ball_rect.bottom >= screen_y or ball_rect.top <= 0:
        ball_v_speed = -ball_v_speed

    # Chang direction to oposite if paddle is touched
    if paddle1_rect.colliderect(ball_rect):
        ball_h_speed = -ball_h_speed
    if paddle2_rect.colliderect(ball_rect):
        ball_h_speed = -ball_h_speed

    # Game Over
    if ball_rect.left >= screen_x:
        print("Game Over")
        p1_score += 1
        # Restar ball / stop game
    if ball_rect.right <= 0: 
        print("Game Over")
        p2_score += 1
        # Restar ball / stop game

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
exit()
