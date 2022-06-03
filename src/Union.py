from VertexSet import VertexSet

class Union:

    @staticmethod
    def union(u, v, s):

        s.remove([u])
        s.remove([v])
        s.add([u, v])
        return s
        