from linked_list import Node

# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

class Stack:
    def __init__(self, val=None):
        self.top = None
        self.next = None
        self.size = 0
        if val:
            self.top = Node(val)
            self.size += 1
    
    def empty(self):
        return self.top != None
    
    def size(self):
        return self.size
    
    def peek(self):
        return self.top
    
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
    
    def pop(self):
        val = self.head.val
        node = self.head
        self.head = self.head.next
        del node
        return val