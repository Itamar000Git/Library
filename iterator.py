class iterator(object):
    def __init__(self, some_books_list):
        self.iterable = some_books_list
        self.index = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        else:
            next = self.iterable[self.index]
            self.index += 1
            return next
