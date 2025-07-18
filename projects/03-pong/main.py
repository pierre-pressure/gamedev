import pygame

pygame.init()

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HEIGHT = 600
WIDTH = 800
PLAYER_W = 20
PLAYER_H = 200
PLAYER_X = WIDTH - 30
ENEMY_W = 20
ENEMY_H = 200
ENEMY_X = 30
BALL_SIZE = 10

frame_count = 0
player_vely = 5
enemy_vely = 5
ball_vely = 3
ball_velx = 4
player_y = HEIGHT / 2 - PLAYER_H / 2
enemy_y = HEIGHT / 2 - ENEMY_H / 2
ball_x = WIDTH / 2
ball_y = HEIGHT / 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong 3")
player = pygame.Rect(PLAYER_X, player_y, PLAYER_W, PLAYER_H)
enemy = pygame.Rect(ENEMY_X, enemy_y, ENEMY_W, ENEMY_H)

clock = pygame.time.Clock()

# ----------------------------------------------------------------------------------------------------

running = True
while running:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        running = False

    # ----------------------------------------------------------------------------------------------------

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.y -= player_vely
    elif keys[pygame.K_s]:
        player.y += player_vely

    enemy.y += enemy_vely
    if enemy.bottom >= HEIGHT:
        enemy_vely *= -1
        enemy.bottom = HEIGHT
    elif enemy.top <= 0:
        enemy_vely *= -1
        enemy.top = 0

    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT
    elif player.top <= 0:
        player.top = 0

    ball_y += ball_vely
    ball_x += ball_velx

    if ball_y - BALL_SIZE <= 0:
        ball_vely *= -1
        ball_y = BALL_SIZE
    elif ball_y + BALL_SIZE >= HEIGHT:
        ball_vely *= -1
        ball_y = HEIGHT - BALL_SIZE
    if ball_x - BALL_SIZE <= 0:
        ball_velx *= -1
        ball_x = BALL_SIZE
    elif ball_x + BALL_SIZE >= WIDTH:
        ball_velx *= -1
        ball_x = WIDTH - BALL_SIZE

    # ----------------------------------------------------------------------------------------------------

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, enemy)
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_SIZE)

    pygame.display.flip()

    frame_count += 1
    if frame_count % 60 == 0:
        fps = clock.get_fps()
        print(f"Gameloop läuft mit {fps:.0f} FPS")

    clock.tick(FPS)

# ----------------------------------------------------------------------------------------------------

print("Spiel wurde beendet!")
pygame.quit()
