import unittest
from unittest import TestCase

import list_excercise


class TestListExercise(TestCase):
    def test_triple_elements(self):
        result = [3, 7, 2, 6, 5]
        output = [27, 343, 8, 216, 125]
        self.assertEqual(list_excercise.triple_element_function(result), output)

if __name__ == '__main__':
    unittest.main()
