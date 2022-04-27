import math

class InitializeSingleSource:

    @staticmethod
    def initialize_single_source(G,s):
    
        for v in G.vertices:
            v.set_distance(math.inf)
            v.set_parent(None)
        s.set_distance(0)