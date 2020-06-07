import sys
sys.path.append('../')
from linked_list.linked_list import LinkedList

class Queue:
    def __init__(self):
        self.list = LinkedList()

     # Get the size of the queue
    def size(self) -> int:
        return self.list.size()

    # Check if the queue is empty
    def isEmpty(self) -> bool:
        return self.size() == 0

    # Get the value of an item from the front of a queue
    def getFront(self) -> object: 
        if(self.isEmpty()): raise Exception('Cannot perform peek on an empty list')
        return self.list.peekFirst()
    
    # Remove an item from the front of a queue
    def dequeue(self) -> LinkedList.Node:
        if(self.isEmpty()): raise Exception('Cannot perform poll on an empty list')
        return self.list.removeFirst()

    # Add item to the back of the queue
    def enqueue(self, item: object): 
        if item is None: return Exception('Cannot add a None object')
        self.list.addLast(item)