


from typing import Dict, List
from base.heuristic import Heuristic
from problems.blocks_world.blocks_world_problem import BlocksWorldProblem, BlocksWorldState

class BlocksWorldNaiveHeuristic(Heuristic):

    def __init__(self, problem: BlocksWorldProblem) -> None:
        super().__init__(problem)
        self.expected_columns = self._calculate_expected_columns(problem.goal)
        self.expected_fundaments = self._calculate_expected_fundaments(problem.goal)

    def _calculate_expected_columns(self, goal: BlocksWorldState) -> Dict[str, int]:
        #
        # return a dict of form:
        # { <block name> : <index of column in the goal state> }
        res = {}
        for i, col in enumerate(goal.columns):  #odpowiednie bloczki w odpowiednich kolumnach
            for block in col:
                res[block] = i
        return res

    def _calculate_expected_fundaments(self, goal: BlocksWorldState) -> Dict[str, List[str]]:
        #
        # return a dict of form:
        # { <block name> : <list of the blocks below it in the goal state> }
        res = {}
        for col in goal.columns:
            for i, block in enumerate(col): #odpowiednie bloczki pod odpowiednimi bloczkami
                res[block] = col[:i]
        return res

    def __call__(self, state: BlocksWorldState) -> int:
        #
        # - add `1` to the heuristic value per each block placed in an incorrect column
        # - for other blocks, add `2` if their fundament is incorrect
        # tip. use self.expected_columns and self.expected_fundaments
        heur = 0

        for x, col in enumerate(state.columns):
            for y, block in enumerate(col):
                if x != self.expected_columns[block]:   #nieodpowiednia kolumna
                    heur += 1
                elif self.expected_fundaments[block] != col[:y]:    #nieodpowiedni fundament (bloczki pod nim)
                    heur += 2

        return heur