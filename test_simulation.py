from model import create_initial_state
from simulation import update_sequential


state = create_initial_state(
    5,
    800,
    600
)

new_asteroids = update_sequential(
    state.asteroids
)

print("Antes:")
print(state.asteroids[0])

print("\nDespues:")
print(new_asteroids[0])