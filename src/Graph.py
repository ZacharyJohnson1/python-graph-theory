from Edge import Edge

class Graph:

    def __init__(self, vertices=[], edges=[]):

        self.vertices = vertices
        self.edges = edges


    def insert_vertex(self, vertex):
        
        for v in self.vertices:
            if v.get_id() == vertex.get_id():
                v = vertex
                return
        self.vertices.append(vertex)

    
    def get_vertex(self, id):

      for v in self.vertices:
        if v.get_id() == id:
          return v
      return None
            

    def define_edge(self, vertex_one, vertex_two, weight=0):
        
        edge = Edge(vertex_one, vertex_two, weight)
        if edge not in self.edges:
            edge.u.set_adjacency_list(edge.v)
            edge.v.set_adjacency_list(edge.u)
            self.insert_vertex(edge.u)
            self.insert_vertex(edge.v)
            self.edges.append(edge)

        else:
            self.edges[self.edges.index(edge)].w = weight
    

    def add_edge(self, edge):

        if edge not in self.edges:
            edge.u.set_adjacency_list(edge.v)
            edge.v.set_adjacency_list(edge.u)
            self.insert_vertex(edge.u)
            self.insert_vertex(edge.v)
            self.edges.append(edge)
        else:
            self.edges[self.edges.index(edge)].w = edge.weight

