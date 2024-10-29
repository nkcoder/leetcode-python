from palindrome import is_palindrome


def test_palindrome():
    s = "A man, a plan, a canal: Panama"
    assert is_palindrome(s) == True


def test_non_palindrome():
    s = "race a car"
    assert is_palindrome(s) == False


def test_empty_input():
    s = ""
    assert is_palindrome(s) == True


def test_upper_case_input():
    s = "abc d ! D C b a"
    assert is_palindrome(s) == True
