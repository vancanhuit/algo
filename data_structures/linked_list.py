class SinglyLinkedListNode:
    def __init__(self, value):
        self._value = value
        self._next = None


class DoublyLinkedListNode(SinglyLinkedListNode):
    def __init__(self, value):
        super().__init__(value)
        self._prev = None


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    def insert_first(self, value):
        node = SinglyLinkedListNode(value)
        if self.is_empty():
            self._head = node
            self._tail = self._head
        else:
            node._next = self._head
            self._head = node

    def insert_last(self, value):
        node = SinglyLinkedListNode(value)
        if self.is_empty():
            self._head = node
            self._tail = self._head
        else:
            self._tail._next = node
            self._tail = node

    def remove_first(self):
        if self.is_empty():
            return
        self._head = self._head._next
        if self.is_empty():
            self._tail = None

    def remove_last(self):
        if self.is_empty():
            return
        if self._head == self._tail:
            self._head = None
            self._tail = None
            return
        slow = self._head
        fast = slow._next
        while fast._next:
            slow = slow._next
            fast = fast._next
        self._tail = slow
        self._tail._next = None

    def is_empty(self):
        return self._head is None

    def __str__(self):
        elems = []
        current = self._head
        while current:
            elems.append(current._value)
            current = current._next
        return '->'.join(map(str, elems))


class DoublyLinkedList(SinglyLinkedList):
    def insert_first(self, value):
        node = DoublyLinkedListNode(value)
        if self.is_empty():
            self._head = node
            self._tail = self._head
        else:
            node._next = self._head
            self._head._prev = node
            self._head = node

    def insert_last(self, value):
        node = DoublyLinkedListNode(value)
        if self.is_empty():
            self._head = node
            self._tail = self._head
        else:
            self._tail._next = node
            node._prev = self._tail
            self._tail = node

    def remove_first(self):
        if self.is_empty():
            return
        self._head = self._head._next
        if self.is_empty():
            self._tail = None
            return
        self._head._prev = None

    def remove_last(self):
        if self.is_empty():
            return
        self._tail = self._tail._prev
        if self._tail is None:
            self._head = None
            return
        self._tail._next = None

    def reverse(self):
        current = self._tail
        elems = []
        while current:
            elems.append(current._value)
            current = current._prev
        return '<-'.join(map(str, elems))
