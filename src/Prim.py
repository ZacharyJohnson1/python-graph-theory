import math
from ExtractMinimum import extract_min

class Prim:

    def prim(G, w, r):

        for v in G.vertices:
            v.key = math.inf
            v.parent = None
            
        r.distance = 0
        q = []
        q.append(G.vertices)

        while q:
            u = extract_min(q)
            for v in G.vertices[u].adjacency_list:
                if v in q and w < v.distance:
                    v.parent = u
                    v.distance = w