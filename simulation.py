from model import Asteroid


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