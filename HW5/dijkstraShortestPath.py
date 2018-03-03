from numpy import inf
from graphHeap import MikesGraphHeap

a ={}

for line in open('dijkstraData.txt', 'r'):
    b = list(line.split())
    a[int(b[0])] = {}
    for i in b[1:]: #'node, distance'
        node, distance = i.split(',')
        a[int(b[0])][int(node)] = int(distance)
    
# a is graph of the form {node1: {node2: distance, node3: distance, ... }, ...}

X = {1} # Verticies passed so far
A = {1:0} # Computed shortest path distances
V = set(a.keys())
M = MikesGraphHeap() # stores nodes in form node = (label, key)
# Dijkstra greedy score for nodes with edge from 1 is the values of the edges

heapFill = V - X - set(a[1].keys()) #all of the nodes that 1 doesnt have an edge to, to have key of inf in M
M.heapify([(x, inf) for x in heapFill])
for node in a[1]: 
    M.insert((node, a[1][node]))

while X != V:
    # find minimum A[v] + len(v,w) among edges (v,w) for all v in X and w not in X
    # call it (vStar, wStar)
    m = M.extractMin() # gives us (node, key)
    X.add(m[0])
    A[m[0]] = m[1]
    #for each edge (m[0], v) out of m[0], a[m[0]][v] = distance to v
    for v in a[m[0]]:
        if v in V - X:
            M.heapList[0] = (0,0)
            vKey = dict(M.heapList)[v]
            M.delete((v,vKey))
            vKey = min(vKey, A[m[0]] + a[m[0]][v])
            M.insert((v, vKey))
        
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
    