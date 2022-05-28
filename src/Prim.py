import math
from ExtractMinimum import extract_min

class Prim:

    def prim(G, w, r):

        for v in G.vertices:
            v.set_distance(math.inf)
            v.set_parent(None)
            
        r.set_distance(0)
        q = []
        q.append(G.vertices)

        while q:
            u = extract_min(q)
            for v in G.vertices[u].adjacency_list:
                if v in q and w < v.get_distance():
                    v.set_parent(u)
                    v.set_distance(w)

if __name__=='__main__':
    pass