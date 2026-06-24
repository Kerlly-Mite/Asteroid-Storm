import pygame


def init_screen(width, height):

    pygame.init()

    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Asteroid Storm")

    return screen


def draw(screen, asteroids):

    screen.fill((0, 0, 0))

    for a in asteroids:

        pygame.draw.circle(
            screen,
            (200, 200, 200),
            (int(a.x), int(a.y)),
            a.size
        )

    pygame.display.flip()