import time

import parse
import search
import results

UI_UX = True
DEBUG = True

if __name__ == '__main__':
    while True:
        top_dir = input("Enter path (relative or absolute) to dataset (ENTER -> test-skup): ")
        if top_dir == '':
            top_dir = 'test-skup'
        data = parse.PopulateStructures(top_dir, ui_ux=UI_UX)  # populated data how stored in data.set and data.graph
        if len(data.html_files) != 0:
            break
    print('\nConstructing adjacent(+ constraint sum of each column equals 1) matrix for PageRank...')
    start = time.time()
    pr_matrix = search.construct_pr_adj_matrix(data.graph, data.html_files)
    end = time.time()
    print('Done in {0} seconds.'.format(end - start))
    print('\nCalculating PageRank...')
    start = time.time()
    pagerank = search.pagerank(pr_matrix)
    end = time.time()
    print('Done in {0} seconds.'.format(end - start))
    while True:
        print('\n\n---------- HTMLSE Search Section ----------\n')
        query = input('Enter one word, multiple words separated by space or '
                      'word1 OPERATOR word2(OPERATOR can be AND, OR, NOT).\nEnter \'q\' for exit.\nInput: ')
        query = query.lower()
        if query == 'q':
            exit(0)
        elif query.strip() == '':
            print('Empty string passed, use \'q\' for exit. Reloading.')
            continue
        elif search.validate_query(query):
            print('\nExecuting search by query (hard_result_set, broad_positive_res_set)...')
            start = time.time()
            positive_query, hard_result_set, broad_positive_res_set = search.execute_query(query, data.trie)
            end = time.time()
            print('Done in {0} seconds.'.format(end - start))
            print('\nPerforming Ranked Search...')
            start = time.time()
            ranks = search.get_ranks(pagerank, data.graph, hard_result_set, broad_positive_res_set,
                                     data.html_files, len(positive_query.split(' ')))
            end = time.time()
            print('Done in {0} seconds.'.format(end - start))
            print('\nCompiling result set...')
            start = time.time()
            result = results.get_search_result(ranks, data.html_files)
            end = time.time()
            print('Done in {0} seconds.'.format(end - start))
            if len(result) == 0:
                print(('Your search - {0} - did not match any documents.'
                       '\n\nSuggestions:'
                       '\n\n\t- Make sure that all words are spelled correctly.'
                       '\n\t- Try different keywords.'
                       '\n\t- Try more general keywords.'
                       '\n\nAnd yes, we are fully copy-pasting Google.').format(query))
                continue
            print('\nSorting results...')
            start = time.time()
            results.sort(result)
            end = time.time()
            print('Done in {0} seconds.'.format(end - start))
            results.paginate(result, rank_details=True)
        else:
            print('Invalid search query. Reloading.')
            continue
