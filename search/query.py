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
                                appearances for every searched word in positive_query
             broad_positive_res_set: dict with file paths as keys and numbers of appearances for every searched word
                                    present in positive_query (sites present in hard_result_set are not included)
    """
    query = get_correct_query(query)
    flag = None
    words = []
    ret_string = ""
    broad_search = {}
    hard_search = {}
    if ' ' not in query:
        paths = trie.word_exists(query)
        ret_string = query
        if paths is not False:
            result_set = Set()
            for p in paths.keys():
                result_set.add(p)
                broad_search[p] = []
                broad_search[p].append(paths[p])
            """ hard and broad search are same for 1 word """
            return ret_string, broad_search, broad_search
        print("'" + query + "' doesn't exist in trie")
        return ret_string, hard_search, broad_search
    elif ' and ' not in query and ' or ' not in query and ' not ' not in query:
        flag = 'or'
        words = query.split(' ')
    else:
        parts = query.split(' ')
        words.append(parts[0])
        words.append(parts[2])
        if parts[1] == 'and':
            flag = 'and'
        elif parts[1] == 'not':
            flag = 'not'
        elif parts[1] == 'or':
            flag = 'or'
    if flag is not None:
        if flag == 'and' or flag == 'or':
            for i in range(0, len(words)):
                ret_string += words[i] + " "
        else:
            ret_string += words[0]
        ret_string = ret_string.strip()
        if flag == 'and' or flag == 'not':
            first = Set()
            second = Set()
            paths = trie.word_exists(words[0])
            if paths is not False:
                for p in paths.keys():
                    first.add(p)
                    broad_search[p] = []
                    broad_search[p].append(paths[p])
                    if flag != 'not':
                        broad_search[p].append(0)
            paths = trie.word_exists(words[1])
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
                result_set = first & second
            elif flag == 'not':
                result_set = first - second
            for i in result_set.get_list():
                hard_search[i] = broad_search[i]
            return ret_string, hard_search, broad_search
        elif flag == 'or':
            sets = []
            for i in range(len(words)):
                new_set = Set()
                paths = trie.word_exists(words[i])
                if paths is not False:
                    for p in paths:
                        new_set.add(p)
                        if p not in broad_search.keys():
                            broad_search[p] = [0] * len(words)
                            broad_search[p][i] = paths[p]
                        elif p in broad_search.keys():
                            broad_search[p][i] = paths[p]
                sets.append(new_set)
            result_set = sets[0]
            for i in range(1, len(words)):
                result_set = result_set | sets[i]
            for i in result_set.get_list():
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
