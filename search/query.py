from structures.set import Set


def validate_query(query: str):
    """
    Checking validation for normal(not advanced) search

    :param query: input query for normal(not advanced) search
    :return: True if query is valid
    """
    query = get_correct_query(query)
    if query == 'and' or query == 'not' or query == 'or':
        return False
    elif ' ' not in query:
        return True
    else:
        parts = query.split(' ')
        if 'and' not in parts and 'or' not in parts and 'not' not in parts:
            return True
        if len(parts) != 3:
            return False
        elif parts[0] == 'and' or parts[0] == 'not' or parts[0] == 'or' or parts[2] == 'and' or parts[2] == 'not' or \
                parts[2] == 'or':
            return False
        elif parts[1] != 'and' and parts[1] != 'not' and parts[1] != 'or':
            return False
        return True


def execute_query(query, trie):
    """
    Method executes normal search query and returns proper data structures

    :param query: input string
    :param trie: populated trie
    :return: positive_query: string with searched words(excluding words after NOT operator)
             hard_result_set: dict with file paths that satisfies constraints in query as keys and numbers of
    appearances for every searched word on those paths
             broad_positive_res_set: dict with file paths as keys and numbers of appearances for every searched word
    on those paths
    """
    query = get_correct_query(query)
    flag = None
    words = []
    ret_string = ""
    broad_search = {}
    hard_search = {}
    if ' ' not in query:
        paths = trie.word_exists(query)
        ret_string += query
        if paths is not False:
            ret = Set()
            for p in paths.keys():
                ret.add(p)
                broad_search[p] = []
                broad_search[p].append(paths[p])
            for i in ret.get_list():
                hard_search[i] = broad_search[i]
            return ret_string, hard_search, broad_search
        else:
            print("'" + query + "' doesn't exist in trie")
            return ret_string, hard_search, broad_search
    elif ' and ' not in query and ' or ' not in query and ' not ' not in query:
        flag = 'or'
        words = query.split(' ')
    else:
        parts = query.split(' ')
        if parts[1] == 'and':
            flag = 'and'
            words.append(parts[0])
            words.append(parts[2])
        elif parts[1] == 'not':
            flag = 'not'
            words.append(parts[0])
            words.append(parts[2])
        elif parts[1] == 'or':
            flag = 'or'
            words.append(parts[0])
            words.append(parts[2])
    if flag is not None:
        correct_words = []
        for w in words:
            if w != '':
                correct_words.append(w)
        if flag == 'and' or flag == 'or':
            for i in range(0, len(correct_words)):
                ret_string += correct_words[i] + " "
        elif flag == "not":
            ret_string += correct_words[0]
        ret_string = ret_string.strip()
        if flag == 'and' or flag == 'not':
            first = Set()
            second = Set()
            paths = trie.word_exists(correct_words[0])
            if paths is not False:
                for p in paths.keys():
                    first.add(p)
                    broad_search[p] = []
                    broad_search[p].append(paths[p])
                    if flag != 'not':
                        broad_search[p].append(0)
            paths = trie.word_exists(correct_words[1])
            if paths is not False:
                for p in paths.keys():
                    second.add(p)
                    if flag != 'not' and p not in broad_search.keys():
                        broad_search[p] = []
                        broad_search[p].append(0)
                        broad_search[p].append(paths[p])
                    elif flag != 'not' and p in broad_search.keys():
                        broad_search[p][1] = paths[p]
            if flag == 'and':
                ret = first & second
            elif flag == 'not':
                ret = first - second
            for i in ret.get_list():
                hard_search[i] = broad_search[i]
            return ret_string, hard_search, broad_search
        elif flag == 'or':
            sets = []
            for i in range(len(correct_words)):
                sets.append(Set())
            for i in range(len(correct_words)):
                paths = trie.word_exists(correct_words[i])
                if paths is not False:
                    for p in paths:
                        sets[i].add(p)
                        if p not in broad_search.keys():
                            broad_search[p] = []
                            for j in range(len(correct_words)):
                                broad_search[p].append(0)
                            broad_search[p][i] = paths[p]
                        elif p in broad_search.keys():
                            broad_search[p][i] = paths[p]
            ret = sets[0]
            for i in range(1, len(correct_words)):
                ret = ret | sets[i]
            for i in ret.get_list():
                hard_search[i] = broad_search[i]
            return ret_string, hard_search, broad_search


def get_correct_query(input_query: str):
    """
    Ignoring multiple whitespaces in input string

    :param input_query: string
    :return: same query with 1 whitespace between words
    """
    correct_words = []
    words = input_query.split(' ')
    for w in words:
        w = w.strip()
        if w != '':
            correct_words.append(w)
    ret = ""
    for w in correct_words:
        ret += w + " "
    return ret.strip()
