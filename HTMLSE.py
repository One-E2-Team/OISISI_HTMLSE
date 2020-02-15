import time

import parse
import search
import results

UI_UX = True

if __name__ == '__main__':
    top_dir = input("Enter path (relative or absolute) to dataset (ENTER -> test-skup): ")
    if top_dir == '':
        top_dir = 'test-skup'
    data = parse.PopulateStructures(top_dir, ui_ux=UI_UX)  # populated data how stored in data.set and data.graph
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
        query = input('Enter one word, multiple words separated by space or /'
                      'word1 OPERATOR word2(OPERATOR can be AND, OR, NOT).\nEnter \'q\' for exit.\nInput: ')
        query = query.strip()
        query = query.lower()
        if query.lower() == 'q':
            exit(0)
        elif query == '':
            print('Empty string passed, use \'q\' for exit. Reloading.')
            continue
        elif search.validate_query(query):
            print('\nExecuting search by query (hard_result_set, broad_positive_res_set)...')
            start = time.time()
            positive_query, hard_result_set, broad_positive_res_set = search.execute_query(query, data.trie)
            end = time.time()
            print('Done in {0} seconds.'.format(end - start))
            print('Performing Ranked Search...')
            start = time.time()
            ranks = search.get_ranks(pagerank, data.graph, hard_result_set, broad_positive_res_set,
                                     data.html_files, len(positive_query.split(' ')))
            end = time.time()
            print('Done in {0} seconds.'.format(end - start))
            print('Compiling result set...')
            start = time.time()
            result_set = results.get_search_result(ranks, data.html_files)
            end = time.time()
            print('Done in {0} seconds.'.format(end - start))
            result = results.sort(result_set)
            for r in result_set:
                print(r)
        else:
            print('Invalid search query. Reloading.')
            continue
        # TODO etc.
