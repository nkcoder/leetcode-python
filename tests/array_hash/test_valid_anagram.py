import unittest


from array_hash import valid_anagram


class ValidAnagramTest(unittest.TestCase):
    def test_valid_anagram(self):
        self.assertTrue(valid_anagram('anagram', 'nagaram'))
        self.assertFalse(valid_anagram('rat', 'car'))

    def test_valid_anagram2(self):
        self.assertTrue(valid_anagram('anagram', 'nagaram'))
        self.assertFalse(valid_anagram('rat', 'car'))

    def test_valid_anagram3(self):
        self.assertTrue(valid_anagram('anagram', 'nagaram'))
        self.assertFalse(valid_anagram('rat', 'car'))
