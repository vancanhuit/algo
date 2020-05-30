from .linked_list import SinglyLinkedList


class Stack:
    def __init__(self):
        self._storage = SinglyLinkedList()

    def is_empty(self):
        return self._storage.is_empty()

    def push(self, value):
        self._storage.insert_first(value)

    def pop(self):
        self._storage.remove_first()

    def top(self):
        if self.is_empty():
            return None
        return self._storage._head._value


class Queue:
    def __init__(self):
        self._storage = SinglyLinkedList()

    def is_empty(self):
        return self._storage.is_empty()

    def enqueue(self, value):
        self._storage.insert_last(value)

    def dequeue(self):
        self._storage.remove_first()

    def peek(self):
        if self.is_empty():
            return None
        return self._storage._head._value
