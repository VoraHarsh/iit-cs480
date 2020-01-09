from problem import TravelProblem, CityMap, NQueensProblem
from search import best_first_tree_search, best_first_graph_search, uninformed_tree_search
from search import uniform_cost_search, greedy_best_first_search, astar_search, breadth_first_search, depth_first_search
from search import todo

if __name__ == '__main__':
       
    print()
    print( '=' * 50)
    print( '=' * 50)
    print( "Q1: FIVE QUEENS")
    print( '=' * 50)
    print( '=' * 50)
      
    fq = NQueensProblem(5)
    
    print()
    print( '-' * 50)
    print( "DEPTH-FIRST-TREE-SEARCH")
    print( '-' * 50)
    
    dfts = depth_first_search(fq, search_type=uninformed_tree_search)
    
    print( "Solution", dfts.solution())
    
    
    print()
    print( '=' * 50)
    print( '=' * 50)
    print( "Q2-5: TRAVEL")
    print( '=' * 50)
    print( '=' * 50)
    
    city_map = CityMap()
    
    city_map.add_road('F', 'S', 5)
    city_map.add_one_way_road('S', 'A', 2)
    city_map.add_road('S', 'C', 6)
    city_map.add_road('A', 'B', 5)
    city_map.add_one_way_road('A', 'D', 3)
    city_map.add_road('B', 'G', 7)
    city_map.add_road('D', 'E', 4)
    city_map.add_road('E', 'G', 3)
    city_map.add_road('C', 'E', 4)
    city_map.add_one_way_road('C', 'D', 3)

    '''todo() # Make sure to add all roads'''
        

    def city_h(node):
        if node.state == 'A':
            return 5
        elif node.state == 'B':
            return 2
        elif node.state == 'C':
            return 7
        elif node.state == 'D':
            return 5
        elif node.state == 'E':
            return 2	
        elif node.state == 'F':
            return 10
        elif node.state == 'G':
            return 0
        elif node.state == 'S':
            return 8
            
    
    travel_problem = TravelProblem('S', 'G', city_map)
    
    print()
    print( '-' * 50)
    print( "Q2: BREADTH-FIRST-TREE-SEARCH")
    print( '-' * 50)
    
    bfts = breadth_first_search(travel_problem, search_type=uninformed_graph_search)
    
    print( "Solution", bfts.solution())
    
    
    print()
    print( '-' * 50)
    print( "Q3: UNIFORM-COST-GRAPH-SEARCH")
    print( '-' * 50)
    
    ucs = uniform_cost_search(travel_problem, search_type=best_first_graph_search)
    
    print( "Solution", ucs.solution())
    
    print()
    print( '-' * 50)
    print( "Q4: GREEDY-BEST-FIRST-TREE-SEARCH")
    print( '-' * 50)
    
    gbfs = greedy_best_first_search(travel_problem, city_h, search_type=best_first_tree_search)
    
    print( "Solution", gbfs.solution())
    
    
    print()
    print( '-' * 50)
    print( "Q5: A*-TREE-SEARCH")
    print( '-' * 50)
    
    asts = astar_search(travel_problem, city_h, search_type=best_first_tree_search)
    
    print( "Solution", asts.solution())
