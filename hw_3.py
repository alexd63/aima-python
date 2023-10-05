from search import *

# eight_puzzle = EightPuzzle(initial=(2,3,1,4,5,7,8,6,0))
# print(astar_search(eight_puzzle, h=None, display=True).solution())

# bfs = print(breadth_first_graph_search(eight_puzzle).solution())

# dfs = print(depth_first_graph_search(eight_puzzle).solution())

eight_puzzle2 = EightPuzzle( initial=(2,3,1,4,5,7,8,6,0) ) # <- change this
if __name__ == '__main__':    
    print(astar_search(eight_puzzle2, h=None, display=True).solution())
    exit()