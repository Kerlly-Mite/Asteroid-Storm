from dataclasses import dataclass
from random import randint


@dataclass(frozen=True)
class Asteroid:

    x: float
    y: float
    vx: float
    vy: float
    size: int


@dataclass(frozen=True)
class GameState:

    asteroids: tuple


def create_asteroids(amount, width, height):

    return tuple(

        Asteroid(
            x=randint(0, width),
            y=randint(0, height),
            vx=randint(-3, 3) or 1,
            vy=randint(-3, 3) or 1,
            size=randint(2, 5)
        )

        for _ in range(amount)

    )


def create_initial_state(amount, width, height):

    return GameState(

        asteroids=create_asteroids(
            amount,
            width,
            height
        )

    )