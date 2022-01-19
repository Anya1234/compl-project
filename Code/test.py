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


def testForRandomUnweighted():
    alpha = 0.87

    for n in range(5, 20):
        print(n)
        for i in range(5):
            graph = Graph(n, np.random.randint(low=0, high=2, size=(n, n)))
            slv = Solver(graph)
            long_slv = LongSolver(graph)
            x, y, cut = slv.solve()
            x_long, y_long, cut_long = long_slv.solve()

            if cut < alpha*cut_long:
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
        print("OK")

def testForRandomUnweighted1():
    alpha = 0.8


    for n in range(5, 15):
        print(n)
        for i in range(5):
            matrix = np.random.randint(low=0, high=5, size=(n, n))
            matrix = np.where(matrix == 0, 0, 1)
            graph = Graph(n, matrix)
            slv = Solver(graph)
            long_slv = LongSolver(graph)
            x, y, cut = slv.solve()
            x_long, y_long, cut_long = long_slv.solve()

            if cut < alpha*cut_long:
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
        print("OK")