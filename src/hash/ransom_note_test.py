from ransom_note import ransom_note


def test_ransom_note():
    assert ransom_note("a", "b")  == False
    assert ransom_note("aa", "ab") == False
    assert ransom_note("aa", "aab") == True
