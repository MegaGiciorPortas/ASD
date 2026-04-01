class Node:
    def __init__(self, value):
        self.val = value
        self.next: "None | Node" = None


# wstawianie do posortowanej listy odsyłaczowej
def insert(head: Node, value) -> Node:
    new_node = Node(value)
    if head is None:
        return new_node

    prev: "None | Node" = None
    cur = head
    while cur is not None:
        if cur.val < value:
            prev = cur
            cur = cur.next
        else:
            if prev is None:
                new_node.next = head
                return new_node
            else:
                new_node.next = cur
                prev.next = new_node
                return head
    if prev is not None:
        prev.next = new_node
    return head


# usuwanie maksymalnego elementu
def remove_max(head) -> tuple[Node | None, Node | None]:
    if head is None:
        return (None, None)

    value = head.val
    cur, prev = head, None

    while cur.next is not None:
        if cur.next.val > value:
            value = cur.next.val
            prev = cur
        cur = cur.next

    node = Node(value)
    if prev is None:  # head jest najwieksze
        return (head.next, node)
    prev.next = prev.next.next
    return (head, node)


# odwrócić liste odsyłaczową
def reverse_linked_list(first):
    cur = first
    if first is None:
        return None
    if cur.next is None:
        return first

    prev = None
    while cur is not None:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev
