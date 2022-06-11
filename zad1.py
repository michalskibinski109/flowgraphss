from networkx.drawing.nx_pydot import graphviz_layout
import json
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
    N = []
    e = []
    E = [] #(u,v,weight)
    # 97 - a
    N = [i for i in range(len(C))]
    for i in range(len(C)):
        for j in range(len(C)):
            if C[i][j] != 0:
                E.append((N[i], N[j], '0/'+str(C[i][j]))) 
                e.append((N[i], N[j], C[i][j])) 
    return e, E    

def plot(C):
    e, E = CtoNE(C)
    G = nx.DiGraph()
    G.add_weighted_edges_from(e)
    pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
    G = nx.DiGraph()
    G.add_weighted_edges_from(E)

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, width=3)

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


with open('graph.json', 'r') as f:
    C = json.load(f)
C = C['C']




source = 0  # a
sink = 5    # f
max_flow_value = max_flow(C, source, sink)
print("Edmonds-Karp algorithm")
print("max_flow_value is: ",max_flow_value)


plot(C)