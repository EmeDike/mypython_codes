from unittest import TestCase
from mypythonassignments.list_assignments import personal_assignment_compare_string


class Test(TestCase):
    def test_compare_two_strings(self):
        result = personal_assignment_compare_string.equal_strings("love", "evol")
        self.assertTrue(result)
