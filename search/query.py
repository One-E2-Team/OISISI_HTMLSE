from structures.set import Set

def validate_query(query):
    if query == 'and' or query == 'not' or query == 'or':
        return False
    elif ' ' not in query:
        return True
    else:
        if 'and' not in query and 'or' not in query and 'not' not in query:
            return True
        parts = query.split(' ')
        if len(parts) != 3:
            return False
        elif parts[0] == 'and' or parts[0] == 'not' or parts[0] == 'or' or parts[2] == 'and' or parts[2] == 'not' or parts[2] == 'or':
            return False
        elif parts[1] != 'and' and parts[1] != 'not' and parts[1] != 'or':
            return False
        return True


def execute_query(query, trie):
    flag = None
    words = []
    ret_string = ""
    if ' ' not in query:
        paths = trie.word_exists(query)
        ret_string += query
        if paths is not False:
            ret = Set()
            for p in paths:
                ret.add(p)
            return ret_string, ret
        else:
            print("'" + query + "' doesn't exist in trie")
            return ret_string, None
    elif 'and' not in query and 'or' not in query and 'not' not in query:
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
        if flag == 'and' or flag == 'not':
            first = Set()
            second = Set()
            paths = trie.word_exists(correct_words[0])
            if paths is not False:
                for p in paths:
                    first.add(p)
            paths = trie.word_exists(correct_words[1])
            if paths is not False:
                for p in paths:
                    second.add(p)
            #print(first)
            #print(second)
            if flag == 'and':
                ret = first.__and__(second)
            elif flag == 'not':
                ret = first.__sub__(second)
            #print(ret)
            return ret_string, ret
        elif flag == 'or':
            sets = []
            for i in range(0, correct_words.__len__()):
                sets.append(Set())
            for i in range(0, correct_words.__len__()):
                paths = trie.word_exists(correct_words[i])
                if paths is not False:
                    for p in paths:
                        sets[i].add(p)
            ret = sets[0]
            for i in range(1, correct_words.__len__()):
                ret = ret.__or__(sets[i])
            #print(ret)
            return ret_string, ret
