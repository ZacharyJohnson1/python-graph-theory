from Graph import Graph
import math

class Vertex:

    def __init__(self, id, color='WHITE', distance=math.inf, time=0, parent=None):

        self.id = id
        self.color = color
        self.distance = distance
        self.time = time
        self.parent = parent
        self.adjacency_list = []


    def __ge__(self, v):
        
        return True if self.distance > v.distance else False


    def __lt__(self, v):

        return True if self.distance < v.distance else False


    def __eq__(self, v):
        
        return True if self.id == v.id else False


def dfs(G):
    
    for v in G.vertices:
        v.color = 'WHITE'
        v.parent = None
    time = 0
    
    for v in G.vertices:
        if v.color == 'WHITE':
            dfs_visit(G, v)


def dfs_visit(G, u):
    
    time += 1
    u.distance = time
    u.color = 'GRAY'

    for v in G.vertices[u].adjacency_list:
        if v.color == 'WHITE':
            v.parent = u
            dfs_visit(G, v)
    u.color = 'BLACK'
    time += 1
    u.finish = time