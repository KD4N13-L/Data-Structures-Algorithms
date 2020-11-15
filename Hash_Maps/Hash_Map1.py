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
                self._index = i
                break
        return self

    def __next__(self):
        if self._index >= len(self._hashtable):
            raise StopIteration

        tmpInd = self._index
        self._index = len(self._hashtable)
        for i in range(tmpInd + 1, len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i
                break
        return self._hashtable[tmpInd].value

    def _hash(self, element):
        #return hash(element) % self._capacity
        return ord(element[0]) % self._capacity

    def put(self, key, value):
        index = self._hash(key)
        print(index)
        for i in range (index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    oldValue = self._hashtable[i].value
                    self._hashtable[i].value = value
                    return oldValue
            else:
                self._hashtable[index] = Entry(key, value)
                self._size += 1
                return None
                #TODO resize and add the key,value pair

    def get(self, key):
        index = self._hash(key)
        for i in range (index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    return self._hashtable[i].value
            else:
                return None

    def hasKey(self, element):
        pass

    def remove(self, element):
        pass

    def size(self):
        return self._size

    def print(self):
        print("printing hashset elements")
        for e in self._hashtable:
            while (e != None):
                print(e.data)
                e = e.next

HM = HashMap()
print(HM.put("a", "arbitrary"))
print(HM.put("a", "anything"))
print(HM.put("aa", "Aaron"))
print(HM.put("ac", "actor"))
print(HM.put("b", "barbeque"))
print(HM.put("d", "doll"))
for elem in HM:
    print(elem)