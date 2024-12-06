from majority_element import majority_element, majority_element_moore_voting, majority_element_sort


def test_majority_element():
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


def test_majority_element_sort():
    assert majority_element_sort([3, 2, 3]) == 3
    assert majority_element_sort([2, 2, 1, 1, 1, 2, 2]) == 2


def test_majority_element_2():
    assert majority_element_moore_voting([3, 2, 3]) == 3
    assert majority_element_moore_voting([2, 2, 1, 1, 1, 2, 2]) == 2
