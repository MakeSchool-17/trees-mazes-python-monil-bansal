import maze
import random

def do_dfs(m,visited_till_now,current_cell):
	m.refresh_maze_view()
	if(visited_till_now == m.total_cells):
		return
	visited_till_now += 1
	neighbors = m.cell_neighbors(current_cell)
	while(len(neighbors)):
		sz = len(neighbors)
		idx = random.randint(0,sz-1)
		neighbor, compass_idx = neighbors[idx]
		m.connect_cells(current_cell,neighbor,compass_idx)
		do_dfs(m,visited_till_now,neighbor)
		neighbors = m.cell_neighbors(current_cell)

# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    visited_till_now = 0
    total_cells = m.total_cells
    current_cell = random.randint(0,total_cells-1)
    do_dfs(m,visited_till_now,current_cell)
    m.refresh_maze_view()
    m.state = 'solve'


def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
