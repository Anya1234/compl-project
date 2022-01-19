import numpy as np


class Graph:
    '''Class for represenring graph'''
    def __init__(self, n: int, adjacency_list=None, weights=None, adjacencyMatrix=None):
        if adjacencyMatrix is None:
            if weights is None:
                weights = np.ones(shape=adjacency_list.shape[0])
            self.n = n

            self.adjacencyMatrix = np.zeros(shape=(self.n, self.n))

            for i in range(adjacency_list.shape[0]):
                edge = adjacency_list[i] - 1
                self.adjacencyMatrix[edge[0]][edge[1]] = weights[i]
                self.adjacencyMatrix[edge[1]][edge[0]] = weights[i]
        else:
            self.n = n
            self.adjacencyMatrix = adjacencyMatrix