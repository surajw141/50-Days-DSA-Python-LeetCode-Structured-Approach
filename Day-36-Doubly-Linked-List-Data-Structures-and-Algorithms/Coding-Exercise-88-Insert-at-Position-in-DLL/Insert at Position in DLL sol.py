"""Question :DLL remove all, insert at position

Create a Doubly Linked List class. Write Instance Methods for this class to be able to

Done in Prev exercise -

1. remove all the nodes in the doubly linked list which have their value equal to a given value.

Let's do the below as part of this exercise -

2.Insert a node at a desired position (node and position are given). The Linked List is 0 indexed.
If given node is a node existing in the Linked List shift it to the desired position."""




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
        curr = self.head
        while curr:
            temp = curr
            curr = curr.next
            if temp.val == value:
                self.remove(temp)
 
    def insertPosition(self, position, node):
        # Time complexity Explanation:
        # This method involves traversing the list until the desired position or the end of the list is reached.
        # Therefore, the time complexity is linear O(n), where n is the number of nodes in the list.
 
        curr = self.head
        counter = 0
        while curr != None and counter != position:
            curr = curr.next
            counter += 1
        if curr != None:
            self.insertB(curr, node)
        else:
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                self.remove(node)
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
                
    def __str__(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " <-> ".join(vals)

# Create nodes
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(2)
n5 = Node(5)

# Create doubly linked list
dll = DoublyLinkedList()
dll.head = n1
dll.tail = n3
linkNodes(n1, n2)
linkNodes(n2, n3)

print("Initial List:", dll)

# Insert node at position
dll.insertPosition(1, n5)
print("After inserting 5 at position 1:", dll)

# Remove all nodes with value 2
dll.allNodesValueRemove(2)
print("After removing all 2s:", dll)
