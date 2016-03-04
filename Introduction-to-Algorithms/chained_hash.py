

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class HashTable(object):
    TABLE_SIZE = 11

    def __init__(self):
        self.table = [None for i in range(self.TABLE_SIZE)]

    @classmethod
    def _hash(cls, key):
        if not isinstance(key, basestring):
            raise ValueError('key must be a string.')

        code = reduce(lambda code, x: code * 128 + ord(x), list(key), 0)
        return code % cls.TABLE_SIZE

    def insert(self, key, value):
        new_node = Node(key, value)
        index = self._hash(new_node.key)

        node = self.table[index]
        if node is not None:
            while node.next is not None and node.key != new_node.key:
                node = node.next
            if node.key == new_node.key:
                node.value = value
            else:
                node.next = new_node
                new_node.prev = node
        else:
            self.table[index] = new_node

    def delete(self, key):
        index = self._hash(key)

        node = self.table[index]
        if node is None:
            raise IndexError('Not exist.')

        while node.key != key and node.next is not None:
            node = node.next

        if node.key == key:
            if node.prev is not None:
                node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev
            if node.prev is None:
                self.table[index] = None

            del node
        else:
            raise IndexError('Not exist.')

    def search(self, key):
        index = self._hash(key)

        node = self.table[index]
        if node is None:
            raise IndexError('Not exist.')

        while node.key != key and node.next is not None:
            node = node.next

        if node.key == key:
            return node.value
        else:
            raise IndexError('Not exist.')


if __name__ == '__main__':
    hash_table = HashTable()

    hash_table.insert('key1', 'value1')
    hash_table.insert('key2', '2')
    hash_table.insert('key2', 2)
    hash_table.insert('key3', [1, 2, 3])

    print hash_table.search('key1')
    print hash_table.search('key2')
    print hash_table.search('key3')
    # print hash_table.search('key4')

    hash_table.delete('key1')
    print hash_table.search('key1')
