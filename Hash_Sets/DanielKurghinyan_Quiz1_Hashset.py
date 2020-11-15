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
            if (e != None):
                self._elem = e

                break
        return self

    def __next__(self):
        if self._elem == None:
            raise StopIteration

        tmp = self._elem
        if self._elem.next != None:
            self._elem = self._elem.next
        else:
            index = self._hash(self._elem.data)
            self._elem = None
            for i in range(index + 1, len(self._hashtable)):
                if self._hashtable[i] != None:
                    self._elem = self._hashtable[i]
                    break
        return tmp.data

    def levelOrderIterator(self):
        for i in range(self._size):
            isYield = False
            for e in self._hashtable:
                for j in range(i):
                    if (e != None):
                        e = e.next
                if (e != None):
                    yield e.data
                    isYield = True
            if (isYield == False):
                break

    def levelOrderIteratorWithQueue(self):
        yield None

    def _hash(self, element):
        return ord(element[0]) % self._capacity

    def add(self, element):
        index = self._hash(element)
        if (self._hashtable[index] == None):
            self._hashtable[index] = Node(element)
        else:
            n = Node(element, self._hashtable[index])
            self._hashtable[index] = n
        self._size += 1

    def contains(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        while (n != None):
            if (n.data == element):
                return True
            n = n.next
        return False

    def remove(self, element):
        index = self._hash(element)
        n = self._hashtable[index]
        p = None
        while (n != None):
            if (n.data == element):
                if (p == None):
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
            while (e != None):
                print(e.data)
                e = e.next

    def union_update(self, s):
        for element in s._hashtable:
            while element != None:
                if not self.contains(element.data):
                    self.add(element.data)
                element = element.next


def union(set1, set2):
    for e in set1._hashtable:
        while (e != None):
            if not set2.contains(e.data):
                set2.add(e.data)
            e = e.next
    return set2


HS2 = HashSet(100)
HS2.add("x")
HS2.add("y")
HS2.add("z")
HS2.add("xx")
HS2.add("yy")
HS2.add("zz")

HS1 = HashSet(100)
HS1.add("13")
HS1.add("84")
HS1.add("41")
HS1.add("75")
HS1.add("xx")

HS3 = union(HS1, HS2)
HS3.print()

HS2.union_update(HS1)
HS2.print()

for elem in HS2.levelOrderIteratorWithQueue():
    print(elem)

print("Daniel Kurghinyan: A09190522")