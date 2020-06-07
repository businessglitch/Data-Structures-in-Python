class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
        
        def toString(self):
            return str(self.data)

        
    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    # O(1)
    def size(self):
        return self.__size
    
    def peekFirst(self):
        if self.isEmpty(): raise Exception ('Cannot perform peek on empty list')

        return self.__head.data
    
    def peekLast(self):
        if self.isEmpty(): raise Exception ('Cannot perform peek on empty list')
        
        return self.__tail.data
         
    # Clears out the list in O(n) time
    def clear(self):
        trav = self.__head
        while trav is not None:
            next = trav.next
            trav.data = None
            trav.next =  trav.prev = None
            trav = next

        self.__head = self.__tail = None
        self.__size = 0

        return True
    
    # Adds to the back of the list FIFO O(n)
    def add(self, item: object):
        self.addLast(item)
      
    # Add to the head of the linked list
    def addFirst(self, item: object):
        if self.isEmpty():
            self.__head = self.__tail = self.Node(item)
        else:
            newNode = self.Node(item)
            self.__head.prev = newNode
            newNode.next = self.__head
            self.__head = newNode

        self.__size += 1

    # Add to the back(Tail) of the linked list
    def addLast(self, item: object):
        if self.isEmpty():
            self.__head = self.__tail = self.Node(item)
        else:
            newNode = self.Node(item)
            newNode.prev = self.__tail
            self.__tail.next = newNode
            self.__tail = newNode

        self.__size += 1

    def addAt(self, item: object, index:int):
        if index >= self.size() or index < 0: raise Exception ('Index:{} is out of bound'.format(index))

        if index == 0:
            self.addFirst(item)
            return
        
        if index == self.size():
            self.addLast(item)
            return

        i = 0
        trav = self.__head
        while i is not index:
            trav = trav.next

        newNode = self.Node(item)
        newNode.next = trav
        newNode.prev = trav.prev
        trav.prev.next = newNode
        trav.prev = newNode
        
        self.__size += 1

    def removeFirst(self):
        if self.isEmpty(): raise Exception('Cannot perform removeFirst on an empty list')

        next = self.__head.next
        data = self.__head.data
        self.__head.data =  self.__head.next = None
        self.__head = next
        self.__size -= 1

        if self.isEmpty():
            self.__tail = None

        return data

    def removeLast(self):
        if self.isEmpty(): raise Exception('Cannot perform removeFirst on an empty list')

        prev = self.__tail.prev
        data = self.__tail.data
        self.__tail.data =  self.__tail.prev = None
        self.__tail = prev
        self.__size -= 1

        if self.isEmpty():
            self.__head = None

        return data

    def __remove(self, node: Node) -> Node:
        node.next.prev = node.prev
        node.prev.next = node.next

        data = node.data
        node.next = node.prev =  None
        node.data = None
        self.__size -= 1

        return data

    # Remove item at index and return data. O(n)
    def removeAt(self, index: int):
        if index >= self.size() or index < 0: raise Exception ('Index:{} is out of bound'.format(index))

        if index == 0: return self.removeFirst()
        if index == self.size(): return self.removeLast()
        
        i = 0
        trav = self.__head
        while i is not index:
            trav = trav.next
            i += 1

        return self.__remove(trav)

    # Remove head and return data
    def pop(self):
        if self.isEmpty(): raise Exception ('Cannot pop from an empty list')

        next = self.__head.next
        data = self.__head.data

        self.__head.data = None
        self.__head.next = None
        self.__head = next
        self.__size -= 1
        return data
    
    def get(self, index: int):
        if index >= self.size() or index < 0: raise Exception ('Index:{} is out of bound'.format(index))

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
        return self.size() == 0

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