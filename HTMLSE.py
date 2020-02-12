import parse
import search

if __name__ == '__main__':
    top_dir = input("Enter path (relative or absolute) to dataset (ENTER -> test-skup): ")
    if top_dir == '':
        top_dir = 'test-skup'
    data = parse.PopulateStructures(top_dir)  # populated data how stored in data.set and data.graph
    while True:
        print('\n\n---------- HTMLSE Search Section ----------\n')
        query = input('Enter one word, multiple words separated by space or /'
                      'word1 OPERATOR word2(OPERATOR can be AND, OR, NOT).\nEnter \'q\' for exit.\nInput: ')
        if query.lower() == 'q':
            exit(0)
        elif query == '':
            print('Empty string passed, use \'q\' for exit. Reloading.')
            continue
        elif search.validate_query(query):
            # TODO call _ = search.execute_query(query,...) (returns #resulting_set needed for search)
            # let it fall trough
            search.execute_query(query, data.trie) # delete this after proper implementation
            pass
        else:
            print('Invalid search query. Reloading.')
            continue
        # TODO perform #ranked_search
        # TODO etc.
