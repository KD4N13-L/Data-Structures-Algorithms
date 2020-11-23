class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class HashSet():
    def __init__(self, capacity):
        self._hashtable = [None] * capacity
        self._capacity = capacity
        self._size = 0

    def __iter__(self):
        for e in self._hashtable:
            if e is not None:
                self._elem = e

                break
        return self

    def __next__(self):
        if self._elem is None:
            raise StopIteration

        tmp = self._elem
        if self._elem.next is not None:
            self._elem = self._elem.next
        else:
            index = self._hash(self._elem.data)
            self._elem = None
            for i in range(index + 1, len(self._hashtable)):
                if self._hashtable[i] is not None:
                    self._elem = self._hashtable[i]
                    break
        return tmp.data

    def levelOrderIterator(self):
        for i in range(self._size):
            isYield = False
            for e in self._hashtable:
                for j in range(i):
                    if e is not None:
                        e = e.next
                if e is not None:
                    yield e.data
                    isYield = True
            if not isYield:
                break

    def _hash(self, element):
        return ord(element[0]) % self._capacity

    def add(self, element):
        index = self._hash(element)
        if self._hashtable[index] is None:
            self._hashtable[index] = Node(element)
        else:
            n = Node(element, self._hashtable[index])
            self._hashtable[index] = n
        self._size += 1

    def contains(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        while n is not None:
            if n.data == element:
                return True
            n = n.next
        return False

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def remove(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        p = None
        while n is not None:
            if n.data == element:
                if p is None:
                    self._hashtable[index] = n.next
                else:
                    p.next = n.next
                n.next = None
                self._size -= 1
                return n
            p = n
            n = n.next
        return None

    def size(self):
        return self._size

    def print(self):
        print("printing hashset elements")
        for e in self._hashtable:
            while e is not None:
                print(e.data)
                e = e.next

    def intersection(self, s):
        newSet = HashSet(100)
        for e in self._hashtable:
            while e is not None:
                if s.contains(e.data):
                    newSet.add(e.data)
                    e = e.next
                    return newSet

    def intersection_update(self, s):
        for e in self._hashtable:
            p = None
            while e is not None:
                r = None
                if not s.contains(e.data):
                    r = e
                if r is not None:
                    if p is None:
                        self._hashtable[self._hash(r.data)] = e.next
                    else:
                        p.next = e.next
                        e = e.next
                        self._size -= 1
                else:
                    p = e
                    e = e.next

    def union_update(self, s):
        for element in s._hashtable:
            while element is not None:
                if not self.contains(element.data):
                    self.add(element.data)
                element = element.next


def union(set1, set2):
    for e in set1._hashtable:
        while e is not None:
            if not set2.contains(e.data):
                set2.add(e.data)
            e = e.next
    return set2
