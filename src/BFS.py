from Vertex import Vertex
from Graph import Graph
import math

def bfs(G, v):
    
    for u in G.vertices:
        if u is not v:
            u.set_color('WHITE')
            u.set_distance(math.inf)
            u.set_parent(None)
    
    v.set_color('GRAY')
    v.set_distance(0)
    v.set_parent(None)

    q = []
    q.append(v)

    while len(q) != 0:

        u = q.pop(0)
        index = G.vertices.index(u)
        for vertex in G.vertices[index].adjacency_list:
            if vertex.get_color() == 'WHITE':
                vertex.set_color('GRAY')
                vertex.set_distance(u.get_distance() + 1)
                vertex.set_parent(u)
                q.append(vertex)
        u.set_color('BLACK')
        print(f'id: {u.get_id()}, distance: {u.get_distance()}')


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
    #G.define_edge(w, x)
    G.define_edge(z, w)
    G.define_edge(x, y)
    G.define_edge(y, z)
    G.define_edge(u, x)
    G.define_edge(v, w)
    # for v in G.vertices: print(v.id)
    # for e in G.edges:
    #     for v in e:
    #         print(v.id)
    #bfs(G, u)
    bfs(G, z)