import time

import parse
import results
import search
import search.advanced

UI_UX = True
DEBUG = False


def rank_and_display():
    if DEBUG:
        print('\nPerforming Ranked Search...')
    start_rs = time.time()
    ranks = search.get_ranks(pagerank, data.graph, hard_result_set, broad_positive_res_set,
                             data.html_files, 0 if positive_query == '' else len(positive_query.split(' ')))
    end_rs = time.time()
    if DEBUG:
        print('Done in {0} seconds.'.format(end_rs - start_rs))
        print('\nCompiling result set...')
    start_crs = time.time()
    result = results.get_search_result(ranks, data.html_files)
    end_crs = time.time()
    if DEBUG:
        print('Done in {0} seconds.'.format(end_crs - start_crs))
    if len(result) == 0:
        print(('\nYour search - {0} - did not match any documents.'
               '\n\nSuggestions:'
               '\n\n\t- Make sure that all words are spelled correctly.'
               '\n\t- Try different keywords.'
               '\n\t- Try more general keywords.'
               '\n\nAnd yes, we are fully copy-pasting Google.').format(query))
        return
    if DEBUG:
        print('\nSorting results...')
    start_sr = time.time()
    results.sort(result)
    end_sr = time.time()
    if DEBUG:
        print('Done in {0} seconds.'.format(end_sr - start_sr))
    search_time = end_sq - start_sq + end_rs - start_rs + end_crs - start_crs + end_sr - start_sr
    results.paginate(result, search_time, rank_details=DEBUG)


if __name__ == '__main__':
    while True:
        top_dir = input("Enter path (relative or absolute) to dataset (ENTER -> test-skup): ")
        if top_dir == '':
            top_dir = 'test-skup'
        data = parse.PopulateStructures(top_dir, ui_ux=UI_UX)
        if len(data.html_files) != 0:
            break
    if DEBUG:
        print('\nConstructing adjacent(+ constraint sum of each column equals 1) matrix for PageRank...')
    start_adj = time.time()
    pr_matrix = search.construct_pr_adj_matrix(data.graph, data.html_files)
    end_adj = time.time()
    if DEBUG:
        print('Done in {0} seconds.'.format(end_adj - start_adj))
        print('\nCalculating PageRank...')
    start_pr = time.time()
    pagerank = search.pagerank(pr_matrix)
    end_pr = time.time()
    if DEBUG:
        print('Done in {0} seconds.'.format(end_pr - start_pr))
    print('\nPageRank calculation done in {0}'.format(end_adj - start_adj + end_pr - start_pr))
    search_mode = input('\nEnter advanced search mode? [y/N]')
    if search_mode.strip().lower() == 'y':
        advanced_search_mode = True
    else:
        advanced_search_mode = False
    while True:
        print('\n\n---------- HTMLSE Search Section ----------\n')
        if not advanced_search_mode:
            query = input('Enter one word, multiple words separated by space or '
                          'word1 OPERATOR word2 (OPERATOR can be AND, OR, NOT).\nEnter \'q\' for exit.\nInput: ')
        else:
            query = input('Enter advanced query (&& is AND, || is OR, ! is NOT). You may use parentheses in '
                          'expressions.\nEnter \'q\' for exit.\nInput: ')
        query = query.lower()
        if query == 'q':
            exit(0)
        elif query.strip() == '':
            print('Empty string passed, use \'q\' for exit. Reloading.')
            continue
        elif not advanced_search_mode and search.validate_query(query):
            if DEBUG:
                print('\nExecuting search by query (hard_result_set, broad_positive_res_set)...')
            start_sq = time.time()
            positive_query, hard_result_set, broad_positive_res_set = search.execute_query(query, data.trie)
            end_sq = time.time()
            if DEBUG:
                print('Done in {0} seconds.'.format(end_sq - start_sq))
            rank_and_display()
        elif advanced_search_mode:
            if DEBUG:
                print('\nParsing advanced mode query...')
            start_p = time.time()
            parsed_query = search.advanced.parse(query)
            end_p = time.time()
            if DEBUG:
                print('Done in {0} seconds.'.format(end_p - start_p))
            if parsed_query is not None:
                if DEBUG:
                    print('\nExecuting search by query (hard_result_set, broad_positive_res_set)...')
                start_sq = time.time()
                positive_query, hard_result_set, broad_positive_res_set = search.advanced.eval_query(parsed_query, data)
                end_sq = time.time()
                if DEBUG:
                    print('Done in {0} seconds.'.format(end_sq - start_sq))
                rank_and_display()
            else:
                print('Invalid search query. Reloading.')
        else:
            print('Invalid search query. Reloading.')
