from collections import deque
from math import inf
from Graph_Representation import Matrix_to_list, List_to_matrix

def Topological_sort_matrix(G):
    visited = [False for _ in range(len(G))]
    stack = deque()

    def Topological_sort_matrix_util(G, visited, stack, u):
        visited[u] = True

        for v in range(len(G)):
            if not visited[v] and G[u][v] == 1:
                Topological_sort_matrix_util(G, visited, stack, v)
        stack.append(u)

    for i in range(len(G)):
        if not visited[i]:
            Topological_sort_matrix_util(G, visited, stack, i)
    print("TOPOLOGICAL MATRIX SORT")
    print(stack)

def Topological_sort_list(G):
    visited = [False for _ in range(len(G))]
    stack = deque()

    def Topological_sort_list_util(G, visited, stack, u):
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                Topological_sort_list_util(G, visited, stack, v)
        stack.append(u)
    
    for i in range(len(G)):
        if not visited[i]:
            Topological_sort_list_util(G, visited, stack, i)
    print("TOPOLOGICAL LIST SORT")
    print(stack)

G = [[],
    [],
    [3],
    [1],
    [0, 1],
    [0, 2]]
Topological_sort_list(G)
H = List_to_matrix(G)
Topological_sort_matrix(H)