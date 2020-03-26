from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        return None if self.storage.tail is None else self.storage.remove_from_tail()

    def len(self):
        return self.storage.length
