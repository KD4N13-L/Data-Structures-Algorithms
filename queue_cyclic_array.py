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
    def condition(self):
        pass

    @abstractmethod
    def size(self):
        pass


class ArrayQueue(QueueADT):
    def __init__(self, capacity):
        i = 0
        self.queue = []
        while i <= capacity-1:
            self.queue.append(0)
            i += 1
        self.first = 0
        self.size = 0
        self.number_of_recizes = 1
        self.max_current_size = capacity
        self.max_resize_number = 4

    def size(self):
        return self.size

    def condition(self):
        print("Head:", self.first)
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
        self.max_current_size = self.max_current_size*2
        i = 0
        while i < self.max_current_size:
            self.queue.append(0)
            i += 1
        l = 0
        while l <= self.size:
            self.queue[l] = temp[(self.first + l) % self.size]
            l += 1
        self.first = 0

    def clear(self):
        self.first = 0
        self.size = 0

    def enqueue(self, obj):
        if self.size == self.max_current_size:
            if self.number_of_recizes > self.max_resize_number:
                print ("The queue is full. Cannot resize further. Please try later.")
            else:
                self.resize()
                self.queue[(self.first + self.size) % self.max_current_size] = obj
                self.size += 1
        else:
            self.queue[(self.first + self.size) % self.max_current_size] = obj
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            return "The queue is empty."
        self.first = (self.first + 1) % self.max_current_size
        self.size -= 1


# ------------------------------------------------------------------------------


line = ArrayQueue(3)

i = 0
while i < 50:
    line.enqueue(i)
    i += 1
print()
for i in line.queue:
    print(i)

