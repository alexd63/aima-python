from search import *

# State representation: a list of four integers, [wolf, goat, cabbage, boat]

class WolfGoatCabbage(Problem):
    initWgc = {'F', 'W', 'G', 'C'}
    goalWgc = {'', '', '', ''}
    # state = initWgc
    def __init__(self, initial=initWgc, goal=goalWgc):
        super().__init__(initial, goal)
        
    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = [('F'), ('F', 'G'), ('F', 'W'), ('F', 'C')]
                            # , {'G', 'F'}, {'G', 'W'}, {'G', 'C'}, {'W', 'F'}, {'W', 'G'}, {'W', 'C'}, {'C', 'F'}, {'C', 'G'}, {'C', 'W'}]
        traveled_objects = self.initial.difference(state)

        # for object in traveled_objects:
        #     if object == 'W':
        #         possible_actions.remove({'F', 'W'})
        #         possible_actions.remove({'F'})
        #         possible_actions.remove({'F', 'G'})
        #     elif object == 'G':
        #         possible_actions.remove({'F', 'G'})
        #         possible_actions.remove({'F'})
        #         possible_actions.remove({'F', 'W'})
        #     elif object == 'C':
        #         possible_actions.remove({'F', 'C'})
        #         possible_actions.remove({'F'})
        #         possible_actions.remove({'F', 'G'})
        #     else:
        #         possible_actions.append({object})

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # # blank is the index of the blank square
        # # blank = self.find_blank_square(state)
        # new_state = list(state)

        # delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        # # neighbor = blank + delta[action]
        # # new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        # return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal


# class WolfGoatCabbage(Problem):
#     def __init__(self):
#         super().__init__(initial=frozenset(['F', 'G', 'W', 'C']), goal=frozenset([]))
        
#     def actions(self, state):
#         """Return the actions that can be executed in the given state."""
#         possible_actions = []
#         # if F is in the state, actions involve moving from left to right bank, and vice versa
#         left_to_right = 'F' in state
        
#         for a in ['G', 'W', 'C']:
#             if left_to_right and a in state:
#                 possible_actions.append(frozenset(['F', a]))
#             elif not left_to_right and a not in state:
#                 possible_actions.append(frozenset(['F', a]))
#         possible_actions.append(frozenset(['F']))
        
#         return possible_actions
    
#     def result(self, state, action):
#         """Return the state that results from executing the given action in the given state."""
#         return state.symmetric_difference(action)
        
#     def goal_test(self, state):
#         """Return True if the state is a goal."""
#         return state == self.goal
    
#     def is_valid_state(self, state):
#         """Check if given state is valid."""
#         # Check if the Goat and Wolf are together without Farmer, or Goat and Cabbage are together without Farmer
#         return not (('G' in state and 'W' in state and 'F' not in state) or 
#                     ('G' not in state and 'W' not in state and 'F' in state) or
#                     ('G' in state and 'C' in state and 'F' not in state) or
#                     ('G' not in state and 'C' not in state and 'F' in state))


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)

    # test change