from Heuristic import Heuristic

from EightPuzzleState import State
from output_util import output_result

import sys

visited_state = {}
state_parent = {}


class hill_climbing:
    def __init__(self, intial_state, goal_state):
        self.initial_configuration = intial_state
        self.final_configuration = goal_state
        self.state_explored = 0

    def solve_eight_puzzle(self, current_state, heuristic_choice,depth = 0):
        stack = [current_state]
        while len(stack) != 0 :
            print(self.state_explored, current_state, depth)
            current_state = stack.pop()
            if current_state == self.final_configuration:
                self.state_explored += 1
                print("Goal Achieved....")
                out = output_result(self.initial_configuration, "hill_climbing_result.txt", state_parent,
                                    self.state_explored)
                out.write_output_path(current_state)
                return 0
            elif current_state in visited_state:
                continue
            else:
                self.state_explored += 1
                visited_state[current_state] = 1
                state = State(current_state, Heuristic(self.final_configuration).getHeuristicEstimation(
                    current_state, heuristic_choice
                ))
                neighbours = state.getAllSuccessor(heuristic_choice)
                neighbours.sort()
                neighbours.reverse()
                for neighbour in neighbours:
                    if neighbour.hvalue > state.hvalue:
                        # pass
                        print("stuck in local maxima")
                    if neighbour.puzzleState in visited_state:
                        continue
                    else:
                        state_parent[neighbour.puzzleState] = current_state
                        stack.append(neighbour.puzzleState)
        # self.state_explored += 1
        # print(self.state_explored , current_state, depth)
        # if current_state == self.final_configuration:
        #     out = output_result(self.initial_configuration,"hill_climbing_result.txt",state_parent,self.state_explored)
        #     out.write_output_path(current_state)
        #     print("Goal Achieved....")
        #     return 1
        # else:
        #     visited_state[current_state] = 1
        #     state = State(current_state, Heuristic(self.final_configuration).getHeuristicEstimation(
        #         current_state, heuristic_choice
        #     ))
        #     neighbours = state.getAllSuccessor(heuristic_choice)
        #     neighbours.sort()
        #     for neighbour in neighbours:
        #         if neighbour.hvalue > state.hvalue:
        #             print("stuck in local maxima")
        #         if neighbour.puzzleState in visited_state:
        #             continue
        #         else:
        #             state_parent[neighbour.puzzleState] = current_state
        #             success_indicator = self.solve_eight_puzzle(neighbour.puzzleState, heuristic_choice,depth+1)
        #             if success_indicator == 1:
        #                 return success_indicator
        return 1
