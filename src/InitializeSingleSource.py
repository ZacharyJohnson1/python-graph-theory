import math

class InitializeSingleSource:

    @staticmethod
    def initialize_single_source(G,s):
    
        for v in G.vertices:
            v.distance = math.inf
            v.parent = None
        s.distance = 0