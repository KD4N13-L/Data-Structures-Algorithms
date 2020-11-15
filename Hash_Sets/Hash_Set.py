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
        if (self._elem.next != None):
            self._elem = self._elem.next
        else:
            index = self._hash(self._elem.data)
            self._elem = None
            for i in range(index + 1, len(self._hashtable)):
                if (self._hashtable[i] != None):
                    self._elem = self._hashtable[i]
                    break
        return tmp.data

    def _hash(self, element):
        return hash(element) % self._capacity

    def add(self, element):
        index = self._hash(element)
        if (self._hashtable[index] == None):
            self._hashtable[index] = Node(element)
        else:
            n = Node(element, self._hashtable[index])
            self._hashtable[index] = n
        self._size += 1
        # TODO add only unique values to the set

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

    def union(self, s):
        for e in self._hashtable:
            while (e !=None):
                if (not s.contains(e.data)):
                    s.add(e.data)
                e = e.next
        return s

    def union_update(self, s):
        for element in s._hashtable:
            while element != None:
                if not self.contains(element.data):
                    self.add(element.data)
                element = element.next


    def print(self):
        print("printing hashset elements")
        for e in self._hashtable:
            while (e != None):
                print(e.data)
                e = e.next



HS = HashSet(100)
HS.add("a")
HS.add("b")
HS.add(1)
HS.add(3)
HS.add(101)
HS1 = HashSet(100)
HS1.add("a")
HS1.add("b")
HS1.add(2)
HS1.add(3)
#print()

#HS3 = HS.intersection(HS1)
#print(HS3.size())
#HS3.print()
#HS.intersection_update(HS1)
#HS.print()

#HS4 = HS.union(HS1)
#HS4.print()
HS.union_update(HS1)
HS.print()
print(HS.hasKey(1))
print(HS.hasKey(101))

for elem in HS.levelOrderIterator():
    print(elem)