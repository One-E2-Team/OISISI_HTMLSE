def paginate(result: list, time: float, rank_details=False):
    print('\n{0} results ({1} seconds)\n'.format(len(result), time))
    N = input('Enter pagination number, \'c\' to cancel printing job '
              'and 0 or anything else to print everything all at once:')
    if N.lower() == 'c':
        return
    else:
        try:
            N = int(N)
        except ValueError:
            N = 0
    curr = 0
    printed = 0
    while curr != len(result):
        printed += 1
        print('{0}. {1}\tRANK: {2}'.format(curr+1, result[curr][0], result[curr][1][0]))
        if rank_details:
            print('\tPageRank:{0} IRank: {1} [IRank1: {2}, IRank2: {3}]'.format(result[curr][1][1],
                                                                                result[curr][1][2],
                                                                                result[curr][1][3],
                                                                                result[curr][1][4],))
        curr += 1
        if printed == N:
            printed = 0
            do = input(('{0} links left. Use ENTER(RETURN) to display next page, \'c\' to cancel this job.\n'
                        'Enter a number to change the number of links being displayed in one page '
                        '(0 to print the rest).').format(len(result) - curr))
            if do == '':
                continue
            elif do.lower() == 'c':
                break
            else:
                try:
                    do = int(do)
                except ValueError:
                    print('Invalid input, canceling currently active job.')
                    break
                else:
                    N = do
    print('-------------------------------------------')
