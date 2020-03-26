from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # because the Queue needs to pop off items at the head and tail
        # and doing it this way allows for no need to reindex the rest of
        # the list as the Queue is updating
        # self.storage = ?
        self.storage = DoublyLinkedList()
        # do I need to pass the Queue self to

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.storage.head is None:
            return None
        else:
            self.storage.remove_from_head()
    # def enqueue(self, value):
    #     self.storage.add_to_head(value)

    # def dequeue(self):
    #     if self.storage.tail is None:
    #         return None
    #     else:
    #         self.storage.remove_from_tail()

    def len(self):
        return self.storage.length
