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
            if self._hashtable[i] != None:
                self._index = i
                break
        return self

    def __next__(self):
        if self._index >= len(self._hashtable):
            raise StopIteration
        tmpInd = self._index
        self._index = len(self._hashtable)
        for i in range(tmpInd + 1, len(self._hashtable)):
            if self._hashtable[i] != None:
                self._index = i
                break

    def _hash(self, element):
        return ord(element[0]) % self._capacity

    def put(self, key, value):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    oldValue = self._hashtable[i].value
                    self._hashtable[i].value = value
                    return oldValue
            else:
                self._hashtable[i] = Entry(key, value)
                self._size += 1
                return None

    def get(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                if key == self._hashtable[i].key:
                    return self._hashtable[i].value
            else:
                return None

    def hasKey(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if self._hashtable[i] != None:
                if key == self._hashtable[i].key:
                    return True
            else:
                return False

    def remove(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if self._hashtable[i] != None:
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


addressBook = HashMap()
addressBook.put("Artak", {"fullName": "Artak Zakaryan",
                          "phoneNumber": "094444441"})
addressBook.put("Ani", {"fullName": "Ani Aslanyan",
                        "phoneNumber": "094444442"})
addressBook.put("Karen", {"fullName": "Karen Kocharyan",
                          "phoneNumber": "094444445"})
addressBook.put("Zaven", {"fullName": "Zaven Hakobyan",
                          "phoneNumber": "094444447"})
addressBook.put("Gohar", {"fullName": "Gohar Vardanyan",
                          "phoneNumber": "094444454"})

print(addressBook.hasKey("Gohar"))
print(addressBook.hasKey("David"))

addressBook.remove("Gohar")
print(addressBook.hasKey("Gohar"))

print("Daniel Kurghinyan: A09190522")