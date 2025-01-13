from palindrome_number import is_palindrome, is_palindrome_2

def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(-121) == False
    assert is_palindrome(10) == False

    assert is_palindrome_2(121) == True
    assert is_palindrome_2(-121) == False
    assert is_palindrome_2(10) == False
