"""Question :DLL remove all with specified value

Create a Doubly Linked List class. Write Instance Methods for this class to be able to

1. remove all the nodes in the doubly linked list which have their value equal to a given value.

"""
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
 
def linkNodes(node1, node2):
    node1.next = node2
    node2.prev = node1
 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    def remove(self, node):
        # Time complexity Explanation: 
        # The removal operation in a doubly linked list is done in constant time.
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
        # The insertion operation in a doubly linked list is also done in constant time.
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
 
    def allNodesValueRemove(self, value):
        # Time complexity Explanation:
        # This method involves traversing the entire linked list.
        # Therefore, the time complexity is linear O(n), 
        # where n is the number of nodes in the list.
 
        curr = self.head
        while curr:
            temp = curr
            curr = curr.next
            if temp.val == value:
                self.remove(temp)
 
# The time complexity of the remove operation and insertB operation is O(1), allNodesValueRemove operation is O(n). 


# Helper function to print the list
def print_list(dll):
    curr = dll.head
    vals = []
    while curr:
        vals.append(curr.val)
        curr = curr.next
    print(vals)


# Create nodes
n1 = Node(5)
n2 = Node(3)
n3 = Node(5)
n4 = Node(7)
n5 = Node(5)

# Manually link nodes into a DLL
dll = DoublyLinkedList()
dll.head = n1
dll.tail = n5

linkNodes(n1, n2)
linkNodes(n2, n3)
linkNodes(n3, n4)
linkNodes(n4, n5)

print("Before removal:")
print_list(dll)

# Remove all nodes with value = 5
dll.allNodesValueRemove(5)

print("After removal of value 5:")
print_list(dll)
