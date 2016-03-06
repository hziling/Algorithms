

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class List(object):
    def __init__(self):
        self.head = None

    def reverse_linked_list(self):
        if self.head is not None:
            p1 = self.head

            p2 = p1.next
            p3 = p1
            p3.next = None

            while p2 is not None:
                p1 = p2
                p2 = p2.next
                p1.next = p3
                p3 = p1

            self.head = p1

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            p = self.head
            while p.next is not None:
                p = p.next

            p.next = node

    def show(self):
        p = self.head
        while p is not None:
            print p.value
            p = p.next


if __name__ == '__main__':
    lst = List()
    lst.insert(Node(1))
    lst.insert(Node(2))
    lst.insert(Node(3))
    lst.insert(Node(4))
    lst.show()
    lst.reverse_linked_list()
    lst.show()