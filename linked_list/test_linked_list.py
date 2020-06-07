import unittest
import linked_list

class TestLinkedList(unittest.TestCase):

    def test_getSize(self):
        ll = linked_list.LinkedList()
        self.assertEqual(ll.getSize(), 0)
        ll.add('a') 
        ll.add('b') 
        
        self.assertEqual(ll.getSize(), 2)

    def test_peek(self):
        ll = linked_list.LinkedList()
        self.assertEqual(ll.peek(), None)
        ll.add('a') 
        ll.add('b') 
        
        self.assertEqual(ll.peek(), 'a')

    def test_clear(self):
        ll = linked_list.LinkedList()
        self.assertEqual(ll.clear(), True)
        ll.add('a') 
        ll.add('b') 
        self.assertEqual(ll.clear(), True)

    def test_removeAt(self):
        ll = linked_list.LinkedList()
            # Test out of bound
        with self.assertRaises(Exception):
            ll.removeAt(0)
        ll.add('a') 
        ll.add('b') 
        ll.add('c')

        self.assertEqual(ll.removeAt(1), 'b')
        self.assertEqual(ll.removeAt(0), 'a')
        self.assertEqual(ll.removeAt(0), 'c')

    def test_pop(self):
        ll = linked_list.LinkedList()
        # Test out of bound
        with self.assertRaises(Exception):
            ll.pop()
        ll.add('b') 
        ll.add('b') 
        ll.add('c')
        self.assertEqual(ll.pop(), 'b')
        self.assertEqual(ll.pop(), 'b')
        self.assertEqual(ll.pop(), 'c')

    def test_get(self):
        ll = linked_list.LinkedList()
        with self.assertRaises(Exception):
            ll.get(0)

        ll.add('b') 
        ll.add('a') 
        ll.add('c')

        self.assertEqual(ll.get(2), 'c')
        self.assertEqual(ll.get(1), 'a')
        self.assertEqual(ll.get(0), 'b')

    def test_indexOf(self):
        ll = linked_list.LinkedList()
        self.assertEqual(ll.indexOf('a'), -1)
        ll.add('b') 
        ll.add('a') 
        ll.add('c')

        self.assertEqual(ll.indexOf('a'), 1)
        self.assertEqual(ll.indexOf('b'), 0)
        self.assertEqual(ll.indexOf('c'), 2)

    def test_contains(self):
        ll = linked_list.LinkedList()
        self.assertEqual(ll.contains('a'), False)
        ll.add('b') 
        ll.add('a') 
        self.assertEqual(ll.contains('b'), True)
        self.assertEqual(ll.contains('b'), True)
        self.assertEqual(ll.contains('c'), False)


    def test_isEmpty(self):
        ll = linked_list.LinkedList()
        self.assertEqual(ll.isEmpty(), True)
        ll.add('b') 
        ll.add('a') 
        self.assertEqual(ll.isEmpty(), False)

    def test_toString(self):
        ll = linked_list.LinkedList()
        self.assertEqual(ll.toString(), 'None')
        ll.add('b') 
        ll.add('a') 
        self.assertEqual(ll.toString(), 'b-->a-->None')





if __name__ == '__main__':
    unittest.main()  