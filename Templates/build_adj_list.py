from typing import List, Tuple
from collections import defaultdict

def build_adjacency_list_thru_pairs(pairs: List[Tuple(int)])->dict:
    """
    Builds an undirected adjacency list from a pair of connected nodes
    """
    adj_list = defaultdict(lambda x: list)
    for node1, node2 in pairs:
        adj_list[node1].append(node2)
        adj_list[node2].append(node1)

    return adj_list

