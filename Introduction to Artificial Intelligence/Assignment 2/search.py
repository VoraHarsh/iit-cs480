import bisect

def abstract():
    import inspect
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    raise NotImplementedError(caller + ' must be implemented in subclass')

def todo():
    raise NotImplementedError('You must complete the implementation.')

#______________________________________________________________________________
# Queues: FIFOQueue, LIFOQueue, PriorityQueue

class Queue:
    """Queue is an abstract class/interface. There are three types:        
        FIFOQueue(): A First In First Out Queue.
        LIFOQueue(): A Last In First Out Queue.
        PriorityQueue(order, f): Queue in sorted order (default min-first).
    Each type supports the following methods and functions:
        q.append(item)  -- add an item to the queue        
        q.pop()         -- return the top item from the queue
        len(q)          -- number of items in q (also q.__len())
        item in q       -- does q contain item?
    """
   
    def append(self, item):
        abstract()
    
    def pop(self):
        abstract()

class FIFOQueue(Queue):
    """A First-In-First-Out Queue."""
    def __init__(self):
        self.A = []
    
    def append(self, item):
        """Add to the end"""
        self.A.append(item)

    def pop(self):
        """Remove the first item"""
        return self.A.pop(0)
        
    def __contains__(self, item):
        return item in self.A
    
    def __len__(self):
        return len(self.A)
    
    def __repr__(self):
        """Return [A[0], A[1], ...]"""
        rep = "[" + str(self.A[0])
        for i in range(1, len(self.A)):
            rep += ", " + str(self.A[i])
        rep += "]"
        return rep

class LIFOQueue(Queue):
    """A Last-In-First-Out Queue."""
    def __init__(self):
        self.A = []
    
    def append(self, item):
        """Add to the end"""
        self.A.append(item)

    def pop(self):
        """Remove the last item"""
        return self.A.pop()
        
    def __contains__(self, item):
        return item in self.A
    
    def __len__(self):
        return len(self.A)
    
    def __repr__(self):
        """Return [A[0], A[1], ...]"""
        rep = "[" + str(self.A[0])
        for i in range(1, len(self.A)):
            rep += ", " + str(self.A[i])
        rep += "]"
        return rep

class PriorityQueue(Queue):
    """A queue in which the minimum element (as determined by cost_function)
    is returned first. Also supports dict-like lookup.
    """
    def __init__(self, cost_function=lambda x: x):
        self.A = []
        self.cost_function = cost_function
    
    def append(self, item):
        bisect.insort(self.A, (self.cost_function(item), item))
    
    def pop(self):        
        return self.A.pop(0)[1]
        
    def __contains__(self, item):        
        for _, x in self.A:
            if item == x:
                return True                    
        return False
        
    
    def __len__(self):
        return len(self.A)
    
    def __repr__(self):
        """Return [A[0], A[1], ...]"""
        
        rep = "["
        rep += str(self.A[0][1]) + ":" + str(self.A[0][0]) 
        for i in range(1, len(self.A)):
            rep += ", " + str(self.A[i][1]) + ":" + str(self.A[i][0])        
        
        rep += "]"
        
        return rep
    
    
    # For dict-like operations
    def __getitem__(self, key):
        for _, item in self.A:
            if item == key:
                return item
            
    def __delitem__(self, key):
        for i, (_, item) in enumerate(self.A):
            if item == key:
                self.A.pop(i)
                return

class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        "Create a search tree Node, derived from a parent by an action."
        
        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost
        
        self.depth=0        
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node %s>" % (self.state,)
    
    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        "List the nodes reachable in one step from this node."
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        "Fig. 3.10"
        next_node = problem.result(self.state, action)
        return Node(next_node, self, action,
                    problem.path_cost(self.path_cost, self.state, action, next_node))

    def solution(self):
        "Return the sequence of actions to go from the root to this node."
        return [node.action for node in self.path()[1:]]

    def path(self):
        "Return a list of nodes forming the path from the root to this node."
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # We want for a queue of nodes in breadth_first_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)

#______________________________________________________________________________
# Uninformed Search

def uninformed_tree_search(problem, frontier, print_node=True, print_frontier=False):
    """Uninformed tree search. Frontier is either a
    FIFOQueue or a LIFOQueue.
    """
    frontier.append(Node(problem.initial))
    while frontier:
        node = frontier.pop()        
        if problem.goal_test(node.state):
            return node
        for child in node.expand(problem):           
            frontier.append(child)
    return None

def uninformed_graph_search(problem, frontier):
    """Uninformed graph search. Frontier is either a
    FIFOQueue or a LIFOQueue.
    Because it is uninformed, it does not check whether
    a better path to a Node in frontier is found.
    """
    frontier.append(Node(problem.initial))
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
    return None

def breadth_first_search(problem, search_type=uninformed_tree_search):
    return search_type(problem, FIFOQueue())

def depth_first_search(problem, search_type=uninformed_tree_search):
    return search_type(problem, LIFOQueue())
#______________________________________________________________________________
# Informed Search

def best_first_tree_search(problem, cost_function):
    """Search the nodes with the lowest cost_function scores first.
    You specify the function cost_function(node) that you want to minimize
    """
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue(cost_function)
    frontier.append(node)
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node        
        for child in node.expand(problem):            
            frontier.append(child)            
    return None

def best_first_graph_search(problem, cost_function):
    """Search the nodes with the lowest cost_function scores first.
    You specify the function cost_function(node) that you want to minimize.
    Remember the states you have explored and generated.
    """
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = PriorityQueue(cost_function)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                incumbent = frontier[child]
                if cost_function(child) < cost_function(incumbent): # Check if a better path is found
                    del frontier[incumbent]
                    frontier.append(child)
    return None

def uniform_cost_search(problem, search_type=best_first_tree_search):
    return search_type(problem, lambda node: node.path_cost)

def greedy_best_first_search(problem, h, search_type=best_first_tree_search):
    return search_type(problem, lambda node: h(node))

def astar_search(problem, h, search_type=best_first_tree_search):
     return search_type(problem, lambda node: (h(node)+node.path_cost))
