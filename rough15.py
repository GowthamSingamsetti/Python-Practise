graph = {'A': ['B','D','E'],
         'B':['A','E','E'],
         'C':['B','E','F','G'],
         'D':['A','E'],
         'E':['A','B','C','D','F'],
         'F':['C','E','G'],
         'G':['C','F']}
# visit all the nodes of the graph using BFS
def bfs_connected_component(graph,start):

    explored = []
    queue = [start]
    while queue:
        node = queue.pop(0) # pop shallowest node
        if node not in explored:
            explored.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
    return explored



print(bfs_connected_component(graph,'A'))