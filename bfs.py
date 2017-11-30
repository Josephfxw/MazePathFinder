class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]

example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B','C'],
    'B': [ 'D','E'],
    'C': [],
    'D': [],
    'E': ['F','G'],
    'F': ['H','I'],
    'G': [],
    'H': [],
    'I': ['J','K'],
    'J': [],
    'K': ['L','M'],
    'L': []
}


import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()




#from implementation import *

def breadth_first_search_1(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    
    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        if current == goal:
            break
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

breadth_first_search_1(example_graph, 'A','M')