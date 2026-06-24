from multiprocessing import Pool
from model import Asteroid


def update_asteroid(asteroid):

    return Asteroid(
        x=asteroid.x + asteroid.vx,
        y=asteroid.y + asteroid.vy,
        vx=asteroid.vx,
        vy=asteroid.vy,
        size=asteroid.size
    )


def update_sequential(asteroids):

    return tuple(

        update_asteroid(asteroid)

        for asteroid in asteroids

    )


def update_parallel(
        asteroids,
        workers):

    with Pool(workers) as pool:

        result = pool.map(
            update_asteroid,
            asteroids
        )

    return tuple(result)