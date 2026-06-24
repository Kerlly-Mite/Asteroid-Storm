import pygame

from model import create_initial_state
from config import WIDTH, HEIGHT, DEFAULT_ASTEROIDS

from simulation import update_sequential, update_parallel
from render import init_screen, draw


def main():

    screen = init_screen(WIDTH, HEIGHT)

    state = create_initial_state(
        DEFAULT_ASTEROIDS,
        WIDTH,
        HEIGHT
    )

    clock = pygame.time.Clock()

    running = True

    use_parallel = False

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    use_parallel = not use_parallel

        if use_parallel:
            state = state.__class__(
                update_parallel(state.asteroids, 4)
            )
        else:
            state = state.__class__(
                update_sequential(state.asteroids)
            )

        draw(screen, state.asteroids)

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()