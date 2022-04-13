from InitializeSingleSource import initialize_single_source
from Relax import relax
from Graph import Graph

class BellmanFord:

    def BellmanFord(G, w, s):

        initialize_single_source(G,s)
        
        for _ in range(1, len(G.vertices) - 1):
            for e in G.edges:
                relax(e.u, e.v, w)
        
        for e in G.edges:
            if e.v.distance > e.u.distance + w:
                return False
        return True