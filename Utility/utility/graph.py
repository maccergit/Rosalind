# coding: utf8
"""
Utilities that support using networkx with Rosalind formatted data files.
"""

import networkx as nx

def processLines(lines):
    """
    Convert iterable containing Rosalind style edge list data to networkx graph.
    
    Used to decouple I/O from actual processing to facilitate unit testing.
    """
    # First line is number of vertices and edges, and is not handled by networkx module.
    v_count = [int(x.strip()) for x in lines[0].split()][0]
    # Read the rest of the files (which is just edges) as a regular networkx graph.
    mygraph = nx.parse_edgelist(lines[1:])
    # See if any stand-alone nodes need to be added to the graph - we only need to compare vertex count, and can ignore the edge count.
    for node in (str(x) for x in range(1, v_count + 1)):
        if node not in mygraph:
            mygraph.add_node(node)
    return mygraph

def readRosalindEdgeFile(inFileName):
    """
    Read a Rosalind style edge list file and return a networkx graph.
    
    The stock edge list reader for networkx expects the file to only contain edges.  However, a graph with stand-alone nodes cannot be represented using only edges - this is a limitation of the
    edge list reader in networkx.  Rosalind provides extra information on the first line about the number of vertices and edges, and since Rosalind uses numbered vertices starting with 1, this
    can be combined with the edge data to infer any stand-alone nodes.
    """
    with open(inFileName) as datafile:
        return processLines(datafile.readlines())