import heapq
import sys
from assignment_10_support import *

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar_search(graph, start, goal):
    # # -- print the graph
    # print ("Graph: ", graph)
    # sys.exit()
    # initial set of discovered nodes that can be expanded.
    open_set = []
    # Initially on the start node is known
    heapq.heappush(open_set, (0, start))

    # came from is the node immediately preceding it on the cheapest path from
    # the start
    came_from = {} 
    cost_so_far = {start: 0}

    # -- initialize gScore, where gScore[n] is the cost of the cheapest path
    #    from start to vertex n currently known
    # -- gScore is a dictionary where the key is the node and the value is the
    #    cost of the cheapest path from start to vertex n currently known
    # -- initialize the cost of each node to infinity
    # -- initialize the cost of the start node to 0
    
    # <-- Complete code here -->

    # -- initialize fScore, where fScore[n] = gScore[n] + h(n)
    # -- fScore is a dictionary where the key is the node and the value is the
    #    cost of the cheapest path from start to vertex n currently known
    # -- initialize the fScore of each node to infinity
    # -- initialize the fScore of the start node to h(start)
    
    # <-- Complete code here -->

    # -- initialize the path_found flag to False
    
    # <-- Complete code here -->

    # -- Loop till all open_set is empty or path is found

    # Reconstruct the path from start to goal
    # if path is not found, return an empty list
    # -- initialize the path variable to an empty list
    path = []
    # <-- Complete code here -->

    # -- return the path
    return path

def main(filename = '../resources/grid_0.txt'):
    # -- read the filename
    grid_env = read_environment_file(filename)
    # -- convert grid to graph
    graph = grid_to_graph_eight_neighbor(grid_env)
    # -- plot environment
    # plot_environment(grid_env, 'Grid Environment')
    # -- run astar search
    start, goal = get_start_goal(grid_env)
    path = astar_search(graph, start, goal)
    # -- plot the path
    plot_path(grid_env, path, 'A* Search')
    
if __name__ == '__main__':
    filename = '../resources/grid_5.txt'
    main(filename)