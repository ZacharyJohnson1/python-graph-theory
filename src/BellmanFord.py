from InitializeSingleSource import initialize_single_source
from Relax import relax
from Graph import Graph

class BellmanFord:

    def BellmanFord(G, w, s):

        initialize_single_source(G,s)
        
        for _ in range(0, len(G.vertices) - 1):
            for edge in G.edges:
                relax(edge.u, edge.v, w(edge))
        
        for edge in G.edges:
            if edge.v.get_distance() > edge.u.get_distance() + w(edge):
                return False
        return True
