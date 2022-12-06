import math

from base import Heuristic
from problems.grid_pathfinding.grid_pathfinding import GridPathfinding
from problems.grid_pathfinding.grid import GridCoord


class GridDiagonalHeuristic(Heuristic[GridCoord]):
 
    def __init__(self, problem: GridPathfinding):
        self.problem = problem

    def __call__(self, state: GridCoord) -> float:
        # TODO:
        # Calculate a diagonal distance:
        # - 'state' is the current state 
        # - 'self.problem.goal' is the goal state
        # - 'self.problem.diagonal_weight' is cost of making a diagonal move

        delta_x = math.fabs(self.problem.goal.x - state.x)
        delta_y = math.fabs(self.problem.goal.y - state.y)
        return min(delta_x,delta_y)*self.problem.diagonal_weight+max(delta_x,delta_y)-min(delta_x,delta_y)
