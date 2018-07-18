"""
Kosaraju's two-pass algorithm for computing strongly connected components
First run Depth First Search on graph with edges reversed
Then run Depth First Search on the original graph
"""

import sys
import collections

def order_graph(G, ordering):
    orderedGraph = dict()
    for i in G:
        orderedGraph[ordering[i]] = [ordering[j] for j in G[i]]
    return orderedGraph


def kosaraju(file, n):
    ordering = dict()

    def DFS(Graph, n):
        """
        input is dictionary of adjacency lists and number of nodes
        output is dictionary of connected components while also modifying global 'ordering'
        """
        connected_components = dict()
        time = 0
        nonlocal ordering
        visited = set()
        for i in range(n,0,-1):
            if i in visited:
                continue
            visited.add(i)
            start = i
            if i % 200 == 0:
                print('currently on {}'.format(i))
            stack = collections.deque()
            stack.append(start)
            component = set()
            while stack:
                v = stack.popleft()
                if v not in component:
                    component.add(v)
                    stack.appendleft(v)
                    if v in Graph:
                        for w in Graph[v]:
                            if w not in component and w not in visited:
                                visited.add(w)
                                stack.appendleft(w)
                else:
                    if v not in ordering:
                        ordering[v] = time
                        time += 1
            connected_components[i] = component
        return connected_components

    aReverse = collections.defaultdict(set)
    for line in open(file, 'r'):
        b = list(map(int, line.split())) # list begining with vertex followed by adjacent verticies
        aReverse[b[1]].add(b[0])

    DFS(aReverse, n) # gets ordering
    aReverse = {} # clears aReverse from memory

    a = collections.defaultdict(set)
    for line in open(file, 'r'):
        b = list(map(int, line.split())) # list begining with vertex followed by adjacent verticies
        a[b[0]].add(b[1])

    ordereda = order_graph(a, ordering)
    a = {} # clear a from memory
    return DFS(ordereda, n)

if __name__ == '__main__':
    sys.getrecursionlimit()
    n = 875714 # number of nodes in graph
    segment = kosaraju('SCC.txt', n)
    print(sorted([len(segment[i]) for i in segment]))
