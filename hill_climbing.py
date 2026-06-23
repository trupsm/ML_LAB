# Objective function
def objective_function(x):
    return -(x - 5)**2 + 25
# Hill Climbing Algorithm
def hill_climbing(start, step_size, max_iterations):
    # Current position
    current = start
    current_value = objective_function(current)
    print("Starting Point =", current)
    print("Function Value =", current_value)
    print()
    for i in range(max_iterations):
        # Generate neighboring solutions
        left = current - step_size
        right = current + step_size
        # Evaluate neighbors
        left_value = objective_function(left)
        right_value = objective_function(right)
        # Move to better neighbor
        if left_value > current_value:
            current = left
            current_value = left_value
        elif right_value > current_value:
            current = right
            current_value = right_value
        else:
            # Local optimum reached
            break
    return current, current_value
# Main Program
start_position = float(input("Enter starting position: "))
step_size = float(input("Enter step size: "))
max_iterations = int(input("Enter maximum iterations: "))
best_x, best_value = hill_climbing(start_position,step_size,max_iterations)
print("\nOptimal Solution Found")
print("x =", round(best_x, 2))
print("Maximum Value =", round(best_value, 2))