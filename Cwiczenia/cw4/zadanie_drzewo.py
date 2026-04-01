"""
Zadanie polega na tym, że mamy A[n] tablicę, w której jest log n unikalych
wartości. Mamy ją posrtowować w O(nlog(logn))
"""


class Node:
    def __init__(self, value):
        self.val = value
        self.counter: int = 1
        self.right: "None | Node" = None
        self.left: "None | Node" = None


def insert(root: "Node | None", value: int) -> Node:
    if root is None:
        return Node(value)

    if root.val == value:
        root.counter += 1
    elif root.val < value:
        root.right = insert(root.right, value)
    else:
        root.left = insert(root.left, value)
    return root


def reverse_inorder(root: "Node | None", A: list[int], index: int) -> int:
    if root is None:
        return index

    index = reverse_inorder(root.right, A, index)

    for _ in range(root.counter):
        A[index] = root.val
        index += 1

    index = reverse_inorder(root.left, A, index)

    return index


def main_function(A: list[int]) -> None:
    if not A:
        return

    root = None
    for val in A:
        root = insert(root, val)

    reverse_inorder(root, A, 0)
