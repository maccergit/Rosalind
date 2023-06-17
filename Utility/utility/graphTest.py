
import unittest
import graph as g

"""
- Run a test to see if the Rosalind edge list format converts properly to networkx graph.
- data : An iterator that represents each line in a Rosalind edge file.  First entry is [#vertices, #edges] - subsequent entries are edges [vertex1 vertex2].
- expected : the expected networkx graph.
"""
def run(data, expected):
    actual = g.processLines(data).adj
    assert actual == expected, actual

class Test(unittest.TestCase):

    def testEmptyGraph(self):
        run(["0 0"], {})
    
    def testSingleNode(self):
        run(["1 0"], {'1': {}})
    
    def test2SingleNodes(self):
        run(["2 0"], {'1': {}, '2': {}})
    
    def test2ConnectedNodes(self):
        run(["2 1", "1 2"], {'1': {'2': {}}, '2': {'1': {}}})
    
    def test2ConnectedNodesReverse(self):
        run(["2 1", "2 1"], {'1': {'2': {}}, '2': {'1': {}}})
    
    def test3SingleNodes(self):
        run(["3 0"], {'1': {}, '2': {}, '3': {}})
    
    def test2ConnectedNodes1SingleNode(self):
        run(["3 1", "1 2"], {'1': {'2': {}}, '2': {'1': {}}, '3': {}})
    
    def test2ConnectedNodes1SingleNode2(self):
        run(["3 1", "2 3"], {'1': {}, '2': {'3': {}}, '3': {'2': {}}})
    
    def test2ConnectedNodes1SingleNode3(self):
        run(["3 1", "1 3"], {'1': {'3': {}}, '2': {}, '3': {'1': {}}})
    
    def test3ConnectedNodes2edges(self):
        run(["3 1", "1 2", "2 3"], {'1': {'2': {}}, '2': {'1': {}, '3': {}}, '3': {'2': {}}})
    
    def test3ConnectedNodes3edges(self):
        run(["3 1", "1 2", "2 3", "1 3"], {'1': {'2': {}, '3': {}}, '2': {'1': {}, '3': {}}, '3': {'1': {}, '2': {}}})

if __name__ == "__main__":
    unittest.main()