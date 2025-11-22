"""Question :Construct Stack (using Linked List)

(you can do it with either SLL or DLL. Here let's try to do it with SLL)

Implement a Stack:

1.Using an Array
2.with a Stack class using a Linked list

One should be able to add to the stack and remove from the stack following the LIFO property.

Note-

Remove - after removing , return the value of the removed node"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class StackLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
 
    def addAtBeginning(self, value):
        # Time Complexity Explanation:
        # Adding an element at the beginning of a linked list is an O(1) operation,
        # because it requires a constant amount of work: creating a new node, and changing a couple of references.
        node = Node(value)
        if not self.first:
            self.first = node
            self.last = node
        else:
            temp = self.first
            self.first = node
            self.first.next = temp
        self.size += 1
        return self
 
    def removeFromBeginning(self):
        # Time Complexity Explanation:
        # Removing an element from the beginning of a linked list is an O(1) operation,
        # because it requires a constant amount of work: changing a couple of references, and optionally deleting a node.
        if not self.first:
            return None
        temp = self.first
        self.first = self.first.next
        self.size -= 1
        if self.size == 0:
            self.last = None
        return temp.value
 
# Final time complexity: For both adding and removing from the beginning, the time complexity is O(1).

# Create a stack
stack = StackLinkedList()

# Push values
stack.addAtBeginning(10)
stack.addAtBeginning(20)
stack.addAtBeginning(30)

print("Stack size after pushes:", stack.size)

# Pop values (LIFO order)
print("Popped:", stack.removeFromBeginning())  # Should remove 30
print("Popped:", stack.removeFromBeginning())  # Should remove 20
print("Popped:", stack.removeFromBeginning())  # Should remove 10

# Try popping from empty stack
print("Popped from empty stack:", stack.removeFromBeginning())

print("Final size:", stack.size)
