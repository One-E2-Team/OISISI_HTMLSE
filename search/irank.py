import numpy as np

from structures import Graph


def normalize(vec):
    """
    Function performs mathematical normalization of the first order for a given n - dimensional vector.
    :param vec: vector to be normalized
    :return: normalized vector
    """
    if np.count_nonzero(vec) == 0:
        return vec
    return np.array(vec) / np.linalg.norm(vec, ord=1)


def IRank1(hard_result_set: dict, ordered_list: list, positive_query_len: int, word_count: list = None):
    """
    IR1 is normalized.

        IR1 = appearance penal factor * appearance dividend

    Appearance penal factor - takes values from 0 to 1, all sites not matching The Query given by our God Saviour - User
                                are 0, this will also further propagate to RANK and assure that only sites matching
                                given criteria appears in results. Otherwise, this holds a number following formula:

                                    number of words from positive query appearing on site / num of words in pos. query

                                therefore, max value is 1 (all words are present)
    Appearance dividend - holds count of positive search query words in site divided by maximal same number across all
                            sites
    """
    # word count is not used, but it could be, to utilize percentage of searched words per document
    appearance_penal_factor = np.zeros(len(ordered_list))
    appearance_dividend = np.ones(len(ordered_list))
    for file in ordered_list:
        if positive_query_len == 0 and file in hard_result_set:
            appearance_penal_factor[ordered_list.index(file)] = 1
        elif file in hard_result_set:
            appearance_penal_factor[ordered_list.index(file)] = \
                np.count_nonzero(hard_result_set[file]) / positive_query_len
            appearance_dividend[ordered_list.index(file)] = np.sum(hard_result_set[file])
            # / word_count[ordered_list.index(file)]
    return normalize(np.multiply(appearance_penal_factor, appearance_dividend / np.max(appearance_dividend)))


def IRank2(graph: Graph, hard_result_set: dict, broad_positive_res_set: dict, ordered_list: list,
           positive_query_len: int, word_count: list = None):
    """
    Calculates IR2 factor by formula:

            IR2 = 1 + appearance words count / appearance file count

    Appearance word count - for each site that has a link to matched site, sum of count of appearances of words from
                            positive query
    Appearance file count - number of linking sites in which appear words from positive search query
    """
    # word count is not used, but it could be, to utilize percentage of searched words per document
    appearance_count = np.zeros(len(ordered_list))
    appearance_files = np.ones(len(ordered_list))
    for file in ordered_list:
        if positive_query_len == 0:
            break
        elif file in hard_result_set:
            appearance_files[ordered_list.index(file)] = 0
            for edge in graph.incident_edges(file, outgoing=False):
                inlink = edge.opposite(file)
                if inlink in broad_positive_res_set:
                    appearance_count[ordered_list.index(file)] += np.sum(broad_positive_res_set[inlink])
                    appearance_files[ordered_list.index(file)] += 1
                elif inlink in hard_result_set:
                    appearance_count[ordered_list.index(file)] += np.sum(hard_result_set[inlink])
                    appearance_files[ordered_list.index(file)] += 1
            if appearance_files[ordered_list.index(file)] == 0:
                appearance_files[ordered_list.index(file)] = 1
    return 1 + np.divide(appearance_count, appearance_files)


def IRank(graph: Graph, hard_result_set: dict, broad_positive_res_set: dict,
          ordered_list: list, positive_query_len: int):
    """
    IR is normalized.

        IR = IR1 * IR2

    For further details on algorithm see IRank1 and IRank2 functions in this module.
    """
    IR1 = IRank1(hard_result_set, ordered_list, positive_query_len)
    IR2 = IRank2(graph, hard_result_set, broad_positive_res_set, ordered_list, positive_query_len)
    return normalize(np.multiply(IR1, IR2)), IR1, IR2


def get_ranks(pagerank: np.ndarray, graph: Graph, hard_result_set: dict, broad_positive_res_set: dict,
              ordered_list: list, positive_query_len: int):
    """
    Rank calculation algorithm:

    Formula influenced by:
        number of appearances of the searched words on site - IR1 (included in IR)
        number of sites linking to site - PR (PageRank - US6285999B1)
        number of searched words on linking sites to site - IR2 (included in IR)

    Normalized version of PageRank is used (values 0-1) - PR
    IR is also normalized.

        RANK = PR * IR

    RANK is normalized.

    For details on the algorithm see function IRank in this module and pagerank.py module.

    :param pagerank: PR
    :param graph: PopulateStructures attribute
    :param hard_result_set: result set of the search query
    :param broad_positive_res_set: result set of broad set of sites influencing ranking algorithm
    :param ordered_list: order od sites from PS object
    :param positive_query_len: number of parameters influencing ranking process (all 'positive' words)
    :return: rank matrix (with additional details)
    """
    pagerank = pagerank.reshape((len(ordered_list),))
    IR, IR1, IR2 = IRank(graph, hard_result_set, broad_positive_res_set, ordered_list, positive_query_len)
    return np.concatenate((normalize(np.multiply(pagerank, IR)).reshape((len(ordered_list), 1)),
                           pagerank.reshape((len(ordered_list), 1)),
                           IR.reshape((len(ordered_list), 1)),
                           IR1.reshape((len(ordered_list), 1)),
                           IR2.reshape((len(ordered_list), 1))),
                          axis=1).tolist()
