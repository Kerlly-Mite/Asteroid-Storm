from time import perf_counter

from model import create_initial_state

from simulation import (
    update_sequential,
    update_parallel
)

from config import WORKERS


def benchmark(amount):

    state = create_initial_state(
        amount,
        1200,
        700
    )

    start = perf_counter()

    for _ in range(100):

        update_sequential(
            state.asteroids
        )

    sequential_time = (
        perf_counter() - start
    )

    start = perf_counter()

    for _ in range(100):

        update_parallel(
            state.asteroids,
            WORKERS
        )

    parallel_time = (
        perf_counter() - start
    )

    print()
    print(
        "Asteroides:",
        amount
    )

    print(
        "Secuencial:",
        round(
            sequential_time,
            3
        ),
        "segundos"
    )

    print(
        "Paralelo:",
        round(
            parallel_time,
            3
        ),
        "segundos"
    )


if __name__ == "__main__":

    benchmark(1000)

    benchmark(3000)

    benchmark(5000)