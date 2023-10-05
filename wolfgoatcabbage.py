from search import *

# State representation: a list of four integers, [wolf, goat, cabbage, boat]

class WolfGoatCabbage:
    initWgc = {'F', 'W', 'G', 'C'}
    goalWgc = {'', '', '', ''}
    # state = initWgc
    def __init__(self, initial=initWgc, goal=goalWgc):
        self.initial = initial
        self.goal = goal
        
    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = [{'F'}, {'F', 'G'}, {'F', 'W'}, {'F', 'C'}]
        traveled_objects = state.difference(self.initial)

        for object in traveled_objects:
            if object == 'W':
                possible_actions.remove({'F', 'W'})
            elif object == 'G':
                possible_actions.remove({'F', 'G'})
            elif object == 'C':
                possible_actions.remove({'F', 'C'})
            else:
                possible_actions.remove({'F'})

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)

    # test change