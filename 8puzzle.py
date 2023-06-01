import heapq

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, None]]

def heuristic(state):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != goal_state[i][j])

class State:
    def __init__(self, state, g_cost, parent):
        self.state = state
        self.g_cost = g_cost
        self.h_cost = heuristic(state)
        self.parent = parent

    def __lt__(self, other):
        return (self.g_cost + self.h_cost) < (other.g_cost + other.h_cost)

    def __eq__(self, other):
        return self.state == other.state

def solve_puzzle(initial_state):
    open_list = []
    closed_list = set()

    initial_state_obj = State(initial_state, 0, None)
    heapq.heappush(open_list, initial_state_obj)

    while open_list:
        current_state = heapq.heappop(open_list)
        closed_list.add(tuple(map(tuple, current_state.state)))

        if current_state.state == goal_state:
            path = []
            while current_state:
                path.append(current_state.state)
                current_state = current_state.parent
            return path[::-1]

        row, col = next((i, j) for i in range(3) for j in range(3) if current_state.state[i][j] is None)

        for i, j in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= i < 3 and 0 <= j < 3:
                new_state = [list(row) for row in current_state.state]
                new_state[row][col], new_state[i][j] = new_state[i][j], new_state[row][col]

                if tuple(map(tuple, new_state)) not in closed_list:
                    new_state_obj = State(new_state, current_state.g_cost + 1, current_state)
                    heapq.heappush(open_list, new_state_obj)

    return None

initial_state = [[1, 3, None], [4, 2, 5], [7, 8, 6]]
solution = solve_puzzle(initial_state)

if solution:
    print("Solution found!")
    for state in solution:
        print("\n".join(str(row) for row in state))
        print()
else:
    print("No solution found.")
