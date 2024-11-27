import networkx as nx
import random
import sys

from assignment_10_support import read_environment_file
from assignment_10_support import get_start_goal
from assignment_10_support import plot_path


def bresenham_line(x1, y1, x2, y2):
    ''' Bresenham's line algorithm
    Args:
        x1 (int): x coordinate of start point
        y1 (int): y coordinate of start point
        x2 (int): x coordinate of end point
        y2 (int): y coordinate of end point
    Returns:
        points (list): list of points from start to end
    '''
    # Setup initial conditions
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    # Decision variables for determining the next point
    if dx > dy:
        err = dx / 2
        while x != x2:
            points.append((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2
        while y != y2:
            points.append((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    points.append((x, y))  # Add the final point
    return points

def generate_sample_node(env)->tuple:
    ''' Generate a sample node
    Use random.randint to generate the integer coordinates of the node
    Check if node is valid, if not, generate another node
    Args:
        env (list): list of lists representing the grid
    '''
    # <-- complete code here -->
    pass

def find_closest_node(tree, sample_node)->tuple:
    ''' Find the closest node in the graph to the sample node
    Loops through all the vertices in the tree to get the closest node
    Args:
        tree (nx.Graph): graph representing the tree
        sample_node (tuple): sample node
    Returns:
        closest_node (tuple): closest node to the sample node
    '''
    # -- find the closest node in the graph to the sample node
    # <-- complete code here -->
    pass

def steer(env, closest_node, sample_node):
    ''' Steer the closest node towards the sample node
    Generate a line between the closest node and the sample node using the
    function bresenham_line.
    Check if each point in the line is '-', if so, then line is valid
    If the line is valid, return the last point in the line
    Else, return the closest_node
    Args:
        env (list): list of lists representing the grid
        closest_node (tuple): closest node to the sample node
        sample_node (tuple): sample node
    Returns:
        
    '''
    # <-- complete code here -->
    pass

def rrt_algorithm(env, start, end, tree, max_nodes=300):
    ''' RRT Algorithm
    Args:
        env (list): list of lists representing the grid
        start (tuple): start location
        end (tuple): goal location
        tree (nx.Graph): graph representing the tree
        max_nodes (int): maximum number of nodes to generate
    Returns:
        tree (nx.Graph): graph representing the tree
        goal_found (bool): True if goal was found, False otherwise
    '''
    # -- Initialize the tree with the start node
    tree.add_node(start)
    
    # -- Generate nodes untill one is at goalzone or no more nodes can be generated
    goal_found = False
    notAtGoal = True
    # While loop till goal is found or max_nodes is reached
    # while notAtGoal:
        # -- Generate a sample node
        # <-- complete code here -->

        # -- Find the closest node in the graph to the sample node
        # <-- complete code here -->

        # -- Steer the closest node towards the sample node
        # <-- complete code here -->

        # -- Add the new node to the tree
        # <-- complete code here -->
        
        # -- Check if the new node is at the goal
        # <-- complete code here -->
        
        # -- Check if the max number of nodes has been reached
        # <-- complete code here -->

    # <-- uncomment the following line to return the tree and goal_found -->
    # return tree, goal_found
    # <-- Remove the following statement -->
    pass


def main(filename = '../resources/grid_0.txt'):
    ''' Main function for running the RRT algorithm
    '''
    # -- get the filename
    filename = '../resources/grid_6.txt'
    
    # -- read the filename into environment
    grid_env = read_environment_file(filename)
    
    # -- get the start and goal positions
    start, goal = get_start_goal(grid_env)
    
    # -- remove start and goal from the environment
    grid_env[start[0]][start[1]] = '-'
    grid_env[goal[0]][goal[1]] = '-'
    
    # -- initialize the tree 
    tree = nx.Graph()
    
    # -- calculate RRT path using the grid environment
    tree, goal_found = rrt_algorithm(grid_env, start, goal, tree)
    
    # -- get the path from the tree
    path = nx.shortest_path(tree, start, goal)

    # -- display the path
    plot_path(grid_env, path, 'RRT Path')

def rrt_usage():
    print ("-"*30)
    print ("RRT Usage:")
    print ("-"*30)
    print ("python3 rrt_scaffolding.py <environment_filename>")
    print ("-"*30)

if __name__ == '__main__':
    # -- system argument for environment filename
    # -- default is '../resources/grid_0.txt'
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        rrt_usage()