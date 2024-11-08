from collections import Counter
from three_sum import three_sum


def test_three_sum_all_triplets():
    result = three_sum([-1, 0, 1, 2, -1, -4])
    expect = [[-1, -1, 2], [-1, 0, 1]]
    assert are_list_equal(result, expect) == True


def test_three_sum_only_one_triples():
    result = three_sum([0, 0, 0])
    expect = [[0, 0, 0]]
    assert are_list_equal(result, expect) == True


def test_three_sum_no_triples():
    result = three_sum([0, 1, 1])
    expect = []
    assert are_list_equal(result, expect) == True


def are_list_equal(x: list[list[int]], y: list[list[int]]) -> bool:
    print(f"x = {x}, y = {y}")
    if len(x) != len(y):
        return False

    # tuple is hashable and can be counted (list can't)
    sorted_x = [tuple(sorted(inner)) for inner in x]
    sorted_y = [tuple(sorted(inner)) for inner in y]

    counter_x = Counter(sorted_x)
    counter_y = Counter(sorted_y)

    return counter_x == counter_y
