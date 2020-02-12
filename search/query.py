from structures.set import Set

def validate_query(query):
    if query == 'AND' or query == 'NOT' or query == 'OR':
        return False
    elif ' ' not in query:
        return True
    else:
        if 'AND' not in query and 'OR' not in query and 'NOT' not in query:
            return True
        parts = query.split(' ')
        if len(parts) != 3:
            return False
        elif parts[0] == 'AND' or parts[0] == 'NOT' or parts[0] == 'OR' or parts[2] == 'AND' or parts[2] == 'NOT' or parts[2] == 'OR':
            return False
        elif parts[1] != 'AND' and parts[1] != 'NOT' and parts[1] != 'OR':
            return False
        return True


def execute_query(query, trie):
    flag = None
    words = []
    if ' ' not in query:
        paths = trie.word_exists(query)
        if paths is not False:
            ret = Set()
            for p in paths:
                ret.add(p)
            return ret
        else:
            print("'" + query + "' doesn't exist in trie")
            return None
    elif 'AND' not in query and 'OR' not in query and 'NOT' not in query:
        flag = 'or'
        words = query.split(' ')
    else:
        parts = query.split(' ')
        if parts[1] == 'AND':
            flag = 'and'
            words.append(parts[0])
            words.append(parts[2])
        elif parts[1] == 'NOT':
            flag = 'not'
            words.append(parts[0])
            words.append(parts[2])
        elif parts[1] == 'OR':
            flag = 'or'
            words.append(parts[0])
            words.append(parts[2])
    if flag is not None:
        correct_words = []
        for w in words:
            if w != '':
                correct_words.append(w)
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
            return ret
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
            return ret
