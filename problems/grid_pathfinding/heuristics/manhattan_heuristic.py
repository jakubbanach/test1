import math

from base import Heuristic
from problems.grid_pathfinding.grid_pathfinding import GridPathfinding
from problems.grid_pathfinding.grid import GridCoord


class GridManhattanHeuristic(Heuristic[GridCoord]):
 
    def __init__(self, problem: GridPathfinding):
        self.problem = problem

    def __call__(self, state: GridCoord) -> float:
        # TODO:
        # Calculate a manhattan distance:
        # - 'state' is the current state
        delta_x = math.fabs(self.problem.goal.x - state.x)
        delta_y = math.fabs(self.problem.goal.y - state.y)
        return delta_x + delta_y

