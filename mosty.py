from math import inf
from Graph_Representation import Matrix_to_list, List_to_matrix

Time = 0
def Bridges_util(G, visited, parent, time, low, v):
    global Time
    visited[v] = True
    time[v] = Time
    low[v] = Time
    Time += 1

    for u in G[v]:
        if not visited[u]:
            parent[u] = v

            Bridges_util(G, visited, parent, time, low, u)
            low[v] = min(low[u], low[v])

        elif u != parent[v]:
            low[v] = min(low[v], time[u])


def Bridges_list(G):
    visited = [False for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    time = [inf for _ in range(len(G))]
    low = [inf for _ in range(len(G))]

    for i in range(len(G)):
        if not visited[i]:
            Bridges_util(G, visited, parent, time, low, i)

    for i in range(len(G)):
        if parent[i] != None and time[i] == low[i]:
            print(i, " ", parent[i])

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

Bridges_list(G)