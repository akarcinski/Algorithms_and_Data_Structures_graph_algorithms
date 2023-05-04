from math import inf
from queue import PriorityQueue
from Graph_Representation import Matrix_to_list, List_to_matrix

# O( ( E + V )logV )
def Dijkstra_list(G, s):
    distance = [ inf for _ in range(len(G)) ]
    parent = [None for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    distance[s] = 0
    PQ = PriorityQueue()
    PQ.put((0, s))

    while not PQ.empty():
        current_distance, vertex = PQ.get()
        visited[vertex] = True
        if current_distance > distance[vertex]:
            continue

        for neighbour, weight in G[vertex]:
            dist = current_distance + weight

            if dist < distance[neighbour] and not visited[neighbour]:
                distance[neighbour] = dist
                parent[neighbour] = vertex
                PQ.put((dist, neighbour))

    print("distance from ", s, ": ")
    print(distance)
    print("parents: ")
    print(parent)
    
# O( V^2 )
def Dijkstra_matrix(G, s):
    distance = [ inf for _ in range(len(G)) ]
    visited = [ False for _ in range(len(G)) ]
    parent = [None for _ in range(len(G))]
    distance[s] = 0

    while True:
        shortest_distance = inf
        shortest_index = -1
        for i in range(len(G)):
            if distance[i] < shortest_distance and not visited[i]:
                shortest_distance = distance[i]
                shortest_index = i
        
        if shortest_index == -1:
            print("distance from ", s, ": ")
            print(distance)
            print("parents: ")
            print(parent)
            return 0
        
        for i in range(len(G[shortest_index])):
            if G[shortest_index][i] != 0 and (distance[i] > (distance[shortest_index] + G[shortest_index][i])):
                distance[i] = distance[shortest_index] + G[shortest_index][i]
                parent[i] = shortest_index
        
        visited[shortest_index] = True


G = [ [inf, 3, inf, inf, 3, inf ],
  [inf, inf, 1, inf, inf, inf],
  [inf, inf, inf, 3, inf, 1],
  [inf, 3, inf, inf, inf, inf],
  [inf, inf, inf, inf, inf, 2],
  [6, inf, inf, 1, inf, inf] ]



start = 0
print("MATRIX")

Dijkstra_matrix(G, start)

H = Matrix_to_list(G)

print("LINKED LIST")

Dijkstra_list(H, start)