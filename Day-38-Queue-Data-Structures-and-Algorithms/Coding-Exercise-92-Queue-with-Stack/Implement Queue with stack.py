"""Question :Implement Queue with Stack

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions
of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

push(val) Pushes element val to the back of the queue.

pop() Removes the element from the front of the queue and returns it.

peek() Returns the element at the front of the queue.

empty() Returns true if the queue is empty, false otherwise.

Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively.
You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
Follow-up: Implement the queue such that each operation is amortized O(1) time complexity. 
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer."""

 
# Time Complexity Analysis:
# push operation - O(1) - push operation on stack
# pop operation - Amortized O(1) - pop operation on stack
# peek operation - Amortized O(1) - pop operation on stack
# empty operation - O(1) - checking length of stack
 
# Space Complexity Analysis:
# Space complexity for this approach is O(n) because we are storing all the queue elements in the stacks.
# Where n is the number of elements in the queue.
 
class MyQueue:
 
    def __init__(self):
        self.inStack = []
        self.outStack = []
 
    def push(self, val):
        # Time complexity is O(1) as we are simply adding an element to the stack.
        self.inStack.append(val)
 
    def pop(self):
        # Time complexity is amortized O(1) because in the worst case we will move all elements from inStack to outStack
        # But this happens only when outStack is empty, and after this operation next several pop operations will take O(1) time.
        # Therefore, for n pop operations, overall time will be O(n), making it amortized O(1).
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop()
 
    def peek(self):
        # Similar to the pop operation, the time complexity is amortized O(1).
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
 
    def empty(self):
        # Time complexity is O(1) as we are simply checking the length of the stacks.
        return len(self.inStack) == 0 and len(self.outStack) == 0
 
 # Create a queue
q = MyQueue()

# Push values into queue
q.push(1)
q.push(2)
q.push(3)

print("Peek first element:", q.peek())  # expect 1

print("Pop elements:")
print(q.pop())  # expect 1
print(q.pop())  # expect 2

print("Is empty?", q.empty())  # expect False

q.push(4)
print("Peek:", q.peek())  # expect 3 (front element)

print(q.pop())  # expect 3
print(q.pop())  # expect 4

print("Is empty?", q.empty())  # expect True
