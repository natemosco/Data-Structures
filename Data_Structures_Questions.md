Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

2. What is the runtime complexity of `dequeue`?

3. What is the runtime complexity of `len`?

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1.  What is the runtime complexity of `ListNode.insert_after`?
    o(n)
2.  What is the runtime complexity of `ListNode.insert_before`?
    o(n)
3.  What is the runtime complexity of `ListNode.delete`?
    o(n)
4.  What is the runtime complexity of `DoublyLinkedList.add_to_head`?
    o(n)
5.  What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
    o(n)
6.  What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
    o(n)
7.  What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
    o(n)
8.  What is the runtime complexity of `DoublyLinkedList.move_to_front`?
    o(n)
9.  What is the runtime complexity of `DoublyLinkedList.move_to_end`?
    o(n)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
    o(n)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    generally the delete is going to work better because once at the correct node to delete the operation simply needs to change the pointer values for the previous and next to point to eachother and then there is data-garbage-collection later on

        with splice you select a portion of the array to remove
        this means a loop must be performed over the remaining values after the deleted portion to reassign the indeces
        optionally if the splice is inserting a greater number of indeces than was deleted you need a new place in memory to create a new array and loop over all the values to correctly assign modified indeces.
