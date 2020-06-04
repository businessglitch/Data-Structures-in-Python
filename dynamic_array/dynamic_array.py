import math

class Array:
    __length = 0 #This is what the users think the array size is

    def __init__(self, capacity = 16):
        #Intialize with the capiacity defined
        if capacity <= 0:  raise Exception('Capacity should be greater than 0')
        self.__capacity = capacity
        self.__arr = list([None]*capacity)

    def size(self):
        return self.__length
    
    def isEmpty(self):
        return self.size() == 0
    
    def get(self, index:int):
        if index >= self.size(): raise Exception('Index: {} is out of bound'.format(index))
        return self.__arr[index]

    def set(self, index:int, item):
        if index >= self.size(): raise Exception('Index: {} is out of bound'.format(index))
        self.__arr[index] = item
        
    def clear(self):
        for i in range(self.size()):
            self.__arr[i] = None
        self.__length = 0

    def add(self, item):
        # Resize Array if we reach the maximum capacity
        if(self.size() + 1 >= self.__capacity):
            self.__capacity *= 2
            new_arr = list([None] * self.__capacity)

            for i, element in enumerate(self.__arr):
                new_arr[i] = element

            self.__arr = new_arr 

        self.__arr[self.size()] =  item
        self.__length += 1 

    def removeAt(self, index:int):
        if(index >= self.size()  or index < 0): raise Exception('Index: {} is out of bound'.format(index))

        # Decrease array size if length reaches half the capacity
        if self.size() <= math.ceil(self.__capacity / 2):
            self.__capacity = math.ceil(self.__capacity / 2)
        else:
            self.__capacity -= 1
       
        new_arr = list([None] * self.__capacity)
        data = self.__arr[index]
        
        i = 0
        j = 0
        while i < self.size():
            # Skip the item to be removed
            if i is not index:
                new_arr[j] = self.__arr[i]
                j += 1
                
            i += 1


        self.__arr = new_arr
        self.__length -= 1

        return data

    def remove(self, item: object):
        for i in range(self.size()):
            if self.__arr[i] == item:
                self.removeAt(i)
                return True
            
        return False

    def indexOf(self, item: object):
        for i in range(self.size()):
            if self.__arr[i] == item:
                return i
            
        return -1
    
    def contains(self, item:object): 
        return indexOf(item) is not -1
    
    
    def toString(self):
        if self.size() == 0:
            return '[]'
        
        string = '['
        for i in range(self.size()):
            string += str(self.__arr[i])
            if i is not self.size() - 1:
                string += ','

        string += ']'

        return string
        
        
# # Some Tests
# my_arr = Array(4)
# print('Size: ', my_arr.size())
# my_arr.add(3)
# my_arr.add(1)
# my_arr.add(2)
# my_arr.add(4)
# print('Size: ', my_arr.size())
# print('ToString: ', my_arr.toString())
