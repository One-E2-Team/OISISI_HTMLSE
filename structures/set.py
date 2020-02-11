class Set:
    def __init__(self):
        self._dict = {}

    def add(self, e):
        self._dict[e] = e

    def discard(self, e):
        try:
            del self._dict[e]
        except KeyError:
            return

    def __contains__(self, e):
        return e in self._dict

    def __len__(self):
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
        ret = Set()
        for e in list(self._dict.keys()) + list(other.__get_dict().keys()):
            ret.add(e)
        return ret

    def __and__(self, other):  # cross section
        ret = Set()
        for e in list(self._dict.keys()) + list(other.__get_dict().keys()):
            if e in self._dict and e in other:
                ret.add(e)
        return ret

    def __sub__(self, other):  # difference/complement
        ret = Set()
        for e in self._dict:
            if e not in other.__get_dict():
                ret.add(e)
        return ret

    def __str__(self):
        return str(list(self._dict.keys()))
