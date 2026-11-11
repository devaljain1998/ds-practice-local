"""
Doubly Linked List: Fundamentals Practice (Part 1)

Implement every method marked TODO, then run:  python dll_practice.py

Rules:
  - Use dummy (sentinel) head and tail nodes.
  - No Python list/deque as the underlying storage (to_list helpers are
    allowed to *return* a list, but must walk the nodes).
  - Don't use any built-in reverse. Reverse by rewiring pointers.
  - Invalid indices are silently ignored (or return -1 for get).
"""


class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        node = self.head
        len = 0
        while node is not None:
            len += 1
            node = node.next
        return len

    def add_at_head(self, val):
        """Insert a new node right after the head sentinel. O(1)."""
        if self.head is None:
            self.head = Node(val)
        else:
            newnode = Node(val)
            newnode.next=self.head
            self.head.prev = newnode
            self.head = newnode

    def add_at_tail(self, val):
        """Insert a new node right before the tail sentinel. O(1)."""
        if self.head is None:
            return self.add_at_head(val)

        node = self.head
        while node.next is not None:
            node = node.next
        newnode = Node(val)
        node.next = newnode
        newnode.prev = node


    def add_at_index(self, index, val):
        """
        Insert so the new node ends up at position `index` (0-based).
        index == len(self) appends. index < 0 or index > len(self): do nothing.
        """
        length = len(self)
        if index < 0 or index > length:
            return
        if index == 0:
            return self.add_at_head(val)
        if index == length:
            return self.add_at_tail(val)

        node = self.head
        for _ in range(1, index+1):
            node = node.next
        newnode = Node(val)
        node.prev.next, newnode.prev = newnode, node.prev
        node.prev, newnode.next = newnode, node


    def get(self, index):
        """Return value at `index`, or -1 if the index is invalid."""
        length = len(self)
        if index < 0 or index >= length:
            return -1
        if not self.head:
            return -1
        node = self.head
        for _ in range(1, index+1):
            node = node.next
        return node.val
        

    def delete_at_index(self, index):
        """Remove the node at `index`. Invalid index: do nothing."""
        length = len(self)
        if index < 0 or index > length:
            return
        if index == 0:
            return self._delete_head()
        if index == length-1:
            return self._delete_tail()

        node = self.head
        for _ in range(1, index+1):
            node = node.next
        prevnode, nextnode = node.prev, node.next
        prevnode.next, nextnode.prev = nextnode, prevnode
        print('--')

    def _delete_head(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        nxt_node = self.head.next
        nxt_node.prev = None
        self.head.next = None
        self.head = nxt_node

    def _delete_tail(self):
        if not self.head:
            return
        node = self.head
        while node.next is not None:
            node = node.next
        prevnode = node.prev
        prevnode.next = None
        node.prev = None

    def to_list(self):
        """Walk head -> tail and return the values as a Python list."""
        if not self.head:
            return []
        res = []
        node = self.head
        while node is not None:
            res.append(node.val)
            node = node.next
        return res

    def to_list_reversed(self):
        return self.to_list()[::-1]

    def reverse(self):
        """Reverse the list in place by swapping prev/next pointers. O(n)."""
        # TODO
        pass


# ---------------------------- TESTS (don't edit) ----------------------------
def check(dll, expected, label):
    fwd, bwd = dll.to_list(), dll.to_list_reversed()
    assert fwd == expected, f"[{label}] forward: expected {expected}, got {fwd}"
    assert bwd == expected[::-1], f"[{label}] backward: expected {expected[::-1]}, got {bwd}"
    assert len(dll) == len(expected), f"[{label}] len: expected {len(expected)}, got {len(dll)}"


def run_tests():
    d = DoublyLinkedList()
    check(d, [], "empty")
    assert d.get(0) == -1

    d.add_at_head(2); check(d, [2], "head on empty")
    d.add_at_head(1); check(d, [1, 2], "head")
    d.add_at_tail(3); check(d, [1, 2, 3], "tail")
    d.add_at_tail(4); check(d, [1, 2, 3, 4], "tail 2")

    d.add_at_index(0, 0); check(d, [0, 1, 2, 3, 4], "index 0")
    d.add_at_index(5, 5); check(d, [0, 1, 2, 3, 4, 5], "index == len")
    d.add_at_index(3, 99); check(d, [0, 1, 2, 99, 3, 4, 5], "index middle")
    d.add_at_index(50, 7); check(d, [0, 1, 2, 99, 3, 4, 5], "index too big -> ignored")
    d.add_at_index(-1, 7); check(d, [0, 1, 2, 99, 3, 4, 5], "negative index -> ignored")

    assert d.get(3) == 99 and d.get(6) == 5 and d.get(7) == -1 and d.get(-1) == -1

    d.delete_at_index(3); check(d, [0, 1, 2, 3, 4, 5], "delete middle")
    d.delete_at_index(0); check(d, [1, 2, 3, 4, 5], "delete head")
    d.delete_at_index(4); check(d, [1, 2, 3, 4], "delete tail")
    d.delete_at_index(10); check(d, [1, 2, 3, 4], "delete invalid -> ignored")

    # d.reverse(); check(d, [4, 3, 2, 1], "reverse")
    # d.reverse(); check(d, [1, 2, 3, 4], "reverse back")

    for _ in range(4):
        d.delete_at_index(0)
    check(d, [], "deleted everything")
    d.reverse(); check(d, [], "reverse empty")
    d.add_at_tail(42); d.reverse(); check(d, [42], "reverse single")
    d.add_at_head(41); check(d, [41, 42], "reuse after emptying")

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()