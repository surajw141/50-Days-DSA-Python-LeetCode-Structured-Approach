"""Question :

Reverse SLL- You are given the head of a Singly Linked list. Write a function that will take the given head as input,
reverse the Linked List and return the new head of the reversed Linked List.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
# Creating the list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
 
 
def reverseLinkedList(head):
    # Time Complexity Explanation: 
    # The function contains a while loop that traverses the linked list once, so the time complexity is O(n) 
    # where n is the number of nodes in the linked list.
    
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev
 
# The Time complexity of this function is O(n), where n is the number of nodes in the list.
 
reverseLinkedList(head)