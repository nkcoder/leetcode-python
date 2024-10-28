from top_k_frequent import top_k_frequent2, top_k_frequent

def test_top_k_frequent():
    assert top_k_frequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert top_k_frequent([1, 2], 2) == [1, 2]

    actual = top_k_frequent(
        [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6,
            7,
            7,
            8,
            2,
            3,
            1,
            1,
            1,
            10,
            11,
            5,
            6,
            2,
            4,
            7,
            8,
            5,
            6,
        ],
        10,
    )
    expected = [1, 2, 5, 3, 6, 7, 4, 8, 10, 11]
    assert sorted(actual) == sorted(expected)


def test_top_k_frequent2():
    assert top_k_frequent2([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert top_k_frequent2([1], 1) == [1]
    assert top_k_frequent2([1, 2], 2) == [1, 2]

    actual = top_k_frequent2(
        [
            3,
            2,
            3,
            1,
            2,
            4,
            5,
            5,
            6,
            7,
            7,
            8,
            2,
            3,
            1,
            1,
            1,
            10,
            11,
            5,
            6,
            2,
            4,
            7,
            8,
            5,
            6,
        ],
        10,
    )
    expected = [1, 2, 5, 3, 6, 7, 4, 8, 10, 11]
    assert sorted(actual) == sorted(expected)
