from parse.parse_html_tree import PopulateStructures
from structures import Trie, Set
from .query_parser import Node


def evaluate(parsed_query_tree: Node, data: PopulateStructures):
    sets = []
    for child in parsed_query_tree.children:
        set = evaluate(child, data)
        sets.append(set)
    if parsed_query_tree.value == '||':
        return sets[0] | sets[1]
    elif parsed_query_tree.value == '&&':
        return sets[0] & sets[1]
    elif parsed_query_tree.value == '()':
        return sets[0]
    elif parsed_query_tree.value == '!':
        return get_world_set(data.html_files) - sets[0]
    else:
        return get_set(str(parsed_query_tree.value), data.trie)


def get_set(word: str, trie: Trie):
    paths = trie.word_exists(word)
    if paths is not False:
        ret = Set()
        for path in list(paths.keys()):
            ret.add(path)
        return ret
    else:
        return Set()


def get_world_set(html_files: list):
    ret = Set()
    for html in html_files:
        ret.add(html)
    return ret


def get_positive_list(parsed_query_tree: Node, lst: list):
    if parsed_query_tree.value == '!':
        return
    elif parsed_query_tree.value != '()' and parsed_query_tree.value != '&&' and parsed_query_tree.value != '||':
        lst.append(str(parsed_query_tree.value))
        return
    for child in parsed_query_tree.children:
        get_positive_list(child, lst)


def __populate_dict_by_positive_query(pos_q: list, dic: dict, trie: Trie):
    for word in pos_q:
        paths = trie.word_exists(word)
        if paths is not False:
            for html in dic.keys():
                if paths.get(html) is not None:
                    dic[html].append(paths[html])
        else:
            for html in dic.keys():
                dic[html].append(0)


def eval_query(parsed_query_tree: Node, data: PopulateStructures):
    positive_query_list = []
    get_positive_list(parsed_query_tree, positive_query_list)
    positive_query = ''
    for word in positive_query_list:
        positive_query += word + ' '
    positive_query.strip()
    hard_result_set_set = evaluate(parsed_query_tree, data)
    hard_result_set = {}
    for res in hard_result_set_set:
        hard_result_set[res] = []
    __populate_dict_by_positive_query(positive_query_list, hard_result_set, data.trie)
    broad_positive_res_set_set = Set()
    for word in positive_query_list:
        set = get_set(word, data.trie)
        if set is not False:
            broad_positive_res_set_set = broad_positive_res_set_set | set
    broad_positive_res_set_set = broad_positive_res_set_set - hard_result_set_set
    broad_positive_res_set = {}
    for res in broad_positive_res_set_set:
        broad_positive_res_set[res] = []
    __populate_dict_by_positive_query(positive_query_list, broad_positive_res_set, data.trie)
    return positive_query, hard_result_set, broad_positive_res_set
