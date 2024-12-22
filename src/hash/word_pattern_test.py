from word_pattern import word_pattern

def test_word_pattern():
    assert word_pattern("abba", "dog cat cat dog") == True
    assert word_pattern("aaaa", "dog cat cat dog") == False
    assert word_pattern("aaaa", "dog cat cat dog") == False
    assert word_pattern("aaaa", "dog dog dog dog") == True
    assert word_pattern("abba", "dog dog dog dog") == False
