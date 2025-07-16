import pygame

pygame.init()

FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HEIGHT = 600
WIDTH = 800
PLAYER_H = 50
PLAYER_W = 50

frame_count = 0
player_vely = 5
player_velx = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bewegliche Rechtecke 2 - Jetzt erst recht-eck")
player = pygame.Rect(WIDTH / 2 - PLAYER_W / 2, HEIGHT / 2 - PLAYER_H / 2, 50, 50)

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

    player.x += player_velx
    if player.right >= WIDTH:
        player_velx *= -1
        player.right = WIDTH
    elif player.left <= 0:
        player_velx *= -1
        player.left = 0

    # ----------------------------------------------------------------------------------------------------

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player)

    pygame.display.flip()

    frame_count += 1
    if frame_count % 60 == 0:
        fps = clock.get_fps()
        print(f"Gameloop läuft mit {fps:.0f} FPS")

    clock.tick(FPS)

# ----------------------------------------------------------------------------------------------------

print("Spiel wurde beendet")
pygame.quit()
