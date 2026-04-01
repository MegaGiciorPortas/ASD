# suma elementów w drzewie ale w stałej złożoności pamięciowej
class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.parent = None
        self.val = value


def min_BST(root: Node) -> Node:
    cur = root

    while cur.left is not None:
        cur = cur.left
    return cur


def nastepnik(wezel: Node) -> Node | None:
    if wezel.right is not None:
        return min_BST(wezel.right)

    cur = wezel
    rodzic = cur.parent

    while rodzic is not None and rodzic.right == cur:
        cur = rodzic
        rodzic = cur.parent

    if rodzic is not None:
        return rodzic
    return None


def suma_drzewa(root: Node) -> int:
    suma = 0

    cur = min_BST(root)
    while cur is not None:
        suma += cur.val
        cur = nastepnik(cur)

    return suma
