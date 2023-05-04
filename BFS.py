from collections import deque
from math import inf
from Graph_Representation import Matrix_to_list, List_to_matrix

# V + E
def BFS_list(G, s):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    time = [0 for _ in range(len(G))]
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        vertex = queue.popleft()
        for v in G[vertex]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                parent[v] = vertex
                time[v] = time[vertex] + 1

    print("time from ", s, ": ")
    print(time)
    print("parents: ")
    print(parent)
    
# V^2
def BFS_matrix(G, s):
    visited = [False for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    time = [0 for _ in range(len(G))]
    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
        vertex = queue.popleft()
        for v, edge in enumerate(G[vertex]):
            if not visited[v] and edge == 1:
                queue.append(v)
                visited[v] = True
                parent[v] = vertex
                time[v] = time[vertex] + 1

    print("time from ", s, ": ")
    print(time)
    print("parents: ")
    print(parent)


G=[ [1, 2, 8],
    [4, 5, 7],
    [9],
    [0, 10, 11],
    [13],
    [6, 7, 13],
    [],
    [8],
    [9],
    [],
    [9, 11],
    [],
    [0, 3],
    [12]]

BFS_list(G, 0)
H = List_to_matrix(G)
BFS_matrix(H, 0)