class Data(object):
    def __init__(self, *args):
        self._data = list(args)

    def __iter__(self):
        return DataIter(self)

class DataIter(object):
    def __init__(self, data):
        self._index = 0
        self._data = data._data

    def next(self):
        if self._index >= len(self._data):
            raise StopIteration()
        d = self._data[self._index]
        self._index += 1
        return d