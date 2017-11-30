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



class Stack:
     def __init__(self):
         self.container = []  # You don't want to assign [] to self - when you do that, you're just assigning to a new local variable called `self`.  You want your stack to *have* a list, not *be* a list.

     def empty(self):
         return self.size() == 0   # While there's nothing wrong with self.container == [], there is a builtin function for that purpose, so we may as well use it.  And while we're at it, it's often nice to use your own internal functions, so behavior is more consistent.

     def push(self, item):
         self.container.append(item)  # appending to the *container*, not the instance itself.

     def pop(self):
         return self.container.pop()  # pop from the container, this was fixed from the old version which was wrong

     def size(self):
         return len(self.container)  # length of the container




def deepth_first_search(graph, start, goal):
    frontier = Stack()
    frontier.push(start)
    visited = {}
    visited[start] = True
    
    while not frontier.empty():
        current = frontier.pop()
        print("Visiting %r" % current)
        if current == goal:
            break
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.push(next)
                visited[next] = True

deepth_first_search(example_graph, 'A','M')
