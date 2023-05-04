from math import inf
from Graph_Representation import Matrix_to_list, List_to_matrix

Time = 0
def AP_util(G, visited, parent, time, low, AP, u):
    global Time
    children = 0
    visited[u] = True
    time[u] = Time
    low[u] = Time
    Time += 1

    for v in G[u]:
        if not visited[v]:
            parent[v] = u
            children += 1
            AP_util(G, visited, parent, time, low, AP, v)

            low[u] = min( low[u], low[v] )

            if parent[u] is None and children > 1: # root of DFS tree
                AP.append(u)
            if parent[u] is not None and low[v] >= time[u]:
                AP.append(u)
        elif v != parent[u]:
            low[u] = min( low[u], time[v] )

def Articulation_points(G):
    visited = [False for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    time = [inf for _ in range(len(G))]
    low = [inf for _ in range(len(G))]
    AP = []

    for i in range(len(G)):
        if not visited[i]:
            AP_util(G, visited, parent, time, low, AP, i)
    print(AP)

G = [[1, 2],
    [0, 2],
    [0, 1, 3],
    [2, 4, 5, 9],
    [3, 6],
    [3, 6],
    [4, 5, 7, 8],
    [6],
    [6, 9],
    [3, 8]]
Articulation_points(G)