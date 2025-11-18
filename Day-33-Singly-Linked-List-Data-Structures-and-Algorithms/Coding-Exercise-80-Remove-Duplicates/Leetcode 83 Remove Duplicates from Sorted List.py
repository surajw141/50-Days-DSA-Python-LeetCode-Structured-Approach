"""Question :

delete duplicates - You are given the head of a Sorted Singly Linked list. Write a function that will 
the given head as input, delete all nodes that have a value that is already the value of another node so
that each value appears 1 time only and return the linked list, which is still to be a sorted linked list."""

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

# Creating the list
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node('a')
head.next.next.next.next.next = Node('a')

def removeDupes(head):
    curr = head
    while curr:
        nextDistinctVal = curr.next
        while nextDistinctVal is not None and curr.val == nextDistinctVal.val:
            nextDistinctVal = nextDistinctVal.next
        curr.next = nextDistinctVal
        curr = nextDistinctVal
    return head

def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

new_head = removeDupes(head)
printList(new_head)
