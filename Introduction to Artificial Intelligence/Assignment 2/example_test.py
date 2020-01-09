from problem import TravelProblem, CityMap, EightPuzzleProblem, misplaced_tiles_heuristic
from search import best_first_tree_search, best_first_graph_search, uninformed_tree_search, uninformed_graph_search
from search import uniform_cost_search, greedy_best_first_search, astar_search, breadth_first_search, depth_first_search

if __name__ == '__main__':
       
    print()
    print( '=' * 50)
    print( '=' * 50)
    print( "EIGHT-PUZZLE PROBLEM")
    print( '=' * 50)
    print( '=' * 50)
      
    ep = EightPuzzleProblem([[3, 1, 2], [7, 5, 0], [4, 6, 8]])
    
    print()
    print( '-' * 50)
    print( "Running BREADTH-FIRST-TREE-SEARCH")
    print( '-' * 50)
    
    bfts = breadth_first_search(ep, search_type=uninformed_tree_search)
    
    print( "Solution", bfts.solution())
    
    print()
    print( '-' * 50)
    print( "Running UNIFORM-COST-TREE-SEARCH")
    print( '-' * 50)
    
    ucts = uniform_cost_search(ep, search_type=best_first_tree_search)
    
    print( "Solution", ucts.solution())
    
    print()
    print( '-' * 50)
    print( "Running GREEDY-BEST-FIRST-TREE-SEARCH USING # MISPLACED TILES HEURISTIC")
    print( '-' * 50)
    
    gbfts = greedy_best_first_search(ep, misplaced_tiles_heuristic, search_type=best_first_tree_search)
    
    print( "Solution", gbfts.solution())
    
    print()
    print( '-' * 50)
    print( "Running A*-TREE-SEARCH USING # MISPLACED TILES HEURISTIC")
    print( '-' * 50)
    
    asts = astar_search(ep, misplaced_tiles_heuristic, search_type=best_first_tree_search)
    
    print( "Solution", asts.solution())
    
    print()
    print( '=' * 50)
    print( '=' * 50)
    print( "A MAP")
    print( '=' * 50)
    print( '=' * 50)
    
    # Roads are
    # Between A and B, cost 2
    # One-way from A to C, cost 4
    # Between A and D, cost 10
    # Between B and D, cost 3
    # Betweeb C and D, cost 6
    
    # Start A, goal D
    
       
    city_map = CityMap()
    
    city_map.add_road('A', 'B', 2)
    city_map.add_one_way_road('A', 'C', 4)
    city_map.add_road('A', 'D', 10)
    city_map.add_road('B', 'D', 3)
    city_map.add_road('C', 'D', 6)
    
    
    # Heuristic
    
    def city_h(node):
        if node.state == 'A':
            return 5
        elif node.state == 'B':
            return 2
        elif node.state == 'C':
            return 1
        elif node.state == 'D':
            return 0
    
    travel_problem = TravelProblem('A', 'D', city_map)
    
    
    print()
    print( '-' * 50)
    print( "Running BREADTH-FIRST-TREE-SEARCH")
    print( '-' * 50)
    
    bfts = breadth_first_search(travel_problem, search_type=uninformed_tree_search)
    
    print( "Solution", bfts.solution())
    
    print()
    print( '-' * 50)
    print( "Running UNIFORM-COST-TREE-SEARCH")
    print( '-' * 50)
    
    ucs = uniform_cost_search(travel_problem, search_type=best_first_tree_search)
    
    print( "Solution", ucs.solution())
    
    print()
    print( '-' * 50)
    print( "Running UNIFORM-COST-GRAPH-SEARCH")
    print( '-' * 50)
    
    ucs = uniform_cost_search(travel_problem, search_type=best_first_graph_search)
    
    print( "Solution", ucs.solution())
    
    print()
    print( '-' * 50)
    print( "Running GREEDY-BEST-FIRST-TREE-SEARCH")
    print( '-' * 50)
    
    gbfs = greedy_best_first_search(travel_problem, city_h, search_type=best_first_tree_search)
    
    print( "Solution", gbfs.solution())
    
    print()
    print( '-' * 50)
    print( "Running GREEDY-BEST-FIRST-GRAPH-SEARCH")
    print( '-' * 50)
    
    gbfs = greedy_best_first_search(travel_problem, city_h, search_type=best_first_graph_search)
    
    print( "Solution", gbfs.solution())
    
    print()
    print( '-' * 50)
    print( "Running A*-TREE-SEARCH")
    print( '-' * 50)
    
    asts = astar_search(travel_problem, city_h, search_type=best_first_tree_search)
    
    print( "Solution", asts.solution())
    
    print()
    print( '-' * 50)
    print( "Running A*-GRAPH-SEARCH")
    print( '-' * 50)
    
    asgs = astar_search(travel_problem, city_h, search_type=best_first_graph_search)
    
    print( "Solution", asgs.solution())
    
    
    
    
    
    
    
    
