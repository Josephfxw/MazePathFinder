
# Branch and Bound Search ########


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



example_graph = SimpleGraph()
# caculate the length for each edge from the graph or tree and store them here
example_graph.edges = {   # graph maze 

    'A': {'B': 7, 'C' :109} ,  
    'B': {'A': 7, 'D': 31, 'E': 8},
    'C': {'A': 109},
    'D': {'B': 31},
    'E': {'F': 12, 'G': 24},
    'F': {'H': 46, 'I': 17},
    'G': {'E': 24},
    'H': {'F':46},
    'I': {'J':13,'K':7},
    'J': {'I':13},
    'K': {'I':7,'L':38, 'M':45},
    'L': {'K':38},
    'M': {'K':45}
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


from string import digits
# A* searcj function
def branch_bound_search(graph, start, goal): # here the goal must be 'M', since we already stored the heuristic costs
    frontier = PriorityQueue()
    frontier.put(start, 0) #Form a one-element Priority queue consisting of a zero-length path that contains only the root node.
    came_from = {}         # In order to reconstruct paths we need to store the location of where the nodes came from. for example,{'C': 'A'} means C comes from A
    cost_so_far = {}       # cumulate the cost = real path cost + heuristic cost for current node so far 
    came_from[start] = None
    cost_so_far[start] = 0
    
    num =0
    while not frontier.empty():
        num = num +1
        current = frontier.get()  # get the current node from the priority queue
           
      

        if goal not in current: # currenct is not 'M' or 'M2'
          current = ''.join([i for i in current if not i.isdigit()]) # remove digits from name of node that in differnt locations
          for next in graph.neighbors(current):
            if next in cost_so_far and current == came_from[next]: # avoid repeating expanding the same node at the same location
                break
            new_cost = cost_so_far[current] + graph.cost(current, next)
            priority = new_cost   # underestimate part: real cost  for "NEXT" node
            if next in cost_so_far and current != came_from[next] : #without dynamic programming, which means may expand same node mutiple times at different locations
                 next = next + str(num)  # if there is a different path to "next" node, we label like next1, next2
                

            cost_so_far[next] = new_cost
            
            frontier.put(next, priority)  # use priority queue sort the children nodes and put the least cost node in the front
            came_from[next] = current     # track the  path
        
    d= {key:value for key, value in cost_so_far.items() if goal in key}  # filter the dic for all path to the goal
    Fianlgoal = min(d, key=d.get)  # get the goal label name for the minmum cost path to the goal 
    return came_from, Fianlgoal


# construct the minimum cost path from the came_from dic
def reconstruct_path(result, start, goal):  # here the goal must be 'M', since we already stored the heuristic costs
    
    came_from, Fianlgoal = result
    current = Fianlgoal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    print path


# here the goal must be 'M', since we already stored the heuristic costs
reconstruct_path(branch_bound_search(example_graph, 'A','M'),'A','M')
