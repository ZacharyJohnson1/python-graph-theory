from Vertex import Vertex
from Edge import Edge
from Graph import Graph
import math

def bfs(G, v):
    
    for u in G.vertices:
        if u is not v:
            u.color = 'WHITE'
            u.distance = math.inf
            u.parent = None
    
    v.color = 'GRAY'
    v.distance = 0
    v.parent = None

    q = []
    q.append(v)

    while len(q) != 0:

        u = q.pop(0)
        index = G.vertices.index(u)
        for vertex in G.vertices[index].adjacency_list:
            if vertex.color == 'WHITE':
                vertex.color = 'GRAY'
                vertex.distance = u.distance + 1
                vertex.parent = u
                print(f'id: {vertex.id}, distance: {vertex.distance}, parent: {vertex.parent.id}')
                q.append(vertex)
        u.color = 'BLACK'


if __name__ == '__main__':
    
    u = Vertex('U')
    v = Vertex('V')
    w = Vertex('W')
    x = Vertex('X')
    y = Vertex('Y')
    z = Vertex('Z')

    G = Graph()

    G.insert_vertex(u)
    G.insert_vertex(v)
    G.insert_vertex(w)
    G.insert_vertex(x)
    G.insert_vertex(y)
    G.insert_vertex(z)

    G.define_edge(u, v)
    G.define_edge(w, x)
    G.define_edge(x, y)
    G.define_edge(y, z)
    # for v in G.vertices: print(v.id)
    # for e in G.edges:
    #     for v in e:
    #         print(v.id)
    #bfs(G, u)
    bfs(G, z)