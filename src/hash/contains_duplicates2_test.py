from contains_duplicates2 import containsNearbyDuplicate


def test_contains_duplicates2():
    assert containsNearbyDuplicate([1, 2, 3, 1], 3)
    assert containsNearbyDuplicate([1, 0, 1, 1], 1)
    assert not containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
