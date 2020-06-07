class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
        def toString(self):
            return str(self.data)

        
    def __init__(self):
        self.__length = 0
        self.__head = None

    # O(1)
    def getSize(self):
        return self.__length
    
    def peek(self):
        if self.__head: 
            return self.__head.data
        else: 
           return None
         
    # Clears out the list in O(n) time
    def clear(self):
        if self.isEmpty():
            return True
        else:

            while self.__head.next is not None:
                next = self.__head.next
                self.__head.data = None
                self.__head.next = None
                self.__head = next

            self.__head.data = None
            self.__head = None
            self.__length = 0

            return True
    
    # Adds to the back of the list FIFO O(n)
    def add(self, item: object):
        # Assign as head if list is empty
        if self.getSize() == 0:
           self. __head = self.Node(item)
        else: 
            trav = self.__head
            while trav.next is not None:
                trav = trav.next
            trav.next = self.Node(item)

        self.__length += 1

    # Remove item at index and return data. O(n)
    def removeAt(self, index: int):
       
        if index >= self.getSize() or index < 0: raise Exception ('Index:{} is out of bound'.format(index))

        i = 0
        prev = None
        trav = self.__head

        while i is not index:
            prev = trav
            trav = trav.next
            i += 1

        next = trav.next
        data = trav.data
        trav.data = None
        trav.next = None
        trav = None

        if prev is not None:
            prev.next = next
        else:
            self.__head = next
      

        self.__length -= 1

        return data

    # Remove head and return data
    def pop(self):
        if self.isEmpty(): raise Exception ('Cannot pop from an empty list')

        next = self.__head.next
        data = self.__head.data

        self.__head.data = None
        self.__head.next = None
        self.__head = next
        self.__length -= 1
        return data
    
    def get(self, index: int):
        if index >= self.getSize() or index < 0: raise Exception ('Index:{} is out of bound'.format(index))

        i = 0
        trav = self.__head
        while i is not index:
            trav = trav.next
            i += 1
        
        return trav.data
    
    def indexOf(self, item: object):
        if self.isEmpty(): return -1

        i = 0
        trav= self.__head
        while trav is not None:
            if trav.data == item:
                return i
            trav = trav.next
            i += 1

        return -1

    def contains(self, item: object):
        return self.indexOf(item) is not -1

    def isEmpty(self):
        return self.getSize() == 0

    def toString(self):
        if self.isEmpty():
            return 'None'
        
        trav = self.__head
        string = trav.toString()
        while trav.next is not None:
            trav = trav.next
            string += '-->'
            string += trav.toString()

        string += '-->'
        string += 'None'

        return string