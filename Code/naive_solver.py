import numpy as np
from graph import Graph

class NaiveSolver:
    '''Naive randomly choosing cut algorithm'''
    def __init__(self, cur_graph: Graph, precision=5):
        self.graph = cur_graph

    def solve(self):
        '''

        :return: max cut
        '''

        vertices = np.array(list(i for i in range(self.graph.n)))

        first = np.random.choice(vertices, replace=False,
                                      size=np.random.randint(low=0, high=self.graph.n, size=1)[0])

        second = np.array(tuple(set(vertices.tolist()) - set(first.tolist())))
        maxcut = 0
        for i in first:
            for j in second:
                maxcut += self.graph.adjacencyMatrix[i][j]

        return first+1, second+1, maxcut