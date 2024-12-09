from first_occurrence_in_string import first_occurrence_in_string


def test_first_occurrence_in_string():
    assert first_occurrence_in_string("sadbutsad", "sad") == 0
    assert first_occurrence_in_string("leetcode", "leeto") == -1
