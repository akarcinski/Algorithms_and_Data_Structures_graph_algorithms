from collections import deque
from math import inf
from copy import deepcopy
from Graph_Representation import Matrix_to_list, List_to_matrix

def Euler_cycle_matrix(G):
    def Is_eulerian(G):
        for i in range(len(G)):
            degree = 0
            for j in range(len(G)):
                if G[i][j] == 1:
                    degree += 1
            if degree % 2 == 1:
                return False
        return True
    
    if not Is_eulerian(G):
        print("Graph isn't Eulerian")
        return

    H = deepcopy(G)

    
    def Euler_cycle_matrix_util(u):
        nonlocal H
        print(u)
        for v in range(len(H)):
            if H[u][v] == 1:
                H[u][v] = 0
                H[v][u] = 0
                Euler_cycle_matrix_util(v)

    Euler_cycle_matrix_util(0)

def Euler_cycle_list(G):
    def Is_eulerian(G):
        for i in range(len(G)):           
            if len(G[i]) % 2 == 1:
                return False
        return True
    
    if not Is_eulerian(G):
        print("Graph isn't Eulerian")
        return

G = [[1, 2, 3, 4],
    [0, 2],
    [0, 1],
    [0, 4],
    [0, 3]]
H = List_to_matrix(G,False,True)
Euler_cycle_matrix(H)