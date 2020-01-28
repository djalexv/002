# class MyIterator:
#     def __init__(self, iterable):
#         self.index = 0
#         self.iterable = iterable
#
#     def __next__(self):
#         if self.index < len(self.iterable):
#             self.index += 1
#             return self.iterable[self.index - 1]
#         raise StopIteration

class MyList:
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.iterable[self.index - 1]
        raise StopIteration


# l = MyList('qwertyuiop')
l = [1, 2, 3, 4, 5]

it = l.__iter__()
iit = it.__iter__()
c = iter(l)

print(it)
print(iit)
print(c)

# print(it.__next__())
# l = MyList([1, 2, 3, 4, 5])
# for i in l:
#     print(i)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))
print(next(c))

print(next(c))
print(next(it))