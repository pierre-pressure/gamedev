import pygame

FPS = 60

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Schwarzes Fenster 1 - The Beginning Of The Void!")

clock = pygame.time.Clock()
frame_count = 0

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

    # ----------------------------------------------------------------------------------------------------

    screen.fill((0, 0, 0))

    pygame.display.flip()

    frame_count += 1
    if frame_count % 60 == 0:
        fps = clock.get_fps()
        print(f"Game Loop läuft... FPS: {fps:.0f}")

    clock.tick(FPS)

# ----------------------------------------------------------------------------------------------------

print("Spiel wurde beendet!")
pygame.quit()
