from math import inf
from Graph_Representation import Matrix_to_list, List_to_matrix

def Find(parent, x):
    if parent[x] != x:
        parent[x] = Find(parent, parent[x])
    return parent[x]

def Union(parent, rank, x, y):
    x = Find(parent, x)
    y = Find(parent, y)
    if x == y:
        return
    
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def Kruskal_list(G):
    parent = [_ for _ in range(len(G))]
    rank = [1 for _ in range(len(G))]
    edges = []
    MST = []
    taken = 0

    for v in range(len(G)):
        for u, weight in G[v]:
            edges.append((v, u, weight))  
    edges = sorted(edges, key=lambda item:item[2])

    for edge in edges:
        if taken == len(G) - 1:
            return MST
        x = Find(parent, edge[0])
        y = Find(parent, edge[1])

        if x != y:
            Union(parent, rank, x, y)
            taken += 1
            MST.append(edge)
    print("Something went wrong!")

def Kruskal_matrix(G):
    parent = [_ for _ in range(len(G))]
    rank = [1 for _ in range(len(G))]
    edges = []
    MST = []
    taken = 0

    for u, edge in enumerate(G):
        for v, weight in enumerate(edge):
            if weight != inf and u < v:
                edges.append((u, v, weight))
    edges.sort(key = lambda item:item[2])

    for edge in edges:
        if taken == len(G) - 1:
            return MST
        x = Find(parent, edge[0])
        y = Find(parent, edge[1])

        if x != y:
            Union(parent, rank, x, y)
            taken += 1
            MST.append(edge)
    print("Something went wrong!")


G = [[inf, 5,   inf, 9,   inf, inf, 3,   inf], 
     [5,   inf, 9,   inf, 8,   6,   inf, 7], 
     [inf, 9,   inf, 9,   4,   inf, 5,   3], 
     [9,   inf, 9,   inf, inf, inf, 8,   inf], 
     [inf, 8,   4,   inf, inf, 2,   1,   inf], 
     [inf, 6,   inf, inf, 2,   inf, 6,   inf], 
     [3,   inf, 5,   8,   1,   6,   inf, 9], 
     [inf, 7,   3,   inf, inf, inf, 9,   inf]]
MST = Kruskal_matrix(G)
print(MST)
H = Matrix_to_list(G)
MST = Kruskal_list(H)
print(MST)