import pygame

from model import create_initial_state

from simulation import (
    update_sequential,
    update_parallel
)

from render import (
    init_screen,
    draw
)

from config import (
    WIDTH,
    HEIGHT,
    DEFAULT_ASTEROIDS,
    WORKERS
)


def main():

    screen = init_screen(
        WIDTH,
        HEIGHT
    )

    font = pygame.font.SysFont(
        None,
        30
    )

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

                    use_parallel = (
                        not use_parallel
                    )

        if use_parallel:

            state = state.__class__(

                update_parallel(
                    state.asteroids,
                    WORKERS
                )

            )

        else:

            state = state.__class__(

                update_sequential(
                    state.asteroids
                )

            )

        draw(
            screen,
            state.asteroids
        )

        fps = clock.get_fps()

        mode = (
            "PARALELO"
            if use_parallel
            else
            "SECUENCIAL"
        )

        text = font.render(

            f"FPS: {fps:.2f} | {mode}",

            True,

            (255, 255, 255)

        )

        screen.blit(
            text,
            (10, 10)
        )

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()