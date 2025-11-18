"""Question :

Construct Singly Linked List - Design a Singly linked list class that has a head and tail. Every node is to have two attributes: value:  the value of the current node, and next: a pointer to the next node. The linked list is to be 0-indexed. The class should support the following:

SinglyLinkedList() Initializes the SinglyLinkedList object.

get(index) Get the node at the index passed. If the index is invalid, return -1.

addAtHead(value)- Add a node of given value before the first element of the linked list. Return the SLL

addAtTail(value) -  Add a node of given value at the last element of the linked list. Return the SLL

addAtIndex(index, value) Add a node of given value before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, don’t insert the node(return a message 'invalid index' ). Return SLL once done.

deleteAtIndex(index) Delete the indexth node in the linked list, if the index is valid, else nothing happens.Return deleted node"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
 
        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1
        return current
 
    # Time Complexity: O(1) as we perform constant time operations
    # Space Complexity: O(1) as no additional space is required
    def addAtHead(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
 
    # Time Complexity: O(1) as we perform constant time operations
    # Space Complexity: O(1) as no additional space is required
    def addAtTail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
 
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def addAtIndex(self, index, value):
        if index < 0 or index > self.size:
            return 'invalid index'
        if index == self.size:
            return self.addAtTail(value)
        if index == 0:
            return self.addAtHead(value)
        node = Node(value)
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = node
        node.next = temp
        self.size += 1
 
    # Time Complexity: O(n) as we might traverse through the entire list in the worst case
    # Space Complexity: O(1) as no additional space is required
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return 'invalid index'
        if index == 0:
            temp = self.head
            self.head = temp.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            return temp.value
        if index == self.size - 1:
            old_tail = self.tail
            new_tail = self.get(index - 1)
            self.tail = new_tail
            new_tail.next = None
            self.size -= 1
            return old_tail.value
        prev = self.get(index - 1)
        deleted_node = prev.next
        prev.next = deleted_node.next
        self.size -= 1
        return deleted_node.value
    
    
    
# use this function
# Create list
sll = SinglyLinkedList()

# Add at head
sll.addAtHead(10)   # [10]
sll.addAtHead(20)   # [20, 10]

# Add at tail
sll.addAtTail(30)   # [20, 10, 30]
sll.addAtTail(40)   # [20, 10, 30, 40]

# Insert at index
sll.addAtIndex(2, 25)  # [20, 10, 25, 30, 40]

# Delete at index
deleted = sll.deleteAtIndex(3)  # deletes 30 → [20, 10, 25, 40]

print("Deleted:", deleted)

# Print the list to verify
curr = sll.head
print("List:", end=" ")
while curr:
    print(curr.value, end=" -> ")
    curr = curr.next
print("None")

print("Size:", sll.size)
print("Head:", sll.head.value)
print("Tail:", sll.tail.value)
