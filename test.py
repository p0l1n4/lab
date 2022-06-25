import unittest
import main


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort_1(self):
        expected = [1, 2, 3, 4, 5, 6, 7]
        actual = main.Array([2, 3, 5, 4, 1, 7, 6]).bubble_sort()
        self.assertEqual(expected, actual)

    def test_bubble_sort_2(self):
        expected = [-13, -5, 10, 12]
        actual = main.Array([-5, 12, -13, 10]).bubble_sort()
        self.assertEqual(expected, actual)

    def test_bubble_sort_3(self):
        expected = [-999, -123, 0, 54, 666]
        actual = main.Array([0, -123, 54, 666, -999]).bubble_sort()
        self.assertEqual(expected, actual)

    def test_bubble_sort_4(self):
        expected = [-6, 0, 0, 5, 5, 616]
        actual = main.Array([0, 0, -6, 616, 5, 5]).bubble_sort()
        self.assertEqual(expected, actual)

    def test_bubble_sort_5(self):
        expected = ['a', 'c', 't']
        actual = main.Array(['a', 't', 'c']).bubble_sort()
        self.assertEqual(expected, actual)

    def test_bubble_sort_6(self):
        expected = [0.554, 1.2, 2.76, 9.4, 12.6]
        actual = main.Array([1.2, 9.4, 12.6, 0.554, 2.76]).bubble_sort()
        self.assertEqual(expected, actual)
