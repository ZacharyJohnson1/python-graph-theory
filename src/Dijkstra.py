from InitializeSingleSource import initialize_single_source
from ExtractMinimum import extract_min
from Relax import relax

class Dijkstra:

    def Dijkstra( G, w, s):

        initialize_single_source(G, s)
        S = []
        q = []
        q.append(G.vertices)
        
        while q:
            u = extract_min(q)
            S.append(u)
            for v in G.vertices[u].adjacency_list:
                relax(u, v, w)
        return S