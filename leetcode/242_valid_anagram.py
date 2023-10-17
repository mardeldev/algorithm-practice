"""
242. Valid Anagram
Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

def anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_set, t_set = {}, {}
    for i in range(len(s)):
        s_set[s[i]] = 1 + s_set.get(s[i], 0)
        t_set[t[i]] = 1 + t_set.get(t[i], 0)
    return s_set == t_set

s = "anagram"
t = "grmanaa"
print(anagram(s, t))