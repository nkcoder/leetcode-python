from collections import Counter


# EASY: https://leetcode.com/problems/valid-anagram/description/

def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}

    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1

    for c in s:
        if count_s[c] != count_t.get(c, 0):
            return False

    return True


def valid_anagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def valid_anagram3(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == '__main__':
    assert valid_anagram('anagram', 'nagaram') == True
    assert valid_anagram('rat', 'car') == False
    assert valid_anagram2('anagram', 'nagaram') == True
    assert valid_anagram2('rat', 'car') == False
    assert valid_anagram3('anagram', 'nagaram') == True
    assert valid_anagram3('rat', 'car') == False
