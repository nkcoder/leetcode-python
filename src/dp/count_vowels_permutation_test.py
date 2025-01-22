from count_vowels_permutation import count_vowels_permutation_hash, count_vowels_permutation_array


def test_count_vowels_permutation():
    assert count_vowels_permutation_hash(1) == 5
    assert count_vowels_permutation_hash(2) == 10
    assert count_vowels_permutation_hash(5) == 68

    assert count_vowels_permutation_array(1) == 5
    assert count_vowels_permutation_array(2) == 10
    assert count_vowels_permutation_array(5) == 68
