from collections import Counter

from valid_anagram import valid_anagram, valid_anagram2, valid_anagram3


def test_valid_anagram():
    assert valid_anagram('anagram', 'nagaram') == True
    assert valid_anagram('rat', 'car') == False
    assert valid_anagram2('anagram', 'nagaram') == True
    assert valid_anagram2('rat', 'car') == False
    assert valid_anagram3('anagram', 'nagaram') == True
    assert valid_anagram3('rat', 'car') == False
