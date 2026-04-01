# DRZEWO BST


class Node:
    def __init__(self, value):
        self.val: int = value
        self.left: "None | Node" = None
        self.parent: "Node | None" = None
        self.right: "None | Node" = None


def insert(root: Node, value: int) -> None:
    if root.val < value:
        if root.right is not None:
            insert(root.right, value)
        else:
            nowy_wezel = Node(value)
            nowy_wezel.parent = root
            root.right = nowy_wezel
    else:
        if root.left is not None:
            insert(root.left, value)
        else:
            nowy_wezel = Node(value)
            nowy_wezel.parent = root
            root.left = nowy_wezel


def max_BST(root: Node) -> int:
    cur = root
    while cur.right is not None:
        cur = cur.right
    return cur.val


def min_BST(root: Node) -> int:
    cur = root
    while cur.left is not None:
        cur = cur.left
    return cur.val


def poprzednik(p: Node) -> "int | None":
    if p.left is not None:
        return max_BST(p.left)

    obecny = p
    rodzic = p.parent

    while rodzic is not None and obecny == rodzic.left:
        obecny = rodzic
        rodzic = rodzic.parent

    if rodzic is not None:
        return rodzic.val
    return None


def nastepnik(p: Node) -> "int | None":
    if p.right is not None:
        return min_BST(p.right)

    obecny = p
    rodzic = p.parent

    while rodzic is not None and obecny == rodzic.right:
        obecny = rodzic
        rodzic = rodzic.parent

    if rodzic is not None:
        return rodzic.val
    return None
