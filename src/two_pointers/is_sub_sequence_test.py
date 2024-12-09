from is_subsequence import is_subsequence


def test_is_subsequence():
    assert is_subsequence("abc", "ahbgdc")
    assert not is_subsequence("axc", "ahbgdc")
    assert is_subsequence("abc", "xacdbfkc")
