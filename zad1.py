import networkx as nx
import matplotlib.pyplot as plt
#Edmonds-Karp Algorithm
f = lambda x: chr(x + 97)
def max_flow(C, s, t):
        n = len(C) # C is the capacity matrix
        F = [[0] * n for i in range(n)]
        path = bfs(C, F, s, t)
      #  print path
        while path != None:
            flow = min(C[u][v] - F[u][v] for u,v in path)
            for u,v in path:
                F[u][v] += flow
                F[v][u] -= flow
            path = bfs(C, F, s, t)
        return sum(F[s][i] for i in range(n))

#find path by using BFS
def bfs(C, F, s, t):
        queue = [s]
        paths = {s:[]}
        if s == t:
            return paths[s]
        while queue: 
            u = queue.pop(0)
            for v in range(len(C)):
                    if(C[u][v]-F[u][v]>0) and v not in paths:
                        paths[v] = paths[u]+[(u,v)]
                        print(paths)
                        if v == t:
                            return paths[v]
                        queue.append(v)
        return None
    
def CtoNE(C):
    """capacity matrix to Edges and Nodes"""
    N, E = [],[]
    # 97 - a
    N = [i for i in range(len(C))]
    for i in range(len(C)):
        for j in range(len(C)):
            if C[i][j] != 0:
                E.append((N[i], N[j])) 
    return N, E    
# make a capacity graph
# nod  s   o   p   q   r   t
C = [[ 0, 3, 3, 0, 0, 0 ],  # s
     [ 0, 0, 2, 3, 0, 0 ],  # o
     [ 0, 0, 0, 0, 2, 0 ],  # p
     [ 0, 0, 0, 0, 4, 2 ],  # q
     [ 0, 0, 2, 0, 0, 2 ],  # r
     [ 0, 0, 0, 0, 0, 0 ]]  # t
N, E = CtoNE(C)
G = nx.Graph(E)
nx.draw(G, with_labels=True)


source = 0  # a
sink = 5    # f
max_flow_value = max_flow(C, source, sink)
print("Edmonds-Karp algorithm")
print("max_flow_value is: ",max_flow_value)


plt.show()