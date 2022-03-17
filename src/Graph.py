class Graph:

    def __init__(self):

        self.vertices = []
        self.edges = [[]]


    def insert_vertex(self, vertex):
        
        for v in self.vertices:
            if v.id == vertex.id:
                return
        self.vertices.append(vertex)
            

    def define_edge(self, vertex_one, vertex_two):
        
        edge = [vertex_one, vertex_two]
        if edge not in self.edges:
            self.edges.append(edge)
            vertex_one.adjacency_list.append(vertex_two)
            vertex_two.adjacency_list.append(vertex_one)
    
