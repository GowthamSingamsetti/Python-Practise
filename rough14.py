graph = {'A': ['B','C','E'],
         'B':['A','D','E'],
         'C':['A','F','G'],
         'D':['B'],
         'E':['A','B','D'],
         'F':['C'],
         'G':['C']}
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