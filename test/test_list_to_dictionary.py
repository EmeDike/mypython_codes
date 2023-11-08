import unittest
from Dictionary_task import dictionary_task2

class TestListToDictionary(unittest.TestCase):
    def test_dictionary_task2(self):
        my_list = ["apple", "banana", "orange", "mango"]
        expected_output = {'a': 'apple', 'b': 'banana', 'o': 'orange', 'm': 'mango'}
        actual_output = dictionary_task2.list_return_dictionary(my_list)
        self.assertEqual(actual_output, expected_output)

