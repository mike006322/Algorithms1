from graphHeap import MikesGraphHeap


def dijkstra(graph, start=1):
    """
    input graph of the form {node1: {node2: distance, node3: distance, ... }, ...}
    output dictionary {node: shortest path from start to node}
    """
    X = {start}  # Vertices passed so far
    A = {start: 0}  # Computed shortest path distances
    V = set(graph.keys())
    M = MikesGraphHeap()  # stores nodes in form node = (label, key)
    # Dijkstra greedy score for nodes with edge from 1 is the values of the edges

    heapFill = V - X - set(graph[1].keys())  # all of the nodes that 1 doesnt have an edge to, to have key of inf in M
    M.heapify([(x, 10**6) for x in heapFill])
    for node in graph[1]:
        M.insert((node, graph[1][node]))

    while X != V:
        # find minimum A[v] + len(v,w) among edges (v,w) for all v in X and w not in X
        # call it (vStar, wStar)
        m = M.extractMin() # gives us (node, key)
        X.add(m[0])
        A[m[0]] = m[1]
        # for each edge (m[0], v) out of m[0], a[m[0]][v] = distance to v
        for v in graph[m[0]]:
            if v in V - X:
                M.heapList[0] = (0, 0)
                vKey = dict(M.heapList)[v]
                M.delete((v, vKey))
                vKey = min(vKey, A[m[0]] + graph[m[0]][v])
                M.insert((v, vKey))
    return A


if __name__ == '__main__':
    graph = {}
    for line in open('dijkstraData.txt', 'r'):
        b = list(line.split())
        graph[int(b[0])] = {}
        for i in b[1:]:  # 'node, distance'
            node, distance = i.split(',')
            graph[int(b[0])][int(node)] = int(distance)
    A = dijkstra(graph)
    print('7 = ', A[7])
    print('37 = ', A[37])
    print('59 = ', A[59])
    print('82 = ', A[82])
    print('99 = ', A[99])
    print('115 = ', A[115])
    print('133 = ', A[133])
    print('165 = ', A[165])
    print('188 = ', A[188])
    print('197 = ', A[197])
