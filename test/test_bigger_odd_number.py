from unittest import TestCase
from Assessment_on_python import biggest_odd


class TestOddNumbers(TestCase):
    def test_bigger_odds(self):
        result = biggest_odd.biggest_odd_number("2345")
        self.assertEqual(result, 5)

    def test_empty_input(self):
        result = biggest_odd.biggest_odd_number("")
        self.assertIsNone(result)

    def test_all_even_numbers(self):
        result = biggest_odd.biggest_odd_number("2468")
        self.assertIsNone(result)

    def test_mixed_numbers(self):
        result = biggest_odd.biggest_odd_number("13579")
        self.assertEqual(result, 9)
