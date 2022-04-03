class Edge:

    def __init__(self, u, v, w):

        self.u = u
        self.v = v
        self.w = w


    def __eq__(self, edge):

        if self.u.id == edge.u.id and self.v.id == edge.v.id:
            return True
        return False

