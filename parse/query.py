import parse

def enter_query(trie):
    query = input("\nEnter one word, multiple words separated by space or word1 OPERATOR word2(OPERATOR can be AND, OR, NOT)\nInput: ")
    #TODO proper implementation
    if ' ' in query:
        pass
    else:
        paths = trie.word_exists(query)
        if paths != False:
            for p in paths:
                print(p)
        else:
            print("'" + query + "' doesn't exist in trie")