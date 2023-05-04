from math import inf
from copy import deepcopy
from Graph_Representation import Matrix_to_list, List_to_matrix

def Floyd_warshall(G):
#   distance = list(map(lambda i: list(map(lambda j: j, i)), G))
    distance = deepcopy(G)
    parent = [ [ __ for _ in range(len(G))] for __ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if distance[i][j] == inf or distance[i][j] == 0:
                parent[i][j] = None

    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    parent[i][j] = parent[k][j]

    for i in range(len(G)):
        if distance[i][i] < 0:
            print("negative weight cycle")
            return 
            
    print("distance: ")
    print(distance)
    print("parents: ")
    print(parent)

    return parent

def Path(parent, result, v, u):
    if parent[v][u] == None:
        print("there is no way from ",v," to ",u)
        return
    if v == u:
        result.append(u)
        return
    Path(parent, result, v, parent[v][u])
    result.append(u)

G = [ [0, 5, 4, 8, inf],
    [-4, 0, -2, inf, 5],
    [inf, inf, 0, 5, 2],
    [-1, 2, inf, 0, -1],
    [inf, inf, 4, 2, 0] ]

parent = Floyd_warshall(G)
result = []
Path(parent, result, 0, 0)
print(result)