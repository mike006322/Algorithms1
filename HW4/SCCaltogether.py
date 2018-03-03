#computes strongest connected component using DFS first in reverse and then forwards
import sys
import resource
resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
sys.setrecursionlimit(0x100000)
a = {} #adjacency list, keys are verticies, values are list of adjacent verticies
n = 875714

visited = set()
ordering = dict()
segment = dict()
t = 0
s = 0

def DFS(G, i):
    global t
    visited.add(i)
    if s in segment:
        segment[s].append(i)
    else:
        segment[s] = [i]
    for j in G[i]:
        if j not in visited:
            DFS(G, j)
    t += 1
    ordering[i] = t

'''
#non-recursie DFS function that doesn't work correctly
def DFS(G, i):
    stack = [i]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            global t
            t -= 1
            ordering[vertex] = t
            if s in segment:
                segment[s].append(vertex)
            else:
                segment[s] = [vertex]
            stack.extend(set(G[vertex]) - visited)
'''    
    
def DFS_Loop(G):
    for i in range(len(G), 0, -1):
        if i not in visited:
            global s
            s = i
            DFS(G, i)

def order_graph(G, ordering):
    orderedGraph = dict()
    for i in G:
        orderedGraph[ordering[i]] = [ordering[j] for j in G[i]]
    return orderedGraph

  
   
aReverse = {}
for i in range(1, n + 1):
    aReverse[i] = set()
for line in open('SCC.txt', 'r'):
    b = list(map(int, line.split())) #list begining with vertex followed by adjacent verticies
    aReverse[b[1]].add(b[0])
    


t = 0
DFS_Loop(aReverse)
aReverse = {}

for i in range(1, n + 1):
    a[i] = set()
for line in open('SCC.txt', 'r'):
    b = list(map(int, line.split())) #list begining with vertex followed by adjacent verticies
    a[b[0]].add(b[1])
    
    
ordereda = order_graph(a, ordering)
a = {}
visited = set()
segment = dict()
t = 0
s = 0
DFS_Loop(ordereda)
print(sorted([len(segment[i]) for i in segment]))
    
