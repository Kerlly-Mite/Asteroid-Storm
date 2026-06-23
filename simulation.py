from model import Asteroid
from multiprocessing import Pool


# ==================================
# ACTUALIZAR UN ASTEROIDE
# ==================================

def update_asteroid(asteroid):

    return Asteroid(
        x=asteroid.x + asteroid.vx,
        y=asteroid.y + asteroid.vy,
        vx=asteroid.vx,
        vy=asteroid.vy,
        size=asteroid.size
    )


# ==================================
# ACTUALIZACION SECUENCIAL
# ==================================

def update_sequential(asteroids):

    return tuple(
        update_asteroid(asteroid)
        for asteroid in asteroids
    )

# ==================================
# ACTUALIZACION PARALELA
# ==================================

def update_parallel(
        asteroids,
        workers):

    with Pool(workers) as pool:

        result = pool.map(
            update_asteroid,
            asteroids
        )

    return tuple(result)