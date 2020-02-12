def validate_query(query):
    # TODO
    return True


def execute_query(query, trie):
    # TODO proper implementation
    paths = trie.word_exists(query)
    if paths is not False:
        for p in paths:
            print(p)
    else:
        print("'" + query + "' doesn't exist in trie")
