#coding:utf-8


# 翻转二叉树
def reverse_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left
    reverse_tree(root.left)
    reverse_tree(root.right)
    return root