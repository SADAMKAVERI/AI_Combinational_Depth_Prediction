# Graph-Based Longest Path Analysis
# Represents circuit as a directed graph and finds the longest path

import networkx as nx

def longest_path(graph):
    return nx.dag_longest_path_length(graph)

if __name__ == "__main__":
    print("Graph analysis module")
