import matplotlib.pyplot as plt
import numpy as np

def plot_environment(environment, title):
    ''' Plots the environment
    Args:
        environment (list): list of lists representing the environment
        title (str): title of the plot
    '''
    rows = len(environment)
    cols = len(environment[0])

    # -- set colors
    dark_yellow = (0.8, 0.8, 0)

    # Get the coordinates of the non-black cells
    x_coords_obs = []
    y_coords_obs = []
    x_coord_start = []
    y_coord_start = []
    x_coord_goal = []
    y_coord_goal = []
    x_coord_empty = []
    y_coord_empty = []

    for row in range(rows):
        for col in range(cols):
            if environment[row][col] == '#':
                x_coords_obs.append(col)
                y_coords_obs.append(row)
            elif environment[row][col] == 'S':
                x_coord_start.append(col)
                y_coord_start.append(row)
            elif environment[row][col] == 'G':
                x_coord_goal.append(col)
                y_coord_goal.append(row)
            else:
                x_coord_empty.append(col)
                y_coord_empty.append(row)

    # Generate the scatter plot
    plt.scatter(x_coords_obs, y_coords_obs, color='black', marker='o',s=200)
    plt.scatter(x_coord_start, y_coord_start, color='blue', marker='o', s=100)
    plt.scatter(x_coord_goal, y_coord_goal, color='green', marker='*',s=200)
    plt.scatter(x_coord_empty, y_coord_empty, color=dark_yellow, marker='o',s=50)
    plt.show()

def grid_to_graph_four_neighbor(grid):
    '''converts a grid into a graph represented as a dictionary
    Args:
        grid (list): list of lists representing the grid
    Returns:
        graph (dict): dictionary representing the graph
    '''
    graph = {}
    rows = len(grid)
    cols = len(grid[0])

    def is_valid_cell(row, col):
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] != '#'

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '#':
                neighbors = []
                # Check 4 neighbors: up, down, left, right
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row, new_col = row + dr, col + dc
                    if is_valid_cell(new_row, new_col):
                        neighbors.append(((new_row, new_col),1)) # neighbor and cost
                graph[(row, col)] = neighbors
    return graph

def grid_to_graph_eight_neighbor(grid):
    '''converts a grid into a graph represented as a dictionary
    Args:
        grid (list): list of lists representing the grid
    Returns:
        graph (dict): dictionary representing the graph
    '''
    graph = {}
    rows = len(grid)
    cols = len(grid[0])

    def is_valid_cell(row, col):
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] != '#'

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '#':
                neighbors = []
                # Check 4 neighbors: up, down, left, right
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row, new_col = row + dr, col + dc
                    if is_valid_cell(new_row, new_col):
                        neighbors.append(((new_row, new_col),1)) # neighbor and cost
                # check 4 diagonal neighbors
                for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    new_row, new_col = row + dr, col + dc
                    if is_valid_cell(new_row, new_col):
                        neighbors.append(((new_row, new_col),1.414))
                graph[(row, col)] = neighbors

    return graph

def read_environment_file(filename):
    ''' Reads the text file and loads the content into a list of lists. 
    Args:
        filename (str): path to the file
    Returns:
        grid_env (list): list of lists representing the grid
    '''
    grid_env = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            line = line.strip()
            # -- convert line into list of characters
            line = line.split(' ')
            grid_env.append(list(line))
            line = f.readline()
    return grid_env

def plot_path(grid, path, title):
    rows = len(grid)
    cols = len(grid[0])

    # -- set colors
    dark_yellow = (0.8, 0.8, 0)

    # Get the coordinates of the non-black cells
    x_coords_obs = []
    y_coords_obs = []
    x_coord_start = []
    y_coord_start = []
    x_coord_goal = []
    y_coord_goal = []
    x_coord_empty = []
    y_coord_empty = []

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '#':
                x_coords_obs.append(col)
                y_coords_obs.append(row)
            elif grid[row][col] == 'S':
                x_coord_start.append(col)
                y_coord_start.append(row)
            elif grid[row][col] == 'G':
                x_coord_goal.append(col)
                y_coord_goal.append(row)
            else:
                x_coord_empty.append(col)
                y_coord_empty.append(row)

    # Generate the scatter plot
    plt.scatter(x_coords_obs, y_coords_obs, color='black', marker='o',s=200)
    plt.scatter(x_coord_start, y_coord_start, color='blue', marker='o', s=100)
    plt.scatter(x_coord_goal, y_coord_goal, color='green', marker='*',s=200)
    plt.scatter(x_coord_empty, y_coord_empty, color=dark_yellow, marker='o',s=50)

    # -- plot the path
    x_coords_path = []
    y_coords_path = []
    for node in path:
        x_coords_path.append(node[1])
        y_coords_path.append(node[0])
    plt.plot(x_coords_path, y_coords_path, color='red', linewidth=3)
    
    # -- set title
    plt.title(title)

    # -- show plot 
    plt.show()

    # -- return
    return

def get_start_goal(grid):
    ''' Returns the start and goal locations in the grid
    Args:
        grid (list): list of lists representing the grid
    Returns:
        start (tuple): start location
        goal (tuple): goal location
    '''
    rows = len(grid)
    cols = len(grid[0])
    start = None
    goal = None
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'S':
                start = (row, col)
            elif grid[row][col] == 'G':
                goal = (row, col)
    return start, goal
