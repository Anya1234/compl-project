from graph import Graph
import cvxpy as cp
import numpy as np
from scipy.linalg import ldl
from scipy.stats import norm


class Solver:
    '''Goemans and Williamson algorithm'''
    def __init__(self, cur_graph: Graph, precision=5):
        self.precision=precision
        self.C = cur_graph.adjacencyMatrix
        self.n = cur_graph.n

        self.A = np.zeros(shape=(self.n, self.n, self.n))
        np.fill_diagonal(self.A, 1)

        self.b = np.ones(shape=self.n)
        self.U = np.empty(shape=0)

        self.r = np.zeros(shape=self.n - 1)

    def solveSPD(self):
        '''solves optimization problem min<C,U> for positive semidifinitive U where Uii=1
        :return U where minimum is achieved
        '''
        x = cp.Variable((self.n, self.n), symmetric=True)

        constraints = [x >> 0]
        constraints += [
            cp.trace(self.A[i] @ x) == self.b[i] for i in range(self.n)
        ]

        prob = cp.Problem(cp.Minimize(cp.trace(self.C @ x)),
                          constraints)
        prob.solve()

        self.U = np.round(x.value, decimals=self.precision)

        return self.U

    def compose(self):
        '''composes U to U=X.T@X
        :return X
        '''
        lu, d, perm = ldl(self.U)

        np.fill_diagonal(d, np.diag(d))
        assert np.isclose(lu @ d @ lu.T, self.U).all()

        d[d<0]=0
        self.X = np.round((lu@np.sqrt(d)).T, decimals=self.precision)
        return self.X

    def generateRandomPlane(self):
        '''Generates random plane
            Uses theorem that r/norm(r) distributed on sphere uniformly
            if r has standard Normal distribution
        '''
        self.r = norm.rvs(size=self.n)
        self.r /= np.linalg.norm(self.r)
        self.r = self.r.T

    def choosePartition(self):
        '''

        :return approximate max cut
        '''
        first = list()
        second = list()

        for i in range(self.n):
            if self.r@self.X[:, i] >= 0:
                first.append(i)
            else:
                second.append(i)

        maxcut = 0
        for i in first:
            for j in second:
                maxcut += self.C[i][j]

        return np.array(first)+1, np.array(second)+1, maxcut

    def solve(self):
        '''

        :return: approximate max cut
        '''
        self.solveSPD()
        self.compose()
        self.generateRandomPlane()
        return self.choosePartition()