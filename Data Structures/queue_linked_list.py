from abc import ABC, abstractmethod


class QueueADT(ABC):
    @abstractmethod
    def enqueue(self, obj):
        pass

    @abstractmethod
    def dequeue(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def call_first(self):
        pass


class Node:

    def __init__(self, data, next_node, previous=None):
        self.data = data
        self.next = next_node
        self.previous = previous


class LListQueue(QueueADT):

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def dequeue(self):
        if self.first is None:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        self.first = self.first.next
        tmp.next = None
        self.size -= 1

    def enqueue(self, obj):
        node = Node(obj, None)
        if self.last is None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    def size(self):
        return self.size

    def call_first(self):
        return self.first

    def clear(self):
        self.first = None
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False