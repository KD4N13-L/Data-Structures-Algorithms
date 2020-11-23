class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LListDeque:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insert_first(self, obj):
        node = Node(obj, self.first)
        self.first = node
        if self.last is None:
            self.last = node
        self.size += 1

    def insert_last(self, obj):
        node = Node(obj, None)
        if self.last is None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    def remove_first(self):
        if self.size == 0:
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

    def remove_last(self):
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

    def call_first(self):
        if self.size == 0:
            print("Linked list is empty")
            return
        print(self.first.data)
        return self.first

    def call_last(self):
        if self.size == 0:
            print("Linked list is empty")
            return
        print(self.last.data)
        return self.last

    def print(self):
        if self.size == 0:
            print("Linked list is empty")
            return
        itr = self.first
        while itr:
            print(itr.data)
            itr = itr.next

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def size(self):
        return self.size

    def clear(self):
        self.first = None
        self.last = None
        self.size = 0
