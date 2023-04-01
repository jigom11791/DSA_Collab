# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

from jgom.linked_list import Node


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
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        curr = self.top
        s = ""
        while curr:
            s+= str(curr.val)
            if curr.next:
                s+= " => "
            curr = curr.next
        return s
    
    def peek(self):
        if self.top:
            return self.top.val
        else:
            return None
    
    def push(self, val):
        if self.top:
            node = Node(val)
            node.next = self.top
            self.top = node
        else:
            self.top = Node(val)
        self.size += 1
    
    def pop(self):
        if self.top:
            val = self.top.val
            node = self.top
            if self.top.next:
                self.top = self.top.next
                del node
            else:
                self.top = None
            return val
            self.size -= 1