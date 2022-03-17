import math

class Vertex:

    def __init__(self, id, color='WHITE', distance=math.inf, parent=None):

        self.id = id
        self.color = color
        self.distance = distance
        self.parent = parent
        self.adjacency_list = []

