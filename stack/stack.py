import sys
sys.path.append('../')
from linked_list.linked_list import LinkedList

class Stack:
    def __init__(self):
        self.list = LinkedList()

     # Get the size of the stack
    def size(self) -> int:
        return self.list.size()

    # Check if the stack is empty
    def isEmpty(self) -> bool:
        return self.size() == 0

    # Get the value of an item from the top of a stack
    def peek(self) -> object: 
        if(self.isEmpty()): raise Exception('Cannot perform peek on an empty list')
        return self.list.peekLast()
    
    # Remove an item from the top of a stack
    def pop(self) -> LinkedList.Node:
        if(self.isEmpty()): raise Exception('Cannot perform poll on an empty list')
        return self.list.removeLast()

    # Add item to the back of the stack
    def push(self, item: object): 
        if item is None: return Exception('Cannot add a None object')
        self.list.addLast(item)