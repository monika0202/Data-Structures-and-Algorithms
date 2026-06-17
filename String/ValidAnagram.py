# LeetCode 242 - Valid Anagram
# frequency count
# TC: O(n)
# SC: O(n)

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
