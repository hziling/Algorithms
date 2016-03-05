

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print x.value
        inorder_tree_walk(x.right)


def tree_select(x, k):
    if x is None:
        return None
    if x.value == k:
        return x

    if k < x.value:
        return tree_select(x.left, k)
    else:
        return tree_select(x.right, k)


def iterative_tree_search(x, k):
    while x is not None and k != x.value:
        if k < x.value:
            x = x.left
        else:
            x = x.right

    return x


def tree_minimum(x):
    if x is None:
        return None

    while x.left is not None:
        x = x.left

    return x


def tree_maximux(x):
    if x is None:
        return None

    while x.right is not None:
        x = x.right

    return x


def tree_successor(x):
    if x.right is not None:
        return tree_minimum(x.right)

    y = x.parent
    while y is not None and x == y.right:
        x = y
        y = y.parent

    return y


def tree_insert(T, x):
    if T.root is None:
        T.root = x

    y = T.root
    while y is not None:
        z = y
        if x.value < y.value:
            y = y.left
        else:
            y = y.right

    x.parent = z
    if x.value < z.value:
        z.left = x
    else:
        z.right = x


def transplant(T, u, v):
    if u.parent is None:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v

    if v is not None:
        v.parent = u.parent


def tree_delete(T, z):
    if z.left is None:
        transplant(T, z, z.right)
    elif z.right is None:
        transplant(T, z, z.left)
    else:
        y = tree_minimum(z)
        if y.parent != z:
            transplant(T, y, y.right)
            y.right = z.right
            y.right.parent = y

        transplant(T, z, y)
        y.left = z.left
        y.left.parent = y