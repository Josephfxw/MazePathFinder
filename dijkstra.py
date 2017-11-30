class SimpleGraph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, currentNode):
        return self.edges[currentNode].keys()

    def cost(self,currentNode, nextNode):
        return self.edges[currentNode][nextNode]

example_graph = SimpleGraph()
example_graph.edges = {  # graph2
    
    
    'A': {'B': 7,'C':4, 'D': 6, 'E': 1},
    'B': {},
    'C': {'B': 2, 'D': 5},
    'D': {'B':3},   
    'E': {'D': 1},
    
}






import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1] #Pop and return the smallest item from the heap




def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)  #Form a one-element Priority queue consisting of a zero-length path that contains only the root node.
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):

            new_cost = cost_so_far[current] + graph.cost(current, next)

            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from

# construct the minimum cost path from the came_from dic
def reconstruct_path(came_from, start, goal):  # here the goal must be 'M', since we already stored the heuristic costs
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    print path


# here the goal must be 'M', since we already stored the heuristic costs
reconstruct_path(dijkstra_search(example_graph, 'A','B'),'A','B')


