import unittest
from unittest import TestCase
import tuple_find_duplicates
import tuple_reverse
import tuple_get_values_and_indices


class WeekendListSnacks(TestCase):
    def test_tuple_reverse(self):
        given_tuple = (10, 20, 30, 40, 50)
        output = (50, 40, 30, 20, 10)
        self.assertEqual(tuple_reverse.reverse_elements_in_tuple(given_tuple), output)

    def test_find_duplicates(self):
        input_tuple = (10, 20, 30, 20, 40, 10, 50)
        expected_duplicates = {10, 20}
        seen, duplicates = tuple_find_duplicates.display_duplicates_of_tuple(input_tuple)
        self.assertEqual(seen, set(input_tuple))
        self.assertEqual(duplicates, expected_duplicates)

    def test_get_values_and_indices(self):
        input_tuple = ("Orange", [10, 20, 30], (5, 15, 25))
        result_list = ((1, 2), (2, 2))
        self.assertEqual(tuple_get_values_and_indices.get_values_and_indices(input_tuple, result_list))


if __name__ == '__main__':
    unittest.main()
