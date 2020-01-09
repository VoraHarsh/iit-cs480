def abstract():
    import inspect
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    raise NotImplementedError(caller + ' must be implemented in subclass')

class Problem(object):
    """The abstract class for a formal problem.  You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial; self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        abstract()

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        abstract()

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Override this
        method if checking against a single self.goal is not enough."""
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

class NQueensProblem(Problem):
    """The problem of placing N queens on an NxN board with none attacking
    each other.  A state is represented as an N-element array, where
    a value of r in the c-th entry means there is a queen at column c,
    row r, and a value of None means that the c-th column has not been
    filled in yet.  We fill in columns left to right.
    >>> depth_first_tree_search(NQueensProblem(8))
    <Node [7, 3, 0, 2, 5, 1, 6, 4]>
    """
    def __init__(self, N):
        self.N = N
        self.initial = [None] * N

    def actions(self, state):
        "In the leftmost empty column, try all non-conflicting rows."
        if state[-1] is not None:
            return [] # All columns filled; no successors
        else:
            col = state.index(None)
            return [row for row in range(self.N)
                    if not self.conflicted(state, row, col)]

    def result(self, state, row):
        "Place the next queen at the given row."
        col = state.index(None)
        new = state[:]
        new[col] = row
        return new

    def conflicted(self, state, row, col):
        "Would placing a queen at (row, col) conflict with anything?"
        return any(self.conflict(row, col, state[c], c)
                   for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        "Would putting two queens in (row1, col1) and (row2, col2) conflict?"
        return (row1 == row2 ## same row
                or col1 == col2 ## same column
                or row1-col1 == row2-col2  ## same \ diagonal
                or row1+col1 == row2+col2) ## same / diagonal

    def goal_test(self, state):
        "Check if all columns filled, no conflicts."
        if state[-1] is None:
            return False
        return not any(self.conflicted(state, state[col], col)
                       for col in range(len(state)))

import numpy as np


def misplaced_tiles_heuristic(node):
    state = node.state.arr
    goal = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    num_misplaced_tiles = np.sum(state != goal)
    # do not count the blank (0) tile
    if state[0,0] != 0:
        num_misplaced_tiles -= 1
    return num_misplaced_tiles

import hashlib as hl

class HashableNDArray():
    
    def __init__(self, arr):
        self.arr = arr
    
    def __eq__(self, other):
        return isinstance(other, HashableNDArray) and np.all(self.arr == other.arr)
    
    def __hash__(self):
        return int(hl.sha1(self.arr.view(np.uint8)).hexdigest(), 16)
    
    def __lt__(self, hashableNDArray):
        return (self.arr < hashableNDArray.arr).all()
    
    def __repr__(self):
        return str(self.arr)

class EightPuzzleProblem(Problem):
    
    def __init__(self, initial):
        self.initial = HashableNDArray(np.array(initial))
        self.goal = HashableNDArray(np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]]))
    
    def actions(self, state):
                
        possible_actions = []
        
        # find where zero is
        row, col = np.where(state.arr == 0) # not that np.where returns all locations that has zero; so row and col are arrays
        row = row[0]
        col = col[0]
        
        if col > 0:
            possible_actions.append('L')
        
        if col < 2:
            possible_actions.append('R')
        
        if row > 0:
            possible_actions.append('U')
        
        if row < 2:
            possible_actions.append('D')
        
        
        return possible_actions
    
    def result(self, state, action):
        # find where zero is
        row, col = np.where(state.arr == 0) # not that np.where returns all locations that has zero; so row and col are arrays
        row = row[0]
        col = col[0]
        new_state = np.copy(state.arr)
        # assume the actions are all legal
        if action == 'U':
            replace_val = new_state[row-1, col]
            new_state[row-1, col] = 0
            new_state[row, col] = replace_val
        elif action == 'D':
            replace_val = new_state[row+1, col]
            new_state[row+1, col] = 0
            new_state[row, col] = replace_val
        elif action == 'L':
            replace_val = new_state[row, col-1]
            new_state[row, col-1] = 0
            new_state[row, col] = replace_val
        elif action == 'R':
            replace_val = new_state[row, col+1]
            new_state[row, col+1] = 0
            new_state[row, col] = replace_val
        
        return HashableNDArray(new_state)
    
    def goal_test(self, state):
        return state == self.goal

class CityMap:
    """A City Map that connects cities through roads. Roads can be one-way.
    Each road has a distance associated with it.
    The underlying structure is a dictionary of dictionaries. Example:
    {'Arad' : {'Sibiu': 140, 'Timisoara': 111, 'Zerind': 75}, ...}
    """

    def __init__(self):
        self.the_map = {}

    def add_one_way_road(self, A, B, distance):
        """Add a one-way road"""
        self.the_map.setdefault(A,{})[B] = distance
    
    def add_road(self, A, B, distance):
        """Add a typical road that runs both ways"""
        self.the_map.setdefault(A,{})[B] = distance
        self.the_map.setdefault(B,{})[A] = distance       

    def distance(self, A, B):
        roads_from_A = self.the_map.setdefault(A, {})
        if B in roads_from_A.keys():
            return roads_from_A[B]
        else:
            return None
    
    def reachable_cities(self, A):
        return self.the_map.setdefault(A, {}).keys()

class TravelProblem(object):
    """Given a CityMap, an initial city, and a goal city, find the shortest-cost path.
    Each state is a city.
    """

    def __init__(self, initial, goal, city_map):        
        self.initial = initial
        self.goal = goal
        self.city_map = city_map

    def actions(self, state):
        """Return the reachable cities."""
        return self.city_map.reachable_cities(state)

    def result(self, state, action):
        """Because the actions and states are cities, simply return the action."""
        return action

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):        
        return c + (self.city_map.distance(state1, state2) or np.inf)
    
    
