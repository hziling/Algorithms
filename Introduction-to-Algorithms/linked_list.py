

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = self.prev = None


class List(object):
    def __init__(self):
        self.head = None

    def search(self, k):
        x = self.head
        while x != None and x.value != k:
            x = x.next
        return x

    def insert(self, node):
        node.next = self.head
        if self.head != None:
            self.head.prev = node
        self.head = node
        node.prev = None

    def delete(self, node):
        if node.prev != None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next != None:
            node.next.prev = node.prev


if __name__ == '__main__':
    lst = List()

    lst.insert(Node(5))
    lst.insert(Node(2))
    lst.insert(Node(1))
    lst.insert(Node(5))

    lst.delete(lst.search(5))
    lst.delete(lst.search(2))
