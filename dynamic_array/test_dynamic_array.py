import unittest
import dynamic_array

class TestDynamicArray(unittest.TestCase):
    
    def test_add(self):
        arr = dynamic_array.Array()
        self.assertEqual(arr.size(), 0)
        arr.add('a')
        self.assertEqual(arr.get(0), 'a')
        self.assertEqual(arr.size(), 1)

    def test_size(self):
        # Empty Array
        arr = dynamic_array.Array()
        self.assertEqual(arr.size(), 0)

        # Size after Add operations
        arr.add('a')
        arr.add('b')
        self.assertEqual(arr.size(), 2)

        # Size after remove operations
        arr.remove('b')
        self.assertEqual(arr.size(), 1)

        # Size after clear operations
        arr.clear()
        self.assertEqual(arr.size(), 0)
    
    def test_isEmpty(self):
        # New Array
        arr = dynamic_array.Array()
        self.assertEqual(arr.isEmpty(), True)
        # After add operations
        arr.add('a')
        arr.add('b')
        arr.add('c')
        self.assertEqual(arr.isEmpty(), False)
        # After remove operations
        arr.remove('a')
        self.assertEqual(arr.isEmpty(), False)
        # After clear operation
        arr.clear()
        self.assertEqual(arr.isEmpty(), True)

    def test_get(self):
        arr = dynamic_array.Array()
        # Test lower bound
        with self.assertRaises(Exception):
            arr.get(0)
        
        # Test correct index value
        arr.add('a')
        arr.add('b')
        self.assertEqual(arr.get(0),'a')

        # Test upper bound
        with self.assertRaises(Exception):
            arr.get(2)

    def test_set(self):
        arr = dynamic_array.Array()
        arr.add('a')

        # Test out of bound
        with self.assertRaises(Exception):
            arr.set(1,'b')

        arr.set(0, 'b')
        self.assertEqual(arr.get(0), 'b')

    def test_clear(self):
        arr = dynamic_array.Array()
        # Test on empty array
        arr.clear()
        self.assertEqual(arr.size(), 0)
        arr.add('a')
        arr.add('b')
        arr.add('c')

        # Test on filled array
        arr.clear()
        self.assertEqual(arr.size(), 0)

    def test_removeAt(self):
        arr = dynamic_array.Array()

          # Test out of bound
        with self.assertRaises(Exception):
            arr.removeAt(0)

        arr.add('a')
        arr.add('b')
        arr.add('c')
        self.assertEqual(arr.removeAt(1), 'b')
        self.assertEqual(arr.get(1), 'c')
        self.assertEqual(arr.size(), 2)

    def test_remove(self):
        arr = dynamic_array.Array()
        arr.add('a')
        arr.add('b')
        # Remove a non present item
        self.assertEqual(arr.remove('c'), False)
        # Remove a present item
        self.assertEqual(arr.remove('a'), True)

    def test_indexOf(self):
        arr = dynamic_array.Array()
        arr.add('a')
        arr.add('b')
        # Index of non present item
        self.assertEqual(arr.indexOf('c'), -1)
        # Index of present item
        self.assertEqual(arr.indexOf('a'), 0)

    def test_contains(self):
        arr = dynamic_array.Array()
        arr.add('a')
        arr.add('b')
        self.assertEqual(arr.contains('c'), False)
        self.assertEqual(arr.contains('b'), True)
    
    def test_toString(self):
        arr = dynamic_array.Array()
        self.assertEqual(arr.toString(), '[]')

        arr.add('a')
        arr.add('b')
        arr.add('c')
        arr.add('d')
        self.assertEqual(arr.toString(), '[a,b,c,d]')

if __name__ == '__main__':
    unittest.main()