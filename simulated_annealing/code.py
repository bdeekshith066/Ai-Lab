# Function to calculate the heuristic
def calculate_heuristic(state):
    heuristic = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:  # Same column
                heuristic += 1
            if abs(state[i] - state[j]) == abs(i - j):  # Same diagonal
                heuristic += 1
    return heuristic

# Function to generate neighboring states by swapping
def generate_neighbors(state):
    neighbors = []
    n = len(state)
    # Generate neighbors by swapping positions of two queens
    for i in range(n):
        for j in range(i + 1, n):
            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]  # Swap
            neighbors.append(new_state)
    return neighbors

# Function to print the board as a 2D array
def print_board(state):
    n = len(state)
    board = [['.'] * n for _ in range(n)]
    for row in range(n):
        board[row][state[row]] = 'Q'
    for row in board:
        print(' '.join(row))
    print()

# Hill Climbing algorithm for N-Queens with swapping
def hill_climbing_n_queens(initial_state):
    current_state = initial_state
   
    while True:
        current_heuristic = calculate_heuristic(current_state)
        print(f"Current State: {current_state}, Heuristic: {current_heuristic}")
        print_board(current_state)  # Print the current board
       
        if current_heuristic == 0:
            return current_state
       
        neighbors = generate_neighbors(current_state)
        best_neighbor = None
        best_heuristic = float('inf')
       
        for neighbor in neighbors:
            heuristic = calculate_heuristic(neighbor)
            if heuristic < best_heuristic:
                best_heuristic = heuristic
                best_neighbor = neighbor
       
        if best_heuristic >= current_heuristic:
            break  # Stop if no better neighbor found
       
        current_state = best_neighbor
   
    return None  # No solution found

# Main function to solve the N-Queens problem
def solve_n_queens():
    # Set the initial state for 4 queens
    initial_state = [3, 1, 2, 0]  # Fixed state
    solution = hill_climbing_n_queens(initial_state)
   
    if solution:
        print(f"Solution found for 4-Queens problem: {solution}")
        print_board(solution)  # Print the final board
    else:
        print("No solution found.")

# Run the solver
solve_n_queens()