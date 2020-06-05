lass LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
    def __init__(self):
        self.__length = 0
        self.__head = None

    # O(1)
    def getSize(self):
        return self.__length
    
    def peek(self):
        return self.__head.data
    
    # Clears out the list in O(n) time
    def clear(self):
        trav = self.__head

        while(trav.next is not None):
            next = trav.next
            trav.data = None
            trav.next = None
            trav = next
        
        self.__head = None
        self.__length = 0
    
    # Adds to the back of the list FIFO O(n)
    def add(self, item:object):
        # Assign as head if list is empty
        if (self.getSize() == 0):
           self. __head = self.Node(item)
        else: 
            trav = self.__head
            while(trav.next is not None):
                trav = trav.next
            trav.next = self.Node(item)

        self.__length += 1

    # Remove item at index and return data. O(n)
    def remove(self, index):
        if index >= self.getSize() or index < 0: raise Exception ('Index:{} is out of bound'.format(index))

        i = 0
        prev = None
        trav = self.__head

        while(i is not index):
            prev = trav
            trav = trav.next

        data = trav.data
        trav.data = None

        if prev is None:
            self.__head = None
        else:
            prev.next = trav.next

        self.__length -= 1

        return data
