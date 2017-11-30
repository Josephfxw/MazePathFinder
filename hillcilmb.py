
# Hill Climbing Search


class SimpleGraph:
    def __init__(self):
        self.edges = {}
        self.heuristic_for_each_node ={}
    
    def neighbors(self, currentNode): # return the neighbor nodes for current node
        return self.edges[currentNode].keys()

    def cost(self,currentNode, nextNode): # return cost of the edge
        return self.edges[currentNode][nextNode]

    def heuristic(self,nextNode): # return the heuristic cost to goal for the node
   
        return self.heuristic_for_each_node[nextNode]

    def hasChildren(self,nextNode):
        return  bool(self.edges[nextNode])


example_graph = SimpleGraph()
# caculate the length for each edge from the graph or tree and store them here
example_graph.edges = {   # graph maze 

    'A': {'B': 7, 'C' :109} ,  
    'B': {'D': 31, 'E': 8},
    'C': {},
    'D': {},
    'E': {'F': 12, 'G': 24},
    'F': {'H': 46, 'I': 17},
    'G': {},
    'H': {},
    'I': {'J':13,'K':7},
    'J': {},
    'K': {'L':38, 'M':45},
    'L': {},
    'M': {}
}


# caculate the heuristic cost for each node from the graph and store them here
example_graph.heuristic_for_each_node ={     # graph maze 
    
    'A': 50,
    'B': 45,
    'C': 5,
    'D': 40,
    'E': 45,
    'F': 34,
    'G': 39,
    'H': 28,
    'I': 23,
    'J': 14,
    'K': 18,
    'L': 25,
    'M': 0
}




# priority Queue
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):  # priority value smaller mean its node has higher priotiry
        heapq.heappush(self.elements, (priority, item))
    
    def get(self): # Pop and return the smallest item from the heap
        return heapq.heappop(self.elements)[1]



# A* searcj function
def hill_climb_search(graph, start, goal): # here the goal must be 'M', since we already stored the heuristic costs
    frontier = PriorityQueue()
    frontier.put(start, 0) #Form a one-element Priority queue consisting of a zero-length path that contains only the root node.
    came_from = {}         # In order to reconstruct paths we need to store the location of where the nodes came from. for example,{'C': 'A'} means C comes from A
    
    came_from[start] = None
   
    
    while not frontier.empty():
        current = frontier.get()  # get the current node from the priority queue
        frontier.empty()  # clean the other nodes###########################
        if current == goal:
            break

        if graph.hasChildren(current):
          for next in graph.neighbors(current):
            if next not in came_from:
                priority = graph.heuristic(next)  # underestimate part: real cost + heuristic cost for "NEXT" node
                frontier.put(next, priority)  # use priority queue sort the children nodes and put the least cost node in the front
                came_from[next] = current     # track the  path
        elif(current != goal) :
            print "WE are stuck at %s" % current 
            return     
    return came_from  


# construct the minimum cost path from the came_from dic
def reconstruct_path(came_from, start, goal):  # here the goal must be 'M', since we already stored the heuristic costs
    if not came_from:
        return

    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    print path


# here the goal must be 'M', since we already stored the heuristic costs
reconstruct_path(hill_climb_search(example_graph, 'A','M'),'A','M')
