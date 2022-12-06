import math

from problems.n_puzzle import NPuzzleState

from problems.n_puzzle.heuristics.n_puzzle_abstract_heuristic import NPuzzleAbstractHeuristic


class NPuzzleManhattanHeuristic(NPuzzleAbstractHeuristic):

    def __call__(self, state: NPuzzleState) -> float:
        # TODO:
        # Calculate a manhattan distance between tiles and their expected places
        # The result should be sum of those distances. 
        # tip 1.'state' is the current state, 
        # tip 2. you can use self.positions function to get from it a dictionary:
        #   { tile_number : (x_coordinate, y_coordinate) }
        # tip 3. self.goal_coords contains such a dictionary for the goal state
        tilesDistanceDiff = 0
        stateList = self.positions(state)
        # petla przechodzaca po calym slowniku
        for i in list(stateList.keys()):
            state_i = stateList[i]
            state_x = state_i[0]
            state_y = state_i[1]
            goal_i = self.goal_coords[i]
            goal_x = goal_i[0]
            goal_y = goal_i[1]

            if state_x != goal_x or state_y != goal_y:
                delta_x=math.fabs(goal_x-state_x)
                delta_y=math.fabs(goal_y-state_y)
                tilesDistanceDiff += delta_x+delta_y
        return tilesDistanceDiff