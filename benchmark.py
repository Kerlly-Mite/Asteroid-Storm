import pygame
import time
import sys

def run_benchmark(duration=10):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Benchmark Asteroid Storm")

    clock = pygame.time.Clock()
    frames = 0
    start_time = time.time()

    running = True
    while running:
        clock.tick(60)  # límite de FPS
        frames += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()

        if time.time() - start_time >= duration:
            running = False

    elapsed_time = time.time() - start_time
    avg_fps = frames / elapsed_time

    pygame.quit()

    print("----- BENCHMARK RESULT -----")
    print(f"Duración: {elapsed_time:.2f} segundos")
    print(f"Frames renderizados: {frames}")
    print(f"FPS promedio: {avg_fps:.2f}")

    return avg_fps


if __name__ == "__main__":
    run_benchmark()