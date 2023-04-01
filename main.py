# comment out and add your own
from jgom.linked_list import LinkedList
from jgom.stack import Stack


if __name__ == "__main__":

    ###################################
    #      Single Linked List         #
    ###################################
    print('== Linked List ==')
    # create Linked list class and instantiate linked list item
    linked = LinkedList(10)

    # create "to string class function"
    print(f'Test to string function: \n\t{linked}')

    # create a "to string" class funtion
    linked.append(20)
    print(f'Test append to linked List:\n\t{linked}')

    # create class function to append multiple
    linked.append(20,30,40,50)
    print(f"Test append multiple to linked list: \n\t{linked}")

    # create class function to remove last node
    linked.remove()
    print(f'Test remove from linked list: \n\t{linked}\n')

    ####################################
    #         stack                    #
    ####################################
    # functions associated with stack
    # empty() – Returns whether the stack is empty – Time Complexity: O(1)
    # size() – Returns the size of the stack – Time Complexity: O(1)
    # top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
    # push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
    # pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

    print('== Stack ==')
    # initialize the stack
    stack = Stack(10)

    # Test empty()
    print(f'Test empty(): \n\t{stack.empty()}')

    # Test size()
    print(f"Test size: \n\t{len(stack)}")

    # Test peek():
    print(f"Test peek(): \n\t{stack.peek()}")

    # Test push()
    print(f'Test push(): \n\tTop Before: {stack.peek() }')
    stack.push(40)
    print(f"\tTop After: { stack.peek() }")

    # Test pop()
    print(f"Test pop():\n\tCurrent Top: {stack.peek() }")
    stack.pop()
    print(f'\tNew Top: { stack.peek() }')
    stack.pop()
    print(f"\tNew Top: { stack.peek()}")