import unittest

from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    """
    Class for testing different parts of the merge_sort algorithm
    """

    def test_issorted(self):
        """
        Tests if merge_sort returns a sorted list
        """
        unsorted = [2, 52, 12, 51, 43]
        sorted_ = [2, 12, 43, 51, 52]

        test_merge = merge_sort(unsorted)
        self.assertTrue(sorted_ == test_merge)


if __name__ == "__main__":
    unittest.main()
