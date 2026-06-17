# 438 Find All Anagrams in a String
# Sliding Window + Frequency Count
# TC: O(n)
# SC: O(1)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n = len(s)
        m = len(p)

        if m > n:
            return []

        p_count = [0] * 26
        window = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        for i in range(m):
            window[ord(s[i]) - ord('a')] += 1

        result = []

        if window == p_count:
            result.append(0)

        for i in range(m, n):

            window[ord(s[i]) - ord('a')] += 1

            window[ord(s[i - m]) - ord('a')] -= 1

            if window == p_count:
                result.append(i - m + 1)

        return result
