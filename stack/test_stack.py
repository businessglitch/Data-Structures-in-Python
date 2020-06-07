import unittest
from stack import Stack

class TestLinkedList(unittest.TestCase):
    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)

        s.push('a')
        s.push('b')
        s.push('c')
        self.assertEqual(s.size(), 3)

    def test_isEmpty(self):
        s = Stack()
        self.assertEqual(s.isEmpty(), True)
        s.push('a')
        self.assertEqual(s.isEmpty(), False)

    def test_peek(self):
        s = Stack()
        with self.assertRaises(Exception):
            s.peek()
        s.push('a')
        s.push('b')
        self.assertEqual(s.peek(), 'b')
    
    def test_pop(self):
        s = Stack()
        with self.assertRaises(Exception):
            s.pop()
        
        s.push('a')
        s.push('b')

        self.assertEqual(s.size(), 2)
        self.assertEqual(s.pop(), 'b')
        self.assertEqual(s.pop(), 'a')

        

if __name__ == '__main__':
    unittest.main()