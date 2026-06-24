from model import create_initial_state


state = create_initial_state(
    10,
    800,
    600
)

print("Cantidad de asteroides:")
print(len(state.asteroids))

print()

print("Primer asteroide:")
print(state.asteroids[0])