#Use Karger's algorithm to find the minimum cut of a graph

a = {} #adjacency list, keys are verticies, values are list of adjacent verticies

for line in open('kargerMinCut.txt', 'r'):
    b = map(int, line.split()) #list begining with vertex followed by adjacent verticies
    a[b[0]] = [x for x in b[1:]]

#Step 1: make list of edges
e = [] #list of edges listed twice
for vertex in a:
    for adj in a[vertex]:
        edge = (vertex, adj)
        e.append(edge)
edges = [] #list of edges
for i in e:
    if (i[1], i[0]) not in edges:
        edges.append(i)

#Step 2: pick random edge
import random
def random_edge(edges):
    return random.sample(edges, 1)

#merge two verticies
def merge(graph, ed): 
    #graph is a dicitonary with vertex keys and adjacency list values, 
    #edges is set of edge tuples 
    r = random_edge(ed)[0]
    
#    graph[r[0]] = graph[r[0]] + graph[r[1]]
    graph.pop(r[1])
#    if r[0] in graph[r[0]]:
#        graph[r[0]] = graph[r[0]].remove(r[0])
#    edges.remove(r) #delete circular edges
#    for i in graph:
#        for j in graph[i]:
#            if j == r[1]:
#                j = r[0]
    edges2 = ed
    for i in ed:
        if i[0] == r[1]:
            if r[0] != i[1]: #don't add loop edges
                edges2.append((r[0], i[1]))
            edges2.remove(i)
            print(len(edges2))
        if i[1] == r[1]:
            if r[1] != i[0]: #don't add loop edges
                edges2.append((i[0], r[1]))
            edges2.remove(i)
            print(len(edges2))
    
          
    if len(graph) > 2:
        merge(graph, edges2)
    

merge(a, edges)

