

class Queue(object):
    def __init__(self, size):
        self._queue = [None for i in range(size)]
        self.head = self.tail = 0
        self.size = size

    def enqueue(self, value):
        self._queue[self.tail] = value
        if self.tail == self.size:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.head == self.tail:
            raise ValueError

        value = self._queue[self.head]
        if self.head == self.size:
            self.head = 1
        else:
            self.head += 1
        return value


if __name__ == '__main__':
    q = Queue(5)

    q.enqueue(1)
    q.enqueue(2)
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()