import math

class Vertex:

    def __init__(self, id, color='WHITE', distance=math.inf, discovery_time=0, finish_time=0, parent=None):

        self.id = id
        self.color = color
        self.distance = distance
        self.discovery_time = discovery_time
        self.finish_time = finish_time
        self.parent = parent
        self.adjacency_list = []


    def __ge__(self, v):
        
        return True if self.distance > v.distance else False


    def __lt__(self, v):

        return True if self.distance < v.distance else False


    def __eq__(self, v):
        
        if v == None: return False
        return True if self.id == v.id else False

    
    def get_id(self):

        return self.id

    
    def set_id(self, id):

        self.id = id


    def get_color(self):

        return self.color


    def set_color(self, color):

        self.color = color

    
    def get_distance(self):

        return self.distance

    
    def set_distance(self, distance):

        self.distance = distance

    
    def get_discovery_time(self):

        return self.discovery_time

    
    def set_discovery_time(self, discovery_time):

        self.discovery_time = discovery_time

    
    def get_finish_time(self):

        return self.finish_time

    
    def set_finish_time(self, finish_time):

        self.finish_time = finish_time

    
    def get_parent(self):

        return self.parent

    
    def set_parent(self, parent):

        self.parent = parent
    

    def set_adjacency_list(self, vertex):

        if vertex not in self.adjacency_list:
            self.adjacency_list.append(vertex)

