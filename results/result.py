def get_search_result(ranks: list, ordered_list: list):
    ret = []
    for i in range(len(ranks)):
        if ranks[i][0] != 0:
            ret.append([ordered_list[i], ranks[i]])
    return ret


def sort(result_set: list):
    _quick_sort(result_set, 0, len(result_set)-1)


def _quick_sort(array: list, low: int, high:int):
    if low < high:
        pi = _partition(array, low, high)
        _quick_sort(array, low, pi-1)
        _quick_sort(array, pi+1, high)


def _partition(array: list, low: int, high: int):
    pivot = array[high][1][0]
    ind = low - 1
    for i in range(low, high):
        if array[i][1][0] > pivot:
            ind += 1
            array[ind], array[i] = array[i], array[ind]
    array[ind+1], array[high] = array[high], array[ind+1]
    return ind+1
