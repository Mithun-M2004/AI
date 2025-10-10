def hill_climbing(initial_state, get_neighbors, objective_function):
    current_state = initial_state
    current_value = objective_function(current_state)

    while True:
        neighbors = get_neighbors(current_state)
        if not neighbors:
            break

        neighbor_values = [(n, objective_function(n)) for n in neighbors]
        best_neighbor, best_value = max(neighbor_values, key=lambda x: x[1])

        if best_value <= current_value:
            break

        current_state = best_neighbor
        current_value = best_value

    return current_state, current_value

def get_neighbors(x):
    neighbors = []
    if x > 0:
        neighbors.append(x - 1)
    if x < 10:
        neighbors.append(x + 1)
    return neighbors

def objective_function(x):
    return -x**2 + 4*x

best_state, best_value = hill_climbing(0, get_neighbors, objective_function)
print(f"Best state: {best_state}, Best value: {best_value}")
