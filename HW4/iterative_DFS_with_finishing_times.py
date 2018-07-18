"""
Iterative DFS with finish times
Graph is dictionary with adjacency lists
n is the number of nodes, which are labeled 1 to n
"""
ordering = dict()
def DFS(Graph, n):
    """
    input is dictionary of adjacency lists and number of nodes
    output is dictionary of connected components while also modifying global 'ordering'
    """
    connected_components = dict()
    time = 0
    global ordering
    for i in range(n,0,-1):
        start = i
        stack = [start]
        connected_components[i] = []
        while stack:
            v = stack.pop(0)
            if v not in connected_components[i]:
                connected_components[i].append(v)
                stack = [v] + stack
                if v in Graph:
                    for w in Graph[v]:
                        if w not in connected_components[i]:
                            stack = [w] + stack
            else:
                if v not in ordering:
                    ordering[v] = time
                    time += 1
    return connected_components
