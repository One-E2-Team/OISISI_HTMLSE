import parse
import search

UI_UX = True

if __name__ == '__main__':
    top_dir = input("Enter path (relative or absolute) to dataset (ENTER -> test-skup): ")
    if top_dir == '':
        top_dir = 'test-skup'
    data = parse.PopulateStructures(top_dir, ui_ux=UI_UX)  # populated data how stored in data.set and data.graph
    while True:
        print('\n\n---------- HTMLSE Search Section ----------\n')
        query = input('Enter one word, multiple words separated by space or /'
                      'word1 OPERATOR word2(OPERATOR can be AND, OR, NOT).\nEnter \'q\' for exit.\nInput: ')
        query = query.strip()
        if query.lower() == 'q':
            exit(0)
        elif query == '':
            print('Empty string passed, use \'q\' for exit. Reloading.')
            continue
        elif search.validate_query(query):
            result_set = search.execute_query(query, data.trie)
            print(result_set)
        else:
            print('Invalid search query. Reloading.')
            continue
        # TODO perform #ranked_search
        # TODO etc.
