import pygame
from sys import exit
import random


def display_score():
    result_surf = result_font.render(f"RESULT: {p1_score}:{p2_score}", True, "grey")
    result_rect = result_surf.get_rect(center=((screen_x / 2), 20))
    screen.blit(result_surf, result_rect)


def game_over(player):
    player += 1
    ball_rect.x = screen_x / 2
    ball_rect.y = screen_y / 2
    return player


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
paddle_speed = 500

paddle1_rect = paddle_surf.get_rect(center=(paddle_size_x + 5, screen_y / 2))
paddle2_rect = paddle_surf.get_rect(
    center=(screen_x - (paddle_size_x + 5), screen_y / 2)
)

# Ball
ball_surf = pygame.image.load("img/ball.png").convert_alpha()
ball_rect = ball_surf.get_rect(center=(screen_x / 2, screen_y / 2))

ball_h_speed = 400
ball_v_speed = random.randint(200, 400)

while running:

    # Close game on [x]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render elements
    screen.fill("black")
    display_score()
    pygame.draw.line(screen, "grey", (screen_x / 2, 30), (screen_x / 2, screen_y - 5))
    screen.blit(ball_surf, ball_rect)
    screen.blit(paddle_surf, paddle1_rect)
    screen.blit(paddle_surf, paddle2_rect)

    # Controls for P1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if paddle1_rect.centery >= 0:
            paddle1_rect.centery -= paddle_speed * dt
    if keys[pygame.K_s]:
        if (paddle1_rect.centery) <= screen_y:
            paddle1_rect.centery += paddle_speed * dt

    # Controls for P2
    # if keys[pygame.K_UP]:
    #     if paddle2_rect.top >= 0:
    #         paddle2_rect.top -= paddle_speed * dt
    # if keys[pygame.K_DOWN]:
    #     if (paddle2_rect.bottom) <= screen_y:
    #         paddle2_rect.bottom += paddle_speed * dt

    # Simple AI for P2 Bot
    if paddle2_rect.centery <= 0:
        paddle2_rect.centery = 1
    if paddle2_rect.centery >= screen_y:
        paddle2_rect.centery = screen_y - 1
    if ball_rect.centerx > (screen_x - (screen_y / 3)):
        if paddle2_rect.centery > ball_rect.centery:
            paddle2_rect.centery -= paddle_speed * dt
        if paddle2_rect.centery < ball_rect.centery:
            paddle2_rect.centery += paddle_speed * dt

    # Move ball
    ball_rect.centerx += ball_h_speed * dt
    ball_rect.centery += ball_v_speed * dt

    # Change direction to oppsite  if end of screen
    if ball_rect.bottom >= screen_y:
        ball_rect.bottom = screen_y - 1
        ball_v_speed = -ball_v_speed
    if ball_rect.top <= 0:
        ball_rect.top = 1
        ball_v_speed = -ball_v_speed

    # Chang direction to oposite if paddle is touched
    if paddle1_rect.colliderect(ball_rect):
        ball_h_speed = -ball_h_speed
    if paddle2_rect.colliderect(ball_rect):
        ball_h_speed = -ball_h_speed

    # Game Over
    if ball_rect.left > screen_x:
        p1_score = game_over(p1_score)
    if ball_rect.right < 0:
        p2_score = game_over(p2_score)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
exit()
