class VertexSet:

    def __init__(self, s=[]):
        
        self.s = s
    

    def add(self, e):
        if e not in self.s:
            self.s.append(e)


    def remove(self, e):

        if e in self.s:
            self.s.remove(e)
