##
Algorithm
- **Initialize**: Start with the initial state and goal state.
- **For each state**:
  - Calculate \( g(n) \) (depth of the node).
  - Calculate \( h(n) \) (number of misplaced tiles).
  - Compute \( f(n) = g(n) + h(n) \).
  - Add the state to the open list and track visited states.
- **Expand**: Select the state with the lowest \( f(n) \) and generate its neighbors by swapping the blank tile with neighboring tiles.
- **Continue** until the goal state is reached or the open list is empty.
*/
##

import heapq

def misplaced_tiles(state, goal):
    return sum(1 for i in range(3) for j in range(3) 
               if state[i][j] != goal[i][j] and state[i][j] != 0)

def get_neighbors(state):
    neighbors = []
    blank = [(i, j) for i in range(3) for j in range(3) if state[i][j] == 0][0]
    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    x, y = blank

    for dx, dy in possible_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors

def print_path(path):
    for state in path:
        for row in state:
            print(row)
        print()

def astar_misplaced(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + misplaced_tiles(start, goal), start, 0, []))  # (f, state, g, path)
    visited = set()

    while open_list:
        f, current, g, path = heapq.heappop(open_list)
        path = path + [current]

        if current == goal:
            print("Solution Found (Misplaced Tiles):")
            print_path(path)
            return g  # Return the depth (number of moves)

        for neighbor in get_neighbors(current):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                visited.add(neighbor_tuple)
                h = misplaced_tiles(neighbor, goal)
                heapq.heappush(open_list, (g + 1 + h, neighbor, g + 1, path))

    return -1  # No solution found

# Example usage
start = [[5, 4, 0], [6, 1, 8], [7, 3, 2]]
goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
astar_misplaced(start, goal)