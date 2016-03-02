

class Stack(object):
    def __init__(self):
        self._stack = []
        self.top = 0

    def empty(self):
        if self.top == 0:
            return True
        else:
            return False

    def push(self, value):
        self._stack.append(value)
        self.top += 1

    def pop(self):
        if self.empty():
            raise IndexError
        else:
            self.top -= 1
            value = self._stack[self.top]
            del self._stack[self.top]
            return value


if __name__ == '__main__':
    s = Stack()
    print s.empty()
    s.push(1)
    s.push(2)
    print s._stack
    print s.pop()
    print s._stack