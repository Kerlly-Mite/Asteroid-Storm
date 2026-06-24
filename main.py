import pygame
import sys
import random

# --------------------
# INICIALIZACIÓN
# --------------------
pygame.init()

ANCHO = 800
ALTO = 600

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Asteroid Storm")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# --------------------
# OBJETO SIMPLE (ejemplo jugador)
# --------------------
player = pygame.Rect(400, 500, 50, 50)
speed = 5

# --------------------
# LOOP PRINCIPAL
# --------------------
running = True

while running:

    # Control de FPS (60 FPS máximo)
    dt = clock.tick(60)
    fps = clock.get_fps()

    # --------------------
    # EVENTOS
    # --------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --------------------
    # MOVIMIENTO
    # --------------------
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # --------------------
    # RENDER
    # --------------------
    screen.fill((0, 0, 0))

    # jugador
    pygame.draw.rect(screen, (0, 255, 0), player)

    # FPS en pantalla
    fps_text = font.render(f"FPS: {int(fps)}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()

# --------------------
# SALIDA
# --------------------
pygame.quit()
sys.exit()