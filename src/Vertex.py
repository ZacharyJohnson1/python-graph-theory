import math

class Vertex:

    def __init__(self, id, color='WHITE', distance=math.inf, parent=None):

        self.id = id
        self.color = color
        self.distance = distance
        self.parent = parent
        self.adjacency_list = []


    def __ge__(self, v):
        
        return True if self.distance > v.distance else False


    def __lt__(self, v):

        return True if self.distance < v.distance else False


    def __eq__(self, v):
        
        return True if self.id == v.id else False

