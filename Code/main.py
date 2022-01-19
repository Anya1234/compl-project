# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from test import testForSmallUnweighted
from test import testForRandomUnweighted
from naive_solver import NaiveSolver
from graph import Graph
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    testForSmallUnweighted()
    testForRandomUnweighted()
    testForRandomUnweighted(density=10)