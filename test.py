import unittest
import main


class TestBubbleSort(unittest.TestCase):
    def test_with_positive_numbers(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        actual = main.Array([2, 3, 5, 4, 1, 7, 6]).bubble_sort()
        self.assertEqual(expected, actual)

    def test_with_positive_and_negative_numbers(self):
        expected = [-13, -5, 10, 12]
        actual = main.Array([-5, 12, -13, 10]).bubble_sort()
        self.assertEqual(expected, actual)

    def test_with_literals(self):
        expected = ['a', 'c', 't']
        actual = main.Array(['a', 't', 'c']).bubble_sort()
        self.assertEqual(expected, actual)

    def test_with_double_numbers(self):
        expected = [0.554, 1.2, 2.76, 9.4, 12.6]
        actual = main.Array([1.2, 9.4, 12.6, 0.554, 2.76]).bubble_sort()
        self.assertEqual(expected, actual)

    def test_with_sorted_numbers(self):
        expected = [0, 1, 2, 3, 4, 5]
        actual = main.Array([0, 1, 2, 3, 4, 5]).bubble_sort()
        self.assertEqual(expected, actual)

    def test_with_similar_elements(self):
        expected = [4, 4, 4, 4, 4]
        actual = main.Array([4, 4, 4, 4, 4]).bubble_sort()
        self.assertEqual(expected, actual)

    def test_with_similar_elements_literals(self):
        expected = ['q', 'q', 'q', 'q', 'q']
        actual = main.Array(['q', 'q', 'q', 'q', 'q']).bubble_sort()
        self.assertEqual(expected, actual)

    def test_with_empty_array(self):
        expected = []
        actual = main.Array([]).bubble_sort()
        self.assertEqual(expected, actual)

    def test_with_different_data(self):
        expected = [0.25, 1, 3, 'a', 'b']
        actual = main.Array([1, 3, 0.25, 'b', 'a']).bubble_sort()
        self.assertEqual(expected, actual)
