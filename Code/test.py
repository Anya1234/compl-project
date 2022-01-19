from long_solver import LongSolver
from solver import Solver
from graph import Graph
import numpy as np


def testForSmallUnweighted():
    graphs = [Graph(2, adjacency_list=np.array([[1, 2]])),
              Graph(3, adjacency_list=np.array([[1, 2]])),
              Graph(3, adjacency_list=np.array([[1, 2], [2, 3]])),
              Graph(3, adjacency_list=np.array([[1, 2], [2, 3], [1, 3]])),
              Graph(4, adjacency_list=np.array([[1, 2], [2, 3], [1, 4], [3, 4]])),
              Graph(4, adjacency_list=np.array([[1, 2], [2, 3], [1, 4], [2, 4], [3, 4]])),
              Graph(4, adjacency_list=np.array([[1, 2], [2, 3], [1, 4], [2, 4]])),
              Graph(4, adjacency_list=np.array([[1, 2], [1, 4], [2, 4]])),
              Graph(4, adjacency_list=np.array([[1, 2], [1, 3], [1, 4]]))]

    for graph in graphs:
        slv = Solver(graph)
        long_slv = LongSolver(graph)
        x, y, cut = slv.solve()
        x_long, y_long, cut_long = long_slv.solve()

        if cut != cut_long:
            print("POl Algo")
            print(cut)
            print(x)
            print(y)
            print("EXP Algo")
            print(cut_long)
            print(x_long)
            print(y_long)
            print("FAIL")
            return

    print("SMALL CASES OK")


def testForRandomUnweighted(values=range(5, 15), density=1):
    alpha = 0.8

    for n in values:
        print(n)
        fail_num = 0
        for i in range(5):
            for j in range(10):
                matrix = np.random.randint(low=0, high=density+1, size=(n, n))
                graph = Graph(n, adjacencyMatrix=matrix)
                slv = Solver(graph)
                long_slv = LongSolver(graph)
                x, y, cut = slv.solve()
                x_long, y_long, cut_long = long_slv.solve()

                if cut < alpha*cut_long:
                    if j < 9:
                        continue
                    else:
                        fail_num += 1
        print("FAILED " + str(fail_num) + " TIMES")