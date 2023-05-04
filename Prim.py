from math import inf
from queue import PriorityQueue
from Graph_Representation import Matrix_to_list, List_to_matrix

def Prim_matrix(G):
    parent = [None for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    visited[0] = True
    MST = []
    taken = 0
    while taken < len(G)-1:
        minimum = inf
        for i in range(len(G)):
            if visited[i]:
                for j in range(len(G)):
                    if not visited[j]:
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
    


G = [[inf, 5,   inf, 9,   inf, inf, 3,   inf], 
     [5,   inf, 9,   inf, 8,   6,   inf, 7], 
     [inf, 9,   inf, 9,   4,   inf, 5,   3], 
     [9,   inf, 9,   inf, inf, inf, 8,   inf], 
     [inf, 8,   4,   inf, inf, 2,   1,   inf], 
     [inf, 6,   inf, inf, 2,   inf, 6,   inf], 
     [3,   inf, 5,   8,   1,   6,   inf, 9], 
     [inf, 7,   3,   inf, inf, inf, 9,   inf]]
H = Matrix_to_list(G)

MST = Prim_matrix(G)
print(MST)