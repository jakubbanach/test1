import math

from base import Heuristic
from problems.grid_pathfinding.grid_pathfinding import GridPathfinding
from problems.grid_pathfinding.grid import GridCoord
from math import sqrt


class GridEuclideanHeuristic(Heuristic[GridCoord]):
 
    def __init__(self, problem: GridPathfinding):
        self.problem = problem

    def __call__(self, state: GridCoord) -> float:
        # TODO:
        # Calculate an euclidean distance:
        # - 'state' is the current state 
        # - 'self.problem.goal' is the goal state
        delta_x = math.fabs(self.problem.goal.x - state.x)
        delta_y = math.fabs(self.problem.goal.y - state.y)
        return math.sqrt(delta_x * delta_x + delta_y * delta_y)
  
