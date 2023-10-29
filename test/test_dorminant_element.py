from unittest import TestCase
from mypythonassignments.list_assignments import check_dorminant_element

class Test(TestCase):
    def test_dominant_elements(self):
        my_list = [1, 2, 3, 9, 7, 4]
        output = [9, 7, 4]
        result = check_dorminant_element.check_dominant_elements(my_list)
        self.assertTrue(result, output)