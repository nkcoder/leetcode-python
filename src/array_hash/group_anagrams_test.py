from group_anagrams import group_anagrams, group_anagrams2


# the result should contain the same element, the order of the elements don't matter
def test_group_anagrams():
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    assert sorted(group_anagrams(["a", "ab"])) == sorted([["a"], ["ab"]])
    sorted(group_anagrams(["bdddddddddd", "bbbbbbbbbbc"])) == sorted(
        [["bbbbbbbbbbc"], ["bdddddddddd"]]
    )

    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert len(result) == len(expected)


def test_group_anagrams2():
    assert group_anagrams2([""]) == [[""]]
    assert group_anagrams2(["a"]) == [["a"]]
    assert sorted(group_anagrams2(["a", "ab"])) == sorted([["a"], ["ab"]])
    sorted(group_anagrams2(["bdddddddddd", "bbbbbbbbbbc"])) == sorted(
        [["bbbbbbbbbbc"], ["bdddddddddd"]]
    )

    result = group_anagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert len(result) == len(expected)
