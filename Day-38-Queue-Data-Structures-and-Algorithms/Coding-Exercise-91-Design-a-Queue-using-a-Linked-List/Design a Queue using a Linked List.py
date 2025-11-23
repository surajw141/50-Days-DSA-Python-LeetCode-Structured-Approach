"""Question :Construct Queue

Implement a Queue:

- with a Queue class using a Linked list

One should be able to add to the queue and remove from the queue following the FIFO property."""

# Implementation 1: Queue using an Array
 
queue = []  # array to hold queue elements
value = 1
queue.append(value)  # add value to end of queue, O(1)
queue.pop(0)  # remove value from start of queue, O(n)
 
# The overall time complexity of enqueue operation is O(1), and the dequeue operation is O(n).
#Space complexity is O(1) for enqueue and dequeue

# Implementation 2: Queue using a Linked List
 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
 
    def enqueue(self, value):
        # Time Complexity Explanation:
        # Creating a new node and updating the last pointer has a time complexity of O(1)
        node = Node(value)
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1
 
    def dequeue(self):
        # Time Complexity Explanation:
        # Updating the first pointer and reducing the size variable has a time complexity of O(1)
        if not self.first:
            return None
        temp = self.first
        self.first = self.first.next
        self.size -= 1
        if self.size == 0:
            self.last = None
        return temp.value
 
# Final Time Complexity: The overall time complexity of both enqueue and dequeue operation is O(1).
#Space complexity is O(1) for enqueue and dequeue


# Using your QueueLinkedList implementation

# Create a queue
q = QueueLinkedList()

# Enqueue elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("After enqueues:")
print("First:", q.first.value)    # Expect 10
print("Last:", q.last.value)      # Expect 30
print("Size:", q.size)            # Expect 3

# Dequeue elements
print("\nDequeuing:")
print(q.dequeue())  # Expect 10
print(q.dequeue())  # Expect 20
print(q.dequeue())  # Expect 30

# Queue should now be empty
print("\nAfter all dequeues:")
print("First:", q.first)   # Expect None
print("Last:", q.last)     # Expect None
print("Size:", q.size)     # Expect 0
