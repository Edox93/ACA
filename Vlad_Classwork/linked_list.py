class Node:
    def __init__(self, value):
        self.value = value
        self._next = _next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
            return None

        self.tail._next = node
        self.tail = node

        # add without tail
        '''nxt = self.head
        while nxt._next is not None:
            nxt = nxt._next
        nxt._next = node'''


if __name__ == '__main__':
    llst = LinkedList()
    llst.add(10)
    llst.add(20)
