from Vertex import Vertex
from Graph import Graph

time = 0

def dfs(G):
    
    for v in G.vertices:
        v.set_color('WHITE')
        v.set_parent(None)
    #time = 0
    
    for v in G.vertices:
        if v.get_color() == 'WHITE':
            dfs_visit(G, v)


def dfs_visit(G, u):

    global time
    time += 1
    u.set_distance(time)
    u.set_color('GRAY')

    for v in G.vertices[G.vertices.index(u)].adjacency_list:
        if v.get_color() == 'WHITE':
            v.set_parent(u)
            dfs_visit(G, v)
    u.set_color('BLACK')
    time += 1
    u.set_finish_time(time)
    print(f'{u.get_id()} - distance: {u.get_distance()}, finish: {u.get_finish_time()}')

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
    G.define_edge(v, w)

    dfs(G)