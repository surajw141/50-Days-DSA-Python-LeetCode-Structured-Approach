"""Question :DLL remove 

Create a Doubly Linked List class. Write Instance Methods for this class to be able to

1.remove a node when the node to be removed is given as Input."""


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
 
def linkNodes(node1,node2):
    node1.next = node2
    node2.prev = node1
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def remove(self, node):
        # Time complexity Explanation: 
        # The removal operation in doubly linked list is done in constant time.
        # It does not depend on the number of elements in the list.
        # Hence the time complexity is O(1)
        
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.prev
 
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
 
        node.next = None
        node.prev = None
 
# The time complexity of the remove operation is O(1) since the operation is done in constant time.
def print_list(dll):
    curr = dll.head
    values = []
    while curr:
        values.append(curr.val)
        curr = curr.next
    print(values)


# --- Create nodes ---
a = Node("A")
b = Node("B")
c = Node("C")

# Link nodes together: A <-> B <-> C
linkNodes(a, b)
linkNodes(b, c)

# --- Create the Doubly Linked List manually ---
dll = DoublyLinkedList()
dll.head = a
dll.tail = c

print("Initial list:")
print_list(dll)

# --- Test removing B ---
dll.remove(b)

print("\nList after removing 'B':")
print_list(dll)

# --- Test removing head (A) ---
dll.remove(a)
print("\nList after removing 'A':")
print_list(dll)

# --- Test removing tail (C) ---
dll.remove(c)
print("\nList after removing 'C':")
print_list(dll)