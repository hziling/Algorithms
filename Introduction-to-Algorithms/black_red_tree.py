

def left_rotate(T, x):
    y = x.right
    x.right = y.left
    if y.left is not None:
        y.left.parent = x

    y.parent = x.parent
    if x.parent == T.root:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.left = x
    x.parent = y



def right_rotate(T, x):
    y = x.left
    x.left = y.right
    if y.right is not None:
        y.right.parent = x

    y.parent = x.parent
    if x.parent is None:
        T.root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y

    y.right = x
    x.parent = y


# insert
def rb_insert(T, z):
    x = T.root
    y = None

    while x is not None:
        y = x
        if z < x.value:
            x = x.left
        else:
            x = x.right

    z.parent = y
    if y == None:
        T.root = z
    elif z.value < y.value:
        y.left = z
    else:
        y.right = z

    z.color = 'RED'
    rb_insert_fixup(T, z)


def rb_insert_fixup(T, z):
    while z.parent.color == 'RED':
        if z.parent == z.parent.parent.left:
            y = z.parent.parent.right
            if y.color == 'RED':
                z.parent.color = 'BLACK'
                y.color = 'BLACK'
                z.parent.parent.color = 'RED'
                z = z.parent.parent
            else:
                if z == z.parent.right:
                    z = z.parent
                    left_rotate(T, z)
                z.parent.color = 'BLACK'
                z.parent.parent.color = 'RED'
                right_rotate(T, z.parent.parent)
        else:
            # right and left exchanged
            pass

    T.root.color = 'BLACK'





