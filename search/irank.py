import numpy as np

from structures import Graph


def normalize(vec):
    return np.array(vec) / np.linalg.norm(vec, ord=1)


def IR1(hard_result_set: dict, ordered_list: list, positive_query_len: int, word_count: list = None):
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


def IR2(graph: Graph, hard_result_set: dict, broad_positive_res_set: dict, ordered_list: list, positive_query_len: int,
        word_count: list = None):
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
    return normalize(np.divide(appearance_count, appearance_files))


def IR(graph: Graph, hard_result_set: dict, broad_positive_res_set: dict, ordered_list: list, positive_query_len: int):
    return normalize(np.add(IR1(hard_result_set, ordered_list, positive_query_len),
                            IR2(graph, hard_result_set, broad_positive_res_set, ordered_list, positive_query_len)))


def get_ranks(pagerank, graph: Graph, hard_result_set: dict, broad_positive_res_set: dict,
              ordered_list: list, positive_query_len: int):
    return normalize(np.multiply(pagerank, IR(graph, hard_result_set, broad_positive_res_set,
                                              ordered_list, positive_query_len))).tolist()
