class Entry():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap():
    def __init__(self):
        self._capacity = 26
        self._hashtable = [None] * self._capacity * 10
        self._size = 0

    def __iter__(self):
        for i in range(len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i;
                break
        return self

    def __next__(self):
        if self._index >= len(self._hashtable):
            raise StopIteration
        tmpInd = self._index
        self._index = len(self._hashtable)
        for i in range(tmpInd + 1, len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i;
                break

        return self._hashtable[tmpInd].value

    def hash(self, element):
        return ord(element[0]) % self._capacity

    def add(self, key, value):

        index = self.hash(key)

        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    oldValue = self._hashtable[i].value
                    self._hashtable[i].value = value
                    return oldValue
            else:
                self._hashtable[index] = Entry(key, value)
                self._size += 1
                return None
        # TODO resize and add the key,value pair

    def get(self, key):
        index = self.hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    print(self._hashtable[i].value)
            else:
                return None

    def haskey(self, key):
        index = self.hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    return True
            else:
                return False

    def remove(self, key):
        index = self.hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    self._hashtable[i].key = None
                    self._hashtable[i].value = None
            else:
                return None

    def size(self):
        return self._size

    def print(self):
        print("printing hashset elements")
        for e in self._hashtable:
            while (e != None):
                print(e.data)
                e = e.next




HM = HashMap()
print(HM.add('a', 'arbitrary'))
print(HM.add('a', 'anything'))
print(HM.add('aa', 'Aaron'))
print(HM.add('ac', 'actor'))
print(HM.add('b', 'barbeque'))
print(HM.add('d', 'doll'))
print(HM.remove('b'))
for elem in HM:
    print(elem)
print()
print(HM.get('d'))
print()
print(HM.haskey('d'))
print(HM.haskey('h'))
print(HM.hasValue('doll'))
print(HM.hasValue('nothing'))


