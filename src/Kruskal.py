from Vertex import Vertex
from Graph import Graph
from MakeSet import MakeSet
from Union import Union
from FindSet import FindSet
from VertexSet import VertexSet

class Kruskal:

    @staticmethod
    def kruskal(G):

        A = []
        S = VertexSet()
        for v in G.vertices:
            S.add(MakeSet.make_set(v))
            
        edges = G.edges
        edges.sort()
        # for edge in edges:
        #     print(f'{edge.u.id} - {edge.v.id}')
        
        for edge in edges:

            if FindSet.find_set(S, edge.u) != FindSet.find_set(S, edge.v):
                A.append(edge)
                Union.union(edge.u, edge.v, S)

        return A

if __name__=='__main__':

    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    f = Vertex('F')

    G = Graph()

    G.insert_vertex(a)
    G.insert_vertex(b)
    G.insert_vertex(c)
    G.insert_vertex(d)
    G.insert_vertex(e)
    G.insert_vertex(f)

    G.define_edge(a, b, 4)
    G.define_edge(a, f, 5)
    G.define_edge(b, e, 2)
    G.define_edge(b, f, 8)
    G.define_edge(c, e, 7)
    G.define_edge(c, f, 1)
    G.define_edge(d, e, 3)
    G.define_edge(e, f, 6)

    kruskal_solution = Kruskal.kruskal(G)

    for edge in kruskal_solution:
        print(f'{edge.u.id} - {edge.v.id}')
