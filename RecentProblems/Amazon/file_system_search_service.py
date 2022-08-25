from abc import ABC, abstractmethod
from enum import Enum


class File:
    def __init__(self, name,size, is_file):
        self.name = name
        self.is_file = is_file
        self.size = size
        self.children = []


class Operator(Enum):
    Equal, GreaterThan, GreaterThanEqual, LessThan, LessThanEqual = 0, 1, 2, 3, 4


class Specification(ABC):
    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class AndSpecification(Specification):
    def __init__(self, first: Specification, second: Specification):
        self.first = first
        self.second = second

    def is_satisfied_by(self, candidate):
        return self.first.is_satisfied_by(candidate) and self.second.is_satisfied_by(candidate)


class NameFilter(Specification):
    def __init__(self, name):
        self.name = name

    def is_satisfied_by(self, f: File):
        return f.name == self.name


class SizeFilter(Specification):
    def __init__(self, size, op: Operator):
        self.size = size
        self.op = op

    def is_satisfied_by(self, f: File):
        if self.op == Operator.Equal:
            return f.size == self.size
        return False


class FileSearchService:
    def __init__(self, files):
        self.files = files

    def search(self, search:Specification):
        res = []
        for f in self.files:
            if search.is_satisfied_by(f):
                res.append(f.name)
        return res

class FileSystem:
    root = File('home', 10, False)
    f1 = File('abc.txt', 2, False)
    f2 = File('bcd.txt', 5, False)
    f3 = File('def.txt', 10, False)
    f4 = File('abc.txt', 10, False)

    root.children += [f1, f2,f3,f4]
    name_filter = NameFilter('abc.txt')
    size_filter = SizeFilter(10, Operator.Equal)
    search = name_filter.__and__(size_filter)

    files = [f1, f2,f3,f4]
    fs = FileSearchService(files)
    print(fs.search(name_filter))
    print(fs.search(size_filter))
    print(fs.search(search))