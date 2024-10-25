import unittest

from src.array_hash.contains_duplicate import ContainsDuplicate


class ContainsDuplicateTestCase(unittest.TestCase):
    def test_duplicate(self):
        self.assertEqual(ContainsDuplicate.contains_duplicate([1, 2, 3, 1]), True)
        self.assertEqual(ContainsDuplicate.contains_duplicate([1, 2, 3, 4]), False)
        self.assertEqual(ContainsDuplicate.contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)
