class Set:
    """
    Using internal python set() was forbidden. Many optimization would be possible otherwise (especially in &, |, -
    and get_list methods)
    """
    def __init__(self):
        self._dict = {}

    def add(self, e):
        """
        Method adds element to SET in O(1)
        :param e: element to be added to set
        :return: None
        """
        self._dict[e] = e

    def discard(self, e):
        try:
            del self._dict[e]
        except KeyError:
            return

    def __contains__(self, e):
        """
        Method returns boolean type indicating if a specific object is present in Set, in O(1), abs worst case is O(n).
        :param e: tested element
        :return: True/False
        """
        return e in self._dict

    def __len__(self):
        """"
        Length O(1)
        """
        return len(self._dict)

    def __iter__(self):
        return iter(self._dict.copy())

    def remove(self, e):
        del self._dict[e]

    def pop(self):
        self._dict.popitem()

    def clear(self):
        del self._dict
        self._dict = {}

    def __get_dict(self):
        return self._dict.copy()

    def __or__(self, other):  # union
        """
        Performs union of two sets in O(n) where n is the sum of number of elements of both sets.
        :param other: second set
        :return: resulting Set (union)
        """
        ret = Set()
        for e in list(self._dict.keys()) + list(other.__get_dict().keys()):
            ret.add(e)
        return ret

    def __and__(self, other):  # cross section
        """
        Performs cross-section of two Sets in O(n).
        :param other:  second Set
        :return: resulting Set (cross-section)
        """
        ret = Set()
        for e in list(self._dict.keys()) + list(other.__get_dict().keys()):
            if e in self._dict and e in other:
                ret.add(e)
        return ret

    def __sub__(self, other):  # difference/complement
        """
        Performs difference (complement) of two Sets in O(n).
        :param other: second Set
        :return: resulting Set (complement)
        """
        ret = Set()
        for e in self._dict:
            if e not in other.__get_dict():
                ret.add(e)
        return ret

    def __str__(self):
        return str(list(self._dict.keys()))

    def get_list(self):
        """
        O(n)
        :return: List of Set elements.
        """
        return list(self._dict.keys())
