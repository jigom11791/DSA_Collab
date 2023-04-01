class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val=None):
        if val:
            self.head = self.tail = Node(val)
        else:
            self.head = self.tail = None

    def __str__(self):
        curr = self.head
        s = ""
        while curr:
            s+= str(curr.val)
            if curr.next:
                s+= " => "
            curr = curr.next
        return s
    
    def append(self, val):
        if not self.head:
            self.head = self.tail = Node(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def append(self, *args):
        for a in args:
            if self.head:
                self.tail.next = Node(a)
                self.tail = self.tail.next
            else:
                self.head = self.tail = Node(a)
    
    def remove(self):
        curr = self.head
        while not curr.next == self.tail:
            curr = curr.next

        val = self.tail.val
        self.tail = curr
        self.tail.next = None
        return val

