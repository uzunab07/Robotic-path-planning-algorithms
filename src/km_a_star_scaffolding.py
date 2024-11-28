import heapq
import sys
from assignment_9_support import *
import os

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar_search(graph, start, goal):
    # # -- print the graph
    # print ("Graph: ", graph)
    # sys.exit()
    # initial set of discovered nodes that can be expanded.
    # Frontiercos
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
    gScore = {}
    # <-- Complete code here -->
    for node in graph:
        gScore[node] = float('inf')
    gScore[start] = 0

    # -- initialize fScore, where fScore[n] = gScore[n] + h(n)
    # -- fScore is a dictionary where the key is the node and the value is the
    #    cost of the cheapest path from start to vertex n currently known
    # -- initialize the fScore of each node to infinity
    # -- initialize the fScore of the start node to h(start)
    fScore = {}
    
    # <-- Complete code here -->
    fScore = {}
    for node in graph:
        fScore[node] = float('inf')
    fScore[start] = heuristic(start,goal) 
    # -- initialize the path_found flag to False
    
    # <-- Complete code here -->
    path_found = False
    # -- Loop till all open_set is empty or path is found
    while not open_set or not path_found:
        current_node = heapq.heappop(open_set)[1]
        
        if current_node == goal:
            path_found = True
            break
        
        for neighbor, cost in graph[current_node]:
            tentative_gScore = gScore[current_node] + cost
            if tentative_gScore < gScore[neighbor]:
                # Update gScore and fScore
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, goal)
                # Add to priority queue
                heapq.heappush(open_set, (fScore[neighbor], neighbor))
                # Update the path
                came_from[neighbor] = current_node 
    # Reconstruct the path from start to goal
    # if path is not found, return an empty list
    # -- initialize the path variable to an empty list
    if path_found:
        path = []
        # <-- Complete code here -->
        current = goal
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
    else:
        path = []

    # -- return the path
    return path

def main(filename = os.getcwd()+'/resources/grid_0.txt'):
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
    absolute_path = os.getcwd()
    filename = '/resources/grid_6.txt'
    filename=absolute_path + filename
    main(filename)