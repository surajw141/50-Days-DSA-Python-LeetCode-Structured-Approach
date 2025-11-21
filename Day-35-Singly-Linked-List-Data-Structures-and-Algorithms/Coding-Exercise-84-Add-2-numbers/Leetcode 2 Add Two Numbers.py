"""Question :

Add 2 numbers-You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list. You may assume the two numbers do
not contain any leading zero, except the number 0 itself. 0<=Node value<=9"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
 
    def addAtTail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return self
 
def add2Numbers(l1, l2):
    # Time Complexity Explanation:
    # The while loop runs at most 'max(n, m)' times where 'n' and 'm' are the lengths of l1 and l2 respectively.
    # Thus, the time complexity is O(max(n, m)).
    
    carryForward = 0
    results = LinkedList()
    while l1 or l2 or carryForward:
        l1Value = l1.value if l1 else 0
        l2Value = l2.value if l2 else 0
        sum = (l1Value + l2Value + carryForward)
        nodeValueInResult = sum % 10
        results.addAtTail(nodeValueInResult)
        carryForward = sum // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return results
 
# The time complexity of this function is O(max(n, m)) where n and m are the lengths of l1 and l2 respectively.

# Helper function to create a linked list from a list of digits
def createLinkedList(values):
    ll = LinkedList()
    for v in values:
        ll.addAtTail(v)
    return ll

# Create input linked lists
l1 = createLinkedList([2, 4, 3])  # Represents number 342
l2 = createLinkedList([5, 6, 4])  # Represents number 465

# Run the function
result = add2Numbers(l1.head, l2.head)

# Helper to print the linked list
def printList(head):
    curr = head
    while curr:
        print(curr.value, end=" -> " if curr.next else "")
        curr = curr.next
    print()

printList(result.head)
