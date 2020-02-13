"""PageRank algorithm with explicit number of iterations.

Returns
-------
ranking of nodes (pages) in the adjacency matrix

"""

import numpy as np

from structures import Graph


def pagerank(M, num_iterations: int = 100, d: float = 0.85):
    """PageRank: The trillion dollar algorithm.

    Parameters
    ----------
    M : numpy array
        adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
        sum(i, M_i,j) = 1
    num_iterations : int, optional
        number of iterations, by default 100
    d : float, optional
        damping factor, by default 0.85

    Returns
    -------
    numpy array
        a vector of ranks such that v_i is the i-th rank from [0, 1],
        v sums to 1

    """
    N = M.shape[1]
    v = np.random.rand(N, 1)
    v = v / np.linalg.norm(v, 1)
    M_hat = (d * M + (1 - d) / N)
    for i in range(num_iterations):
        v = M_hat @ v
    return v


def construct_pr_adj_matrix(graph: Graph, ordered_list: list):
    ret = np.zeros((len(ordered_list), len(ordered_list)))
    for i in range(len(ordered_list)):
        for j in range(len(ordered_list)):
            if graph.get_edge(ordered_list[j], ordered_list[i]):
                ret[i, j] = 1 / graph.degree(ordered_list[j])
    return ret
