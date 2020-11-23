class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLiknedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, data):
        node = Node(data)
        if self.head is None:
            self.tail = node
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size += 1

    def add_last(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    def remove_first(self):
        if self.head is None:
            print("The list is empty. Nothing to remove")
        else:
            if self.head != self.tail:
                self.head = self.head.next
                self.head.next = None
            else:
                self.head = None
                self.tail = None
            self.size -= 1

    def remove_last(self):
        if self.head is None:
            print("The list is empty. Nothing to remove")
        else:
            if self.head != self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            self.size -= 1

    def insert_before(self, new_data, target_data):
        cur = self.head
        found = False
        while cur:
            if cur.data != target_data:
                cur = cur.next
            else:
                found = True
                break
        if found:
            if target_data == self.head.data:
                self.add_first(new_data)
            else:
                new_node = Node(new_data)
                cur.prev.next = new_node
                new_node.prev = cur.prev
                new_node.next = cur
        else:
            print("Your target data is not in the list")

    def insert_after(self, new_data, target_data):
        current = self.head
        found = False
        while current:
            if current.data != target_data:
                current = current.next
            else:
                found = True
                break
        if found:
            if target_data == self.tail.data:
                self.add_last(new_data)
            else:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
        else:
            print("Your target data is not in the list")

    def call_first(self):
        return self.head.data

    def call_last(self):
        return self.tail.data

    def odd_even_print(self):
        odds = []
        evens = []
        index = 1
        while index <= self.size:
            if index % 2 == 1:
                iteration = 1
                odd = self.head
                while iteration < index:
                    odd = odd.next
                    iteration += 1
                odds.append(odd.data)
            else:
                iteration = 1
                even = self.head
                while iteration < index:
                    even = even.next
                    iteration += 1
                evens.append(even.data)
            index += 1
        print(odds)
        print(evens)