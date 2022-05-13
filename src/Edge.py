class Edge:

    def __init__(self, u, v, w):

        self.u = u
        self.v = v
        self.w = w


    def __eq__(self, edge):

        if self.u.id == edge.u.id and self.v.id == edge.v.id:
            return True
        return False


    def __ge__(self, v):
        
        return True if self.w > v.w else False


    def __lt__(self, v):

        return True if self.w < v.w else False


    @staticmethod
    def weight(edge):

      return edge.w
      