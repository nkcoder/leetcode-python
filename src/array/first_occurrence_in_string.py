def first_occurrence_in_string(haystack: str, needle: str) -> int:
    for i in range(0, len(haystack)):
        if haystack[i : i + len(needle)] == needle:
            return i
    return -1
