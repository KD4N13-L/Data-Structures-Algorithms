from abc import ABC, abstractmethod


class StackADT(ABC):

    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def top(self):
        pass

    @abstractmethod
    def empty(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass


class Node:

    def __init__(self, data, next_node, previous=None):
        self.data = data
        self.next = next_node
        self.previous = previous


class LListStack(StackADT):

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, data):
        node = Node(data, None)
        if self.last is None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        while tmp.next != self.last:
            tmp = tmp.next
        tmp.next = None
        self.last = tmp
        self.size -= 1

    def size(self):
        return self.size

    def top(self):
        return self.last

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def empty(self):
        self.first = None
        self.last = None
        self.size = 0