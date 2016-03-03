

class Stack(object):
    def __init__(self, size):
        self._stack = [None for i in range(size)]
        self.top = 0
        self.size = size

    def empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def push(self, value):
        if self.full():
            raise ValueError
        self._stack[self.top] = value
        self.top += 1

    def pop(self):
        if self.empty():
            raise IndexError
        else:
            self.top -= 1
            value = self._stack[self.top]
            del self._stack[self.top]
            return value

    def show(self):
        return [v for v in self._stack if v is not None]


if __name__ == '__main__':
    s = Stack(10)
    print s.empty()
    s.push(1)
    s.push(2)
    print s.show()
    print s.pop()
    print s.show()