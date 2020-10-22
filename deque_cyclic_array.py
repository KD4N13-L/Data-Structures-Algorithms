from abc import ABC, abstractmethod


class DequeADT(ABC):
    @abstractmethod
    def add_first(self, obj):
        pass

    @abstractmethod
    def add_last(self, obj):
        pass

    @abstractmethod
    def remove_first(self):
        pass

    @abstractmethod
    def remove_last(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def condition(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def call_first(self):
        pass

    @abstractmethod
    def call_last(self):
        pass


class ArrayDeque(DequeADT):
    def __init__(self, capacity):
        self.first = 0
        self.last = capacity - 1
        i = 0
        self.queue = []
        while i <= self.last:
            self.queue.append(None)
            i += 1
        self.size = 0
        self.number_of_recizes = 1
        self.max_current_size = capacity
        self.max_resize_number = 4

    def size(self):
        return self.size

    def condition(self):
        print("First Index:", self.first)
        print("Last Index:", self.last)
        print("Size:", self.size)
        print("Number of Resizes:", self.number_of_recizes)
        print("Max Current Size:", self.max_current_size)

    def is_empty(self):
        return self.size == 0

    def resize(self):
        print("Resizing...")
        self.number_of_recizes += 1
        temp = self.queue
        self.queue = []
        self.max_current_size = self.max_current_size * 2
        i = 0
        while i < self.max_current_size:
            self.queue.append(None)
            i += 1
        l = 0
        while l <= self.size:
            self.queue[l] = temp[(self.first + l) % self.size]
            l += 1
        self.first = 0
        self.last = self.size - 1

    def clear(self):
        self.first = 0
        self.size = 0

    def add_first(self, obj):
        if self.size == self.max_current_size:
            if self.number_of_recizes > self.max_resize_number:
                print("The queue is full. Cannot resize further. Please try later.")
            else:
                self.resize()
                self.queue[(self.first - 1) % self.max_current_size] = obj
                self.size += 1
                self.first = (self.first - 1) % self.max_current_size
        else:
            self.queue[(self.first - 1) % self.max_current_size] = obj
            self.size += 1
            self.first = (self.first - 1) % self.max_current_size

    def add_last(self, obj):
        if self.size == self.max_current_size:
            if self.number_of_recizes > self.max_resize_number:
                print("The queue is full. Cannot resize further. Please try later.")
            else:
                self.resize()
                self.last = (self.last + 1) % self.max_current_size
                self.queue[self.last] = obj
                self.size += 1
        else:
            self.last = (self.last + 1) % self.max_current_size
            self.queue[self.last] = obj
            self.size += 1

    def remove_first(self):
        if self.size == 0:
            return "The queue is empty."
        self.first = (self.first + 1) % self.max_current_size
        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return "The queue is empty."
        self.last = (self.last - 1) % self.max_current_size
        self.size -= 1

    def call_first(self):
        return self.queue[self.first]

    def call_last(self):
        return self.queue[self.last]
# ------------------------------------------------------------------------------


line = ArrayDeque(4)

line.add_first(2)
line.add_last(3)
line.add_first(1)
line.remove_first()
print("First Value:", line.call_first())
print("Last Value:", line.call_last())
line.add_first(4)
line.add_last(5)
line.add_last(6)
print()
line.condition()
print("First Value:", line.call_first())
print("Last Value:", line.call_last())
for i in line.queue:
    print(i)