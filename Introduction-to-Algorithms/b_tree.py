

def disk_read(x, c):
    pass


def b_tree_search(x, k):
    i = 1
    while i <= x.n and k > x.key:
        i = i + 1
    if i <= x.n and k == x.key:
        return (x, i)
    elif x.leaf:
        return None
    else:
        disk_read(x, c)
        return b_tree_search(x.c, k)
