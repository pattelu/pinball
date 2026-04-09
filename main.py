import pygame
from sys import exit

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
result_font = pygame.font.Font(None, 30)
result_surf = result_font.render("RESULT: ", True, "grey")
result_rect = result_surf.get_rect(center=((screen_x / 2), 20))

# Paddles
paddle_size_x, paddle_size_y = (20, 80)
paddle_surf = pygame.Surface((paddle_size_x, paddle_size_y))
paddle_surf.fill("white")

paddle1_rect = paddle_surf.get_rect(center=(paddle_size_x + 5, screen_y / 2))
paddle2_rect = paddle_surf.get_rect(
    center=(screen_x - (paddle_size_x + 5), screen_y / 2)
)

# p1_paddle_pos = pygame.Vector2(10, 10)
# p2_paddle_pos = pygame.Vector2(screen_x-30, 10)


while running:

    # Close game on [x]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render elements
    screen.fill("black")
    screen.blit(result_surf, result_rect)
    screen.blit(paddle_surf, paddle1_rect)
    screen.blit(paddle_surf, paddle2_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if paddle1_rect.top >= 0:
            paddle1_rect.top -= 300 * dt
    if keys[pygame.K_s]:
        if (paddle1_rect.bottom) <= screen_y:
            paddle1_rect.bottom += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
exit()
