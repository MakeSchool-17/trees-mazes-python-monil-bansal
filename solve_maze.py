import maze
import generate_maze
import sys
import random

def do_dfs(m, current_cell, goal_cell):
    m.refresh_maze_view()
    if current_cell == goal_cell:
        return True
    neighbors = m.cell_neighbors(current_cell)
   
    while(len(neighbors)):
        sz = len(neighbors)
        idx = random.randint(0,sz-1)
        neighbor, compass_idx = neighbors[idx]
        m.visit_cell(current_cell,neighbor,compass_idx)
        if(do_dfs(m,neighbor,goal_cell)):
            return True
        neighbors = m.cell_neighbors(current_cell)

    m.backtrack(current_cell)

# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    current_cell = 0
    goal_cell = m.total_cells - 1
    do_dfs(m,current_cell,goal_cell)


# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    # TODO: Implement solve_bfs
    pass


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
