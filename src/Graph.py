from Edge import Edge

class Graph:

    def __init__(self):

        self.vertices = []
        self.edges = []


    def insert_vertex(self, vertex):
        
        for v in self.vertices:
            if v.id == vertex.id:
                return
        self.vertices.append(vertex)
            

    def define_edge(self, vertex_one, vertex_two, weight=0):
        
        edge = Edge(vertex_one, vertex_two, weight)
        if edge not in self.edges:
            vertex_one.adjacency_list.append(vertex_two)
            vertex_two.adjacency_list.append(vertex_one)
            self.edges.append(edge)

        else:
            self.edges[self.edges.index(edge)].w = weight
    

    def add_edge(self, edge):

        if edge not in self.edges:
            edge.u.adjacency_list.append(edge.v)
            edge.v.adjacency_list.append(edge.u)
            self.edges.append(edge)
        else:
            self.edges[self.edges.index(edge)].w = edge.weight

