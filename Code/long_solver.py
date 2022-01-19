from graph import Graph
import cvxpy as cp
import numpy as np
from scipy.linalg import ldl
from scipy.stats import norm

from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

class LongSolver:
    '''Exponentially working algorithm'''
    def __init__(self, cur_graph: Graph, precision=5):
        self.graph = cur_graph

    def solve(self):
        '''

        :return: max cut
        '''

        vertices = list(i for i in range(self.graph.n))

        sets = powerset(vertices)
        max_val = 0
        split_1 = ()
        split_2 = vertices
        for subset in sets:
            val = 0
            left = tuple(set(vertices) - set(subset))
            for x in subset:
                for y in left:
                    val += self.graph.adjacencyMatrix[x][y]
            if val > max_val:
                max_val = val
                split_1 = subset
                split_2 = left

        return np.array(split_1)+1, np.array(split_2)+1, max_val
