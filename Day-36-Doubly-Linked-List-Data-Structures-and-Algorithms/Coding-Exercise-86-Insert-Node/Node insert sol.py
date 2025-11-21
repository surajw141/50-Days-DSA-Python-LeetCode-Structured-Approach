"""Question :DLL remove insert

Create a Doubly Linked List class. Write Instance Methods for this class to be able to

Done in Prev Question -

1.remove a node when the node to be removed is given as Input.

Do as part of this exercise -

2. insert a node before a particular node(both the node to be inserted and the node before which the insertion is to happen will be given as input). If the node to be inserted is

-part of the linked list then shift its place to the desired location

-a new node, then insert the new node at the place desired."""

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
 
    def insertB(self, nodePosition, nodeInsert):
        # Time complexity Explanation: 
        # Both the removal and insertion operations in doubly linked list are done in constant time.
        # It does not depend on the number of elements in the list.
        # Hence the time complexity is O(1)
 
        if self.head == nodeInsert and self.tail == nodeInsert:
            return
 
        self.remove(nodeInsert)
 
        nodeInsert.prev = nodePosition.prev
        nodeInsert.next = nodePosition
 
        if nodePosition == self.head:
            self.head = nodeInsert
        else:
            nodePosition.prev.next = nodeInsert
 
        nodePosition.prev = nodeInsert
 
# The time complexity of the remove and insertB operations is O(1) since the operation is done in constant time.


# ==== Creating nodes ====
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

# ==== Create list: A <-> B <-> C ====
dll = DoublyLinkedList()
dll.head = a
dll.tail = c
linkNodes(a, b)
linkNodes(b, c)

# ==== TEST 1: remove(B) ====
dll.remove(b)

# Expected: A <-> C
print("After removing B:")
n = dll.head
while n:
    print(n.val, end=" ")
    n = n.next
print("\nhead:", dll.head.val, "tail:", dll.tail.val)

# ==== TEST 2: insertB(C, A) => insert A before C (A was at head already) ====
dll.insertB(c, a)

# Expected: A <-> C (same as before since A is already before C)
print("\nAfter insertB(C, A):")
n = dll.head
while n:
    print(n.val, end=" ")
    n = n.next
print("\nhead:", dll.head.val, "tail:", dll.tail.val)

# ==== TEST 3: insert new node D before C ====
dll.insertB(c, d)

# Expected: A <-> D <-> C
print("\nAfter insertB(C, D):")
n = dll.head
while n:
    print(n.val, end=" ")
    n = n.next
print("\nhead:", dll.head.val, "tail:", dll.tail.val)


