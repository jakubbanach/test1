from multiprocessing.spawn import is_forking
from typing import Callable, Optional
from base.problem import Problem
from base.state import State
from solvers.utils import PriorityQueue
from tree import Node, Tree


class BestFirstSearch:
    """
    Type of search that have access to problem definition and to heuristic, that allows it estimate
    which nodes should be searched.
    """

    def __init__(self, problem: Problem, eval_fun: Callable[[Node], float]):
        self.problem = problem
        self.start: State = problem.initial
        self.root = Node(self.start)
        self.frontier: PriorityQueue = PriorityQueue(eval_fun)
        self.visited = {self.start: float(self.root.cost)}
        self.tree = Tree(self.root)

    def solve(self) -> Optional[Node]:
        if self.problem.is_goal(self.start):
            return self.root

        self.frontier.push(self.root)
        while not self.frontier.is_empty():
            current = self.frontier.pop()
            if self.problem.is_goal(current.state):
                return current
            for child in self.tree.expand(self.problem, current):
                if child.state not in self.visited.keys():
                    self.visited[child.state] = self.visited[current.state] + 1
                    self.frontier.push(child)
                elif self.visited[child.state] < self.visited[current.state]:
                    self.visited[current.state] = self.visited[child.state] + 1
                    self.frontier.push(child)

        return None

        # TODO:
        # - if the root node is a goal, just return it
        #   tip. use 'is_goal' method from Problem
        # - push root node to the frontier
        # - pop nodes from the frontier as long as there any
        #   - if popped node is a goal, return it
        #   - otherwise go through all its children (expand method of Tree)
        #       - if child has not been visited (check self.visited dictionary)
        #         or its cost is better than the saved one
        #         * update cost in visited
        #         * push child onto frontier
        # - return None if nothing happens
