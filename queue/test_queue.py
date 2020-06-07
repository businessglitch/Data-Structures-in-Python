import unittest
from queue import Queue

class TestLinkedList(unittest.TestCase):
    def test_size(self):
        q = Queue()
        self.assertEqual(q.size(), 0)

        q.enqueue('a')
        q.enqueue('b')
        q.enqueue('c')
        self.assertEqual(q.size(), 3)

    def test_isEmpty(self):
        q = Queue()
        self.assertEqual(q.isEmpty(), True)
        q.enqueue('a')
        self.assertEqual(q.isEmpty(), False)

    def test_getFront(self):
        q = Queue()
        with self.assertRaises(Exception):
            q.getFront()
        q.enqueue('a')
        q.enqueue('b')
        self.assertEqual(q.getFront(), 'a')
    
    def test_dequeue(self):
        q = Queue()
        with self.assertRaises(Exception):
            q.dequeue()
        
        q.enqueue('a')
        q.enqueue('b')

        self.assertEqual(q.size(), 2)
        self.assertEqual(q.dequeue(), 'a')
        self.assertEqual(q.dequeue(), 'b')

        

if __name__ == '__main__':
    unittest.main()