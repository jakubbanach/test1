from problems.n_puzzle import NPuzzleState
from problems.n_puzzle.heuristics.n_puzzle_abstract_heuristic import NPuzzleAbstractHeuristic



class NPuzzleTilesOutOfPlaceHeuristic(NPuzzleAbstractHeuristic):

    def __call__(self, state: NPuzzleState) -> float:
        # TODO:
        # Calculate how many tiles are not on their expected positions
        # tip 1.'state' is the current state, 
        # tip 2. you can use self.positions function to get from it a dictionary:
        #   { tile_number : (x_coordinate, y_coordinate) }
        # tip 3. self.goal_coords contains such a dictionary for the goal state
        tilesOutOfPlace = 0
        stateList=self.positions(state)
        #petla przechodzaca po calym slowniku
        for i in list(stateList.keys()):
            state_i=stateList[i]
            state_x=state_i[0]
            state_y=state_i[1]
            goal_i=self.goal_coords[i]
            goal_x=goal_i[0]
            goal_y=goal_i[1]

            if state_x!=goal_x or state_y!=goal_y:
                tilesOutOfPlace+=1
        return tilesOutOfPlace
