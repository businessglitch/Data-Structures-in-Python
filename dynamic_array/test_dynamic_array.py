import unittest
import dynamic_array

class TestDynamicArray(unittest.TestCase):
    
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



if __name__ == '__main__':
    unittest.main()